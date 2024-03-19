from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from data.models import *

from .serializers import *

# ------------------------------------------------------
class EstablishmentViewSet(ReadOnlyModelViewSet):
    queryset = Establishment.objects.all()
    serializer_class = EstablishmentSerializer


class EventViewSet(ReadOnlyModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class GalleryViewSet(ReadOnlyModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer


class SpecialtyGroupViewSet(ReadOnlyModelViewSet):
    queryset = SpecialtyGroup.objects.all()
    serializer_class = SpecialtyGroupSerializer


class SpecialtyViewSet(ReadOnlyModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer


class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class SkillForEstablishmentViewSet(ReadOnlyModelViewSet):
    queryset = SkillForEstablishment.objects.all()
    serializer_class = SkillForEstablishmentSerializer


class FAQViewSet(ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer