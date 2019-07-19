from django.contrib import admin

# Register your models here.
from .models import mission, vision

admin.site.register(mission)
admin.site.register(vision)
