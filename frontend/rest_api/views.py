import logging
import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from multiprocessing import Process, Queue
import os

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = 'gpt-3.5-turbo'
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}"
}

system_role_content = {"role": "system", "content": "You are making ppt for the class, skilled in making index and its belongings.showing only the title and content of the slides without other flowery words or summary or etc."}
url = "https://api.openai.com/v1/chat/completions"




def get_prompt(topic:str, details:str)->str:
    prompt = f"""
    make a powerpoint presentation about {topic} with the following details:
    {details}
    In the structure of:
    Slide 1:
    Title:
    Content:
    Slide 2:
    Title:
    Content:
    ...  
    Slide n:
    Title:
    Content:
    Only write the title of the slides and its content. 
    """
    return prompt

def get_data(topic:str, details:str)->dict:
	prompt=get_prompt(topic, details)
	user_role_content = {"role": "user", "content": prompt}
	data = {
    	"model": "gpt-3.5-turbo",
    	"messages": [system_role_content, user_role_content],
    	"temperature": 0.7
	}
	return data


@login_required
def index(request):
    logger.info('Rendering index page for create_ppt')
    return render(request, 'create_ppt.html')


@login_required
@csrf_exempt
def create_ppt(request):
    logger.info('Received a request to create a PPT')
    
    if request.method == 'POST':
        topic = request.POST.get('topic')
        details = request.POST.get('details')
        logger.info(f'Received POST data with topic: {topic}')

        # Create a queue for inter-process communication
        queue = Queue()

        # Define the target function for the process
        def task(queue, topic, details):
            try:
                BACKEND_HOST = os.environ.get("BACKEND_HOST", "localhost")
                BACKEND_PORT = os.environ.get("BACKEND_PORT", "8000")
                #response = requests.post(
                    #f'http://{BACKEND_HOST}:{BACKEND_PORT}/api/question/create',
                    #headers={'Content-Type': 'application/json'},
                    #json={'topic': topic, 'details': details}
                #)
                response = requests.post(url=url, headers=headers, json=get_data(topic, details))
                response.raise_for_status()  
                
                result = response.json()
                queue.put(result)
                logger.info('Successfully put result in queue')
            except requests.HTTPError as http_err:
                logger.error(f'HTTP error occurred: {http_err}')  # Python 3.6+
                queue.put(None)
            except Exception as err:
                logger.error(f'Other error occurred: {err}')  # Python 3.6+
                queue.put(None)

        # Start the separate process
        process = Process(target=task, args=(queue, topic, details))
        process.start()
        logger.info('Started process to create PPT')

        # Wait for the result from the process
        result = queue.get()

        process.join()  # Ensure the process has finished
        logger.info('Process joined, processing results')

        if result is None:
            logger.error('Did not receive a valid response from the backend service')
            return JsonResponse({'error': 'Backend service did not respond correctly'}, status=500)

        slides = {}

        answer = result['choices'][0]['message']['content'].split('\n\n')
        for i, slide in enumerate(answer, start=1):
            if slide:
                title_key = f'Slide {i}:\nTitle:'
                content_key = '\nContent:'
                title_start = slide.find(title_key) + len(title_key)
                content_start = slide.find(content_key) + len(content_key)
                title = slide[title_start:slide.find('\n', title_start)].strip()
                tmp_list = title.split(": ")
                if len(tmp_list) > 1:
                    title = tmp_list[-1]
                content = slide[content_start:].strip()
                slides[str(i)] = {'title': title, 'content': content}

        logger.info('Successfully processed slides for PPT')
        return render(request, 'create_ppt.html', {'slides': slides})
    else:
        logger.warning('create_ppt called with non-POST method')
        return JsonResponse({'error': 'Invalid method'}, status=405)
