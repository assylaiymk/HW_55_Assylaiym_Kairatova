from django.urls import path
from webapp.views.tasks import add_view, detail_view, update_view, delete_view, confirm_delete
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks/add/', add_view, name='task_add'),
    path('tasks/<int:pk>/update/', update_view, name='task_update'),
    path('tasks/<int:pk>/delete/', delete_view, name='task_delete'),
    path('tasks/<int:pk>/confirm-delete/', confirm_delete, name='confirm_delete'),
    path('tasks/', index_view, name='tasks'),
    path('tasks/<int:pk>', detail_view, name='task_detail')
]
