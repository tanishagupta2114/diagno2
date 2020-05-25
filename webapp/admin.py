
from django.contrib import admin
from .models import data1, merge
from webapp.models import patient

admin.site.register(data1)
admin.site.register(patient)
admin.site.register(merge)
