from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
	path('', views.projects, name = 'projects'),
	path('single-project/<str:pk>', views.project, name = 'single-project'),
	path('update-project/<str:pk>', views.updateProject, name = 'update-project'),
	path('create-project/', views.createProject, name = 'create-project'),
	path('delete-project/<str:pk>', views.deleteProject, name = 'delete-project'),
]
	# path('project-form/', views.createProject),
