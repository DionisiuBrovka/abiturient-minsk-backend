from rest_framework import serializers
from .models import *


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class SpecialtyGroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = SpecialtyGroup
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['id','e_date','title']


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class SpecialtyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = ['id','title','code']


class SpecialtyDetailSerializer(serializers.ModelSerializer):
    
    group = SpecialtyGroupSerializers()
    
    class Meta:
        model = Specialty
        fields = '__all__'


class EstablishmentListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Establishment
        fields = ['id','title','short_title','adress']


class EstablishmentDetailSerializer(serializers.ModelSerializer):    
    
    events = EventListSerializer(many=True, read_only=True)
    gallery = GallerySerializers(many=True, read_only=True)
    specialty = SpecialtyListSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = '__all__'