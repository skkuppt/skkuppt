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
                response = requests.post(
                    f'http://{BACKEND_HOST}:{BACKEND_PORT}/api/question/create',
                    headers={'Content-Type': 'application/json'},
                    json={'topic': topic, 'details': details}
                )
                response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
                
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
        answer = result.get('answer', '').split('\n\n')
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
