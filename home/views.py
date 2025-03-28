from django.shortcuts import render, redirect
import json
from django.conf import settings
import os


def home(request):
    '''
    Render Homepage
    '''
    return render(request, 'home/index.html')

def women_in_tech(request):
    '''
    Render Women in Tech page
    '''
    return render(request, 'home/women_in_tech.html') 

def team(request):
    '''
    Render Team page
    '''
    return render(request, 'home/team.html')

def contact(request):
    '''
    Render Contact page
    '''
    return render(request, 'home/contact.html')  # Render the team.html template
def mentor(request):
    '''
    Render mentor page
    '''
    return render(request, 'home/mentor.html')  # Render the team.html template

def about(request):
    '''
    Render about page
    '''
    return render(request, 'home/about.html')  # Render the team.html template

def questions(request):
    # Load the JSON file
    json_file_path = os.path.join(settings.BASE_DIR, 'home/static/data/faq.json')
    with open(json_file_path, 'r') as file:
        faq_data = json.load(file)

    success_message = None  # Initialize the success message

    if request.method == "POST":
        # Get form data
        heading = request.POST.get("heading")
        question = request.POST.get("question")

        # Save the question temporarily (for admin approval)
        temp_file_path = os.path.join(settings.BASE_DIR, 'home/static/data/temp_questions.json')
        if os.path.exists(temp_file_path):
            with open(temp_file_path, 'r') as temp_file:
                temp_questions = json.load(temp_file)
        else:
            temp_questions = []

        temp_questions.append({"heading": heading, "question": question})
        with open(temp_file_path, 'w') as temp_file:
            json.dump(temp_questions, temp_file, indent=4)

        # Set the success message
        success_message = "Thank you for submitting your question! It is under review and will be displayed once approved."

    return render(request, 'home/questions.html', {'faq_data': faq_data, 'success_message': success_message})

