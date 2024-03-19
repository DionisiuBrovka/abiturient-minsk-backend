from django.contrib import admin
from .models import *

admin.site.site_header = '"Абитуриент" v.0.0.1a'

# Register your models here.
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['id','q']
    list_display_links = ['id','q']

class ActualSkillListFilter(admin.SimpleListFilter):
    title = "Связаные"
    parameter_name = "linked"

    def lookups(self, request, model_admin):

        return [
            ("Y", 'Да'),
            ("N", 'Нет'),
        ]
    
    def queryset(self, request, queryset):

        if self.value() == "Y":
            return queryset.exclude(svod__isnull=True)
        if self.value() == "N":
            return queryset


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'specialty']
    list_display_links = ['id', 'code', 'title']
    search_fields = ['code', 'title']

    list_filter = ['specialty__c_type', ActualSkillListFilter ,'svod__est']


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 0


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'title', 'group', 'c_type']
    list_display_links = ['id', 'code', 'title']
    search_fields = ['code', 'title']

    list_filter = ['c_type']

    inlines = [SkillInline]


class SpecialtyInline(admin.TabularInline):
    model = Specialty
    extra = 0


@admin.register(SpecialtyGroup)
class SpecialtyGroupAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    list_display_links = ['id','title']
    

    inlines = [SpecialtyInline]

class EventInline(admin.TabularInline):
    model = Event
    extra = 0


class GalleryInline(admin.TabularInline):
    model = Gallery
    extra = 0


@admin.register(SkillForEstablishment)
class SkillForEstablishmentAdmin(admin.ModelAdmin):
    list_display = ['id','est', 's_type']
    list_display_links = ['id', 'est']

    fieldsets = [
        (
            "Основное", {
                "fields" : ["est", "skill", "s_type", "rule"]
            }
        ),
        (
            "Бюджет", {
                "fields" : ["b_count", "b_long", "b_avd"]
            }
        ),
        (
            "Платка", {
                "fields" : ["p_count", "p_long", "p_avd"]
            }
        ),
        (
            "ОПФР", {
                "fields" : ["is_opfr", "opfr_qnic"]
            }
        ),
    ]

class SkillForEstablishmentInline(admin.StackedInline):
    model = SkillForEstablishment
    extra = 0

@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ['id','short_title', 'title', 'adress', "wsite"]
    list_display_links = ['id','short_title', 'title']

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
                "fields" : ["tel","email","wsite","wtel","wvk","winsta","wface","wtwit","wtic","wother"]
            }
        ),
        
    ]

    inlines = [GalleryInline, EventInline, SkillForEstablishmentInline]

    search_fields = ['title', 'short_title']

# @admin.register(Event)
# class EventAdmin(admin.ModelAdmin):
#     list_display = ['id','title', 'e_date', 'org']
#     list_display_links = ['id','title', 'e_date']
#     search_fields = ['title', 'org']

# @admin.register(Gallery)
# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ['id','est','photo']
#     list_display_links = ['id','est']

# @admin.register(Specialty)
# class SpecialtyAdmin(admin.ModelAdmin):
#     list_display = ['id', 'code', 'title', 'skill', 'group']
#     list_display_links = ['id', 'code', 'title', 'skill']
#     search_fields = ['code', 'title', 'skill']







