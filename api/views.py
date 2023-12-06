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
            'admin':'http://127.0.0.1:8000/admin/',
            'api':'http://127.0.0.1:8000/api/v1/'
        }
        return Response(data)

class RootView(ViewSet):
    def list(self, request):
        data = {
            'establishments':reverse('establishments-list',request=request)
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


class SpecialityDetailView(ViewSet):
    def list(self, request, pk=1):
        queryset = Specialty.objects.get(id=pk)
        serializer = SpecialtyDetailSerializer(queryset)
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