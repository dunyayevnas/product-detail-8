from django.contrib import admin
from pages.models import *
# Register your models here.
@admin.register(InfoModel)
class InfoModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name', 'created_at')
    list_filter = ('name', 'created_at')