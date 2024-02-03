from django.contrib import admin
from .models import ServiceProvider,RequestBox,Booklogs
# Register your models here.
admin.site.register(ServiceProvider)
admin.site.register(RequestBox)
admin.site.register(Booklogs)