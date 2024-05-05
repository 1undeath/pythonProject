from django.http import HttpResponse
from django.urls import reverse


def index(request):
    another_page_url = reverse('tasks:another_page')  # Исправлено имя URL
    html = f"<h1>Система контроля качества1</h1>#<a href='{another_page_url}'>Перейти на другую страницу</a>"
    return HttpResponse(html)

def another_page(request):  # Исправлена опечатка в названии аргумента
    return HttpResponse("Это другая страница приложения tasks")
