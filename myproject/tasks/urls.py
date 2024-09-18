from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # 編集ページへのURL
    path('toggle/<int:task_id>/', views.toggle_task_status, name='toggle_task_status'),  # 完了状態を切り替えるURL
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # タスク削除URL
]
