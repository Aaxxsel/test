from django.urls import path

from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/list/', views.tasks_list, name='tasks_list'),
    path('tasks/new/', views.new_task, name='new_task'),
    path('task/<int:task_id>/', views.task, name='task'),
    path('del_task/<int:del_task_id>/', views.del_task, name='del_task'),
]
