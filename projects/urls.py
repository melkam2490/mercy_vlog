from django.urls import path
from . import views
urlpatterns = [
    path('', views.projects, name="projects"),

    path('project/<uuid:pk>/', views.project, name='project'),
    path('creat_project/', views.CreatProject, name="create-project"),
    path('update-project/<uuid:pk>/', views.UpdateProject, name="update-project"),
    path('delete-project/<uuid:pk>/', views.deleteProject, name="delete-project"),
]
