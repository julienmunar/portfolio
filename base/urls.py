from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.homePage, name='home'),
    path('project/<str:pk>', views.project, name='project'),
    path('addproject', views.addProject, name='addProject'),
    path('editproject/<str:pk>', views.editProject, name='editProject'),
    path('deleteproject/<str:pk>', views.deleteProject, name='deleteProject'),
]