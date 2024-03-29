from django.urls import path
from .views import home, project_detail, contact, service, project, subscribe, brand_growth, digital_solutions, ecommerce_support, about_us

urlpatterns = [
    path('', home, name="home"),
    path('project/<int:pk>/', project_detail, name='project_detail'),
    path('contact/', contact, name='contact'),
    path('about_us/', about_us, name='about_us'),
    path('services/', service, name='services'),
    path('projects/', project, name='projects'),
    path('subscribe/', subscribe, name='subscribe'),
    path('brand-growth/', brand_growth, name="brand_growth"),
    path('digital_solutions/', digital_solutions, name="digital_solutions"),
    path('ecommerce_support/', ecommerce_support, name="ecommerce_support"),
]
