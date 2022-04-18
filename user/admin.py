from django.contrib import admin
from .models import Profile

admin.site.site_header="TPL Data Analytics Dashboard"

# Register your models here.
admin.site.register(Profile),