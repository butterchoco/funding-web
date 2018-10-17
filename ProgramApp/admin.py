from django.contrib import admin
from .models import program_registration, program_update

# Register your models here.
admin.site.register(program_registration)
admin.site.register(program_update)