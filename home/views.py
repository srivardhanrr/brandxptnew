from django.http import HttpResponse
from django.shortcuts import render
from home.models import Service, Project, Contact, Subscribe


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    context = {'services': services, 'projects': projects}
    return render(request, 'home/index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'centrix/home/project_detail.html', context)


def contact(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(name, email, message)
        Contact.objects.create(name=name, email=email, message=message).save()
        return HttpResponse('Thank you for your message!')
    return render(request, 'home/contact.html')


def service(request):
    services = Service.objects.all().values('title', 'image', 'description')
    context = {'services': services}
    return render(request, 'centrix/home/services.html', context)


def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'centrix/home/projects.html', context)


def subscribe(request):
    if request.POST:
        email = request.POST.get('email')
        Subscribe.objects.create(email=email).save()
        print(email)
        return HttpResponse('Thank you for subscribing!')


