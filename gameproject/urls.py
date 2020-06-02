from django.urls import path
from . import views

urlpatterns = [
    path('all_projects/', views.all_projects, name='all_projects'),
    path('project_detail/<project_id>/',
         views.project_detail,
         name='project_detail'),
    path('add_project', views.add_project, name='add_project'),
    path('edit_project/<int:game_project_id>/',
         views.edit_project,
         name='edit_project'),
    path('delete_project/<int:project_id>/',
         views.delete_project,
         name='delete_project'),
]
