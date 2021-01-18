from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


# CSRF = Cross Site Resource Forgery
@csrf_exempt
def get_news(request):
    if request.method == 'POST':
        data = {
            'response': 'Hello World!'
        }
        return JsonResponse(data)
    return HttpResponse('Hello from get response')
