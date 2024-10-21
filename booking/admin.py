from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Artist, Studio, StudioBooking

# Register your models here.

admin.site.register(Artist)
admin.site.register(Studio)
admin.site.register(StudioBooking)