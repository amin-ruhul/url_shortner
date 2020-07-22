from django.contrib import admin

# Register your models here.

from .models import UrlShortner 

admin.site.register(UrlShortner)