from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField


class Service(models.Model):
    title = models.CharField(max_length=200)
    image = ResizedImageField(force_format="WEBP", quality=75, upload_to="images/services/")
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class ServiceDetail(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)  # Link to Service model
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/service/')
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Optional for author tracking


class Project(models.Model):
    title = models.CharField(max_length=200)
    img = ResizedImageField(force_format="WEBP", quality=75, upload_to="images/projects/")
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
