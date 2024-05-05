from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),  # Добавлено имя 'index'
    path('bug_list/', views.bug_list, name='bug_list'),  # Добавлено имя 'another_page'
    path('feature_list/', views.feature_list, name='feature_list'),  # Добавлено имя 'another_page'
]