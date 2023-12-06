from django.contrib import admin
from .models import *

admin.site.site_header = '"Абитуриент" v.0.0.1a'

# Register your models here.

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'adress']
    list_display_links = ['id', 'title']

    fieldsets = [
        (
            "Блок (Название)", {
                "fields" : ["title", "short_title"]
            }
        ),
        (
            "Блок (Местоположение)", {
                "fields" : ["adress","coords"]
            }
        ),
        (
            "Блок (Описание)", {
                "fields" : ["desc","icon","prev","promo_medio"]
            }
        ),
        (
            "Блок (Контакты)", {
                "fields" : ["tel","mail","email","wsite","wtel","wvk","winsta","wother"]
            }
        ),
        (
            "Блок (Специальности)", {
                "fields" : ["specialty"]
            }
        ),
        
    ]

    search_fields = ['title', 'short_title']


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'skill', 'group']
    list_display_links = ['id', 'code', 'title', 'skill']

    search_fields = ['code', 'title', 'skill']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'e_date']
    list_display_links = ['id','title', 'e_date']

    search_fields = ['title']


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','est','photo']
    list_display_links = ['id','est']

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id','q']
    list_display_links = ['id','q']

@admin.register(SpecialtyGroup)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['id','title']

