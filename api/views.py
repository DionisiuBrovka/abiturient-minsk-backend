from django.shortcuts import render
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from .models import *
from .serializers import *

# Create your views here.
class MainView(ViewSet):
    def list(self, request):
        data = {
            'api':reverse('api-v1',request=request),
        }
        return Response(data)

class RootView(ViewSet):
    def list(self, request):
        data = {
            'establishments':reverse('establishments',request=request),
            'specialitys':reverse('specialitys',request=request),
            'specialitys-sso':reverse('specialitys-sso',request=request),
            'specialitys-pto':reverse('specialitys-pto',request=request),
            'specialitys-est':reverse('specialitys-est', args=[1] ,request=request),
            'skills':reverse('skills',request=request),
            'skills-linked':reverse('skills-linked',request=request),
            'skills-sso':reverse('skills-sso',request=request),
            'skills-pto':reverse('skills-pto',request=request),
            'skills-linked-sso':reverse('skills-linked-sso',request=request),
            'skills-linked-pto':reverse('skills-linked-pto',request=request),
            'skill-est':reverse('skill-est',request=request),
            'events':reverse('events',request=request),
            'faq':reverse('faq',request=request),
        }
        return Response(data)


class EstablismentListView(ViewSet):
    def list(self, request):
        queryset = Establishment.objects.all()
        serializer = EstablishmentListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class EstablismentDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = Establishment.objects.get(id=pk)
        serializer = EstablishmentDetailSerializer(queryset)
        return Response(serializer.data)


class SpecialityListView(ViewSet):
    def list(self, request):
        queryset = Specialty.objects.all()
        serializer = SpecialtyListSerializer(queryset, many=True)
        return Response(serializer.data)


class SpecialitySSOListView(ViewSet):
    def list(self, request):
        queryset = Specialty.objects.filter(c_type="ССО")
        serializer = SpecialtyListSerializer(queryset, many=True)
        return Response(serializer.data)


class SpecialityPTOListView(ViewSet):
    def list(self, request):
        queryset = Specialty.objects.filter(c_type="ПТО")
        serializer = SpecialtyListSerializer(queryset, many=True)
        return Response(serializer.data)


class SpecialityESTListView(ViewSet):
    def list(self, request, pk=1):
        queryset = Establishment.objects.filter(skills=pk)
        serializer = EstablishmentListSerializer(queryset, many=True)
        return Response(serializer.data)


class SpecialityDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = Specialty.objects.get(id=pk)
        serializer = SpecialtyDetailSerializer(queryset)
        return Response(serializer.data)


class SkillListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.all()
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)


class SkillLinkedListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.exclude(svod__isnull=True)
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)


class SkillSSOListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.filter(specialty__c_type="ССО")
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SkillPTOListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.filter(specialty__c_type="ПТО")
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)


class SkillLinkedSSOListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.exclude(svod__isnull=True).filter(specialty__c_type="ССО")
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)


class SkillLinkedPTOListView(ViewSet):
    def list(self, request):
        queryset = Skill.objects.exclude(svod__isnull=True).filter(specialty__c_type="ПТО")
        serializer = SkillListSerializer(queryset, many=True)
        return Response(serializer.data)



class SkillDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = Skill.objects.get(id=pk)
        serializer = SkillDetailSerializer(queryset)
        return Response(serializer.data)


class SkillESTListView(ViewSet):
    def list(self, request, pk=1):
        queryset = Establishment.objects.filter(skills__skill=pk)
        serializer = EstablishmentListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SkillForEstListView(ViewSet):
    def list(self, request, pk=1):
        queryset = SkillForEstablishment.objects.all()
        serializer = SkillForEstListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class SkillForEstDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = SkillForEstablishment.objects.get(id=pk)
        serializer = SkillForEstDetailSerializer(queryset)
        return Response(serializer.data)


class EventsListView(ViewSet):
    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventListSerializer(queryset, many=True)
        return Response(serializer.data)
    

class EventsDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = Event.objects.get(id=pk)
        serializer = EventDetailSerializer(queryset)
        return Response(serializer.data)


class FAQListView(ViewSet):
    def list(self, request):
        queryset = FAQ.objects.all()
        serializer = FAQSerializer(queryset, many=True)
        return Response(serializer.data)