from django.urls import path
from . import views

urlpatterns = [
    path('all_projects/', views.all_projects, name='all_projects'),
    path('project_detail/<project_id>/', views.project_detail, name='project_detail'),
]
