# import joblib
from django.shortcuts import render
# from django.http import HttpResponse
# from Chatbot_Hei.websiteapp.chat import FileResponse
# from django import template
# from rest_framework import viewsets

from .chat import *


# from chat import get_response


# Create your views here.

def index(request):
    templates = 'index.html'
    return render(request, templates)


def about(request):
    templates = 'about.html'
    return render(request, templates)


def course(request):
    templates = 'course.html'
    return render(request, templates)


def blog(request):
    templates = 'blog.html'
    return render(request, templates)


def contact(request):
    templates = 'contact.html'
    return render(request, templates)


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import sys


@csrf_exempt
def predict(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data.get('message')
        # TODO: check if text is valid
        response = get_response(text)
        message = {"answer": response}
        return JsonResponse(message)
    else:
        return JsonResponse({"error": "Invalid Request Method"})


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)





