from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),          # Screen 1
    path('add/', views.add_task, name='add_task'),          # Screen 2
    path('edit/<int:id>/', views.edit_task, name='edit_task'), # Screen 3
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
