from django.urls import path
from .views import home, project_detail, contact, service, project, subscribe

urlpatterns = [
    path('', home, name="home"),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('services/', service, name='services'),
    path('projects/', project, name='projects'),
    path('subscribe/', subscribe, name='subscribe'),

]