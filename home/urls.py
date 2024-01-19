from django.urls import path
from .views import home, project_detail, contact, service, project, subscribe, brand_growth, digital_solutions


urlpatterns = [
    path('', home, name="home"),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('services/', service, name='services'),
    path('projects/', project, name='projects'),
    path('subscribe/', subscribe, name='subscribe'),
    path('brand-growth/', brand_growth, name="brand_growth"),
    path('digital_solutions/', digital_solutions, name="digital_solutions"),
]
