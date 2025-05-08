from django.urls import path
from .views import home_page_view, create_task_view, delete_task_view, edit_task_view, update_task_view

urlpatterns = [
    path('', home_page_view, name='HomePage'),
    path('created/', create_task_view, name='create_task'),
    path('deleted/<int:pk>/', delete_task_view, name='delete_task'),
    path('edit/<int:pk>/', edit_task_view, name='edit_task'),
    path('update/<int:pk>/', update_task_view, name='update_task'),
]
