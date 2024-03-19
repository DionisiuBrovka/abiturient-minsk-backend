from rest_framework import serializers
from data.models import *


class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
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
        fields = ['id','title','code', 'icon']


class SpecialtyDetailSerializer(serializers.ModelSerializer):
    group = SpecialtyGroupSerializers()
    
    class Meta:
        model = Specialty
        fields = '__all__'


class SkillListSerializer(serializers.ModelSerializer):
    specialty = SpecialtyDetailSerializer()

    class Meta:
        model = Skill
        fields = ['id', 'code', 'title', 'specialty', 'svod', 'searchtag']


class SkillDetailSerializer(serializers.ModelSerializer):
    specialty = SpecialtyListSerializer()

    class Meta:
        model = Skill
        fields = '__all__'


class SkillForEstListSerializer(serializers.ModelSerializer):

    skill = SkillListSerializer()

    class Meta:
        model = SkillForEstablishment
        fields = ['id', 'est', 'skill', 's_type']


class SkillForEstDetailSerializer(serializers.ModelSerializer):
    skill = SkillListSerializer(many=True, read_only=True)

    class Meta:
        model = SkillForEstablishment
        fields = '__all__'
        

class EstablishmentListSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Establishment
        fields = ['id','title','short_title','adress', 'icon', 'coords']


class EstablishmentDetailSerializer(serializers.ModelSerializer):    
    events = EventListSerializer(many=True, read_only=True)
    gallery = GallerySerializers(many=True, read_only=True)
    skills = SkillForEstDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Establishment
        fields = '__all__'