from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
router.register(r'establishment', EstablishmentViewSet)
router.register(r'event', EventViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'specialty-group', SpecialtyGroupViewSet)
router.register(r'specialty', SpecialtyViewSet)
router.register(r'skill', SkillViewSet)
router.register(r'skill-for-establishment', SkillForEstablishmentViewSet)
router.register(r'faq', FAQViewSet)
urlpatterns = router.urls
