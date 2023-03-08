from django.contrib import admin

# Register your models here.
from .models import Subject
from .models import Section

admin.site.register(Subject)
admin.site.register(Section)