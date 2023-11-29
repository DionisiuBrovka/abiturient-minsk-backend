from django.contrib import admin
from .models import *

admin.site.site_header = 'Адним панель "Приложения коляг"'

# Register your models here.

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'adress']
    list_display_links = ['id', 'title']

    search_fields = ['title', 'short_title']

@admin.register(SpecialtyGroup)
class SpecialtyGroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'g_type']
    list_display_links = ['id', 'code', 'title']
    list_filter = ['g_type']

    search_fields = ['code', 'title']

@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'skill', 'group']
    list_display_links = ['id', 'code', 'title', 'skill']

    search_fields = ['code', 'title', 'skill']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'c_type']
    list_display_links = ['title', 'c_type']