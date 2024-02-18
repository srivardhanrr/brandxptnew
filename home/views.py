import threading

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string

from brandxpt import settings
from home.models import Service, Project, Contact, Subscribe


def home(request):
    services = Service.objects.all()
    projects = Project.objects.all()
    context = {'services': services, 'projects': projects}
    return render(request, 'home/index.html', context)


def brand_growth(request):
    return render(request, 'home/brand_growth.html')


def digital_solutions(request):
    return render(request, 'home/digital_solutions.html')


def ecommerce_support(request):
    return render(request, 'home/ecommerce_support.html')


def about_us(request):
    return render(request, 'home/about.html')


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {'project': project}
    return render(request, 'centrix/home/project_detail.html', context)


def contact(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        email_subject = f'New contact: {email}: {name}'
        email_message = f'Name: {name} \nMessage: {message}'
        EmailThread(email_subject, email_message, ["srivardhan.singh.rathore@gmail.com"]).start()
        print(name, email, message)
        Contact.objects.create(name=name, email=email, message=message).save()
        return HttpResponse('Thank you for your message!')
    return render(request, 'home/contact.html')


def service(request):
    services = Service.objects.all()
    context = {'services': services}
    return render(request, 'home/services.html', context)


def project(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'home/projects.html', context)


def subscribe(request):
    if request.POST:
        email = request.POST.get('email')

        context = {
            "email": email,
        }

        plain_message = "Welcome to our Newsletter!"
        html_message = render_to_string('emails/subscribe.html', context)

        email = EmailMultiAlternatives("Welcome to our Newsletter", plain_message, from_email=settings.EMAIL_HOST_USER, to=[email])
        email.attach_alternative(html_message, "text/html")
        email.send()

        # Subscribe.objects.create(email=email).save()
        # EmailThread('New subscriber', f'New subscriber: {email}', ["srivardhan588@gmail.com",]).start()
        return HttpResponse('Thank you for subscribing!')


class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list, html_message=None):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        message = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER,
                               self.recipient_list)
        message.content_subtype = "html"
        message.send(fail_silently=False)
        print(message.to)
        print(message.from_email)
