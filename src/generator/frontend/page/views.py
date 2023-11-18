import requests
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os

@csrf_exempt
# http:<url>/api/create_ppt
def create_ppt(request):

    if request.method == 'POST':
        # Extract the topic and content from the POST request
        topic = request.POST.get('topic')
        content = request.POST.get('content')

        # Send the POST request to the API endpoint
        BACKEND_HOST=os.environ.get("BACKEND_HOST", "localhost")
        BACKEND_PORT=os.environ.get("BACKEND_PORT", "8000")
        response = requests.post(
            f'http://{BACKEND_HOST}:{BACKEND_PORT}/api/question/create',
            headers={'Content-Type': 'application/json'},
            json={'topic': topic, 'content': content}
        )

        # Process the JSON response to convert it into the desired format
        result = response.json()
        slides = {}
        answer = result.get('answer').split('\n\n')
        print(answer)
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

        print(slides)
        return render(request, 'index.html', {'slides': slides})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)

# http:<url>/
def index(request):
    # Render the index page with no context if not called by create_ppt
    return render(request, 'index.html')
