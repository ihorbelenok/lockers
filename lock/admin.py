from django.contrib import admin
from .models import SchoolClass, Kid, Locker
# Register your models here.
admin.site.register(SchoolClass)
admin.site.register(Kid)
admin.site.register(Locker)