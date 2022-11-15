from django.http import HttpRequest

def index(request):
    return HttpRequest('Привет это главная страница!')
