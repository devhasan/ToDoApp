from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('createtask/', views.createtask, name='createtask'),
    path('details/<int:id>', views.home, name='details'),
    path('edit/<int:id>/', views.edit_task, name='edit'),
    path('delete/<int:id>/', views.delete_task, name='delete')
]