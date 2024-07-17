from django.shortcuts import render
from .utils import generate_image

def generate_image_home(request):
    if request.method == 'POST':
        print("hello")
        prompt = request.POST.get('prompt', '')  # Get the prompt from the form
        generated_image_path = generate_image(prompt)
        return render(request, 'generate_image_home.html', {'generated_image_path': generated_image_path})
    else:
        return render(request, 'generate_image_home.html', {'generated_image_path': None})
