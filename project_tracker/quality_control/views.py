from django.http import HttpResponse
from django.urls import reverse


def index(request):
    bug_page_url = reverse('quality_control:bug_list')  # Исправлено имя URL
    feature_page_url = reverse('quality_control:feature_list')  # Исправлено имя URL
    html = f"<h1>Система контроля качества1</h1>#<a href='{bug_page_url}'>Список всех багов</a>#<a href='{feature_page_url}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):  # Исправлена опечатка в названии аргумента
    return HttpResponse("Cписок отчетов об ошибках")

def feature_list(request):  # Исправлена опечатка в названии аргумента
    return HttpResponse("Список запросов на улучшение")
