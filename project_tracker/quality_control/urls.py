from django.urls import path
from quality_control import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.index, name='index'),  # Добавлено имя 'index'
    path('bug_list/', views.bug_list, name='bug_list'),  # Добавлено имя 'another_page'
    path('feature_list/', views.feature_list, name='feature_list'),  # Добавлено имя 'another_page'
    path('bug_detail/<int:bug_id>/', views.bug_detail, name='bug_detail'),  # Добавлено имя 'another_page'
    path('feature_detail/<int:feature_id>/', views.feature_detail, name='feature_detail'),  # Добавлено имя 'another_page'
]