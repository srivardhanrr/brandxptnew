from django.contrib import admin

from home.models import Service, ServiceDetail, Project, Contact

admin.site.register(Service)
admin.site.register(ServiceDetail)
admin.site.register(Project)
admin.site.register(Contact)
