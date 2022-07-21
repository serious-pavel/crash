from django.contrib import admin
from .models import Frame

# Register your models here.


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    pass
