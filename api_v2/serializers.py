from rest_framework import serializers
from data.models import *


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
 
 
class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = '__all__'


class SpecialtyGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialtyGroup
        fields = '__all__'


class SpecialtySerializer(serializers.ModelSerializer):

    group = SpecialtyGroupSerializer()

    class Meta:
        model = Specialty
        fields = '__all__'


class SkillSerializer(serializers.ModelSerializer):

    specialty = SpecialtySerializer() 

    class Meta:
        model = Skill
        fields = '__all__'


class SkillForEstablishmentSerializer(serializers.ModelSerializer):

    skill = SkillSerializer(many = True)

    class Meta:
        model = SkillForEstablishment
        fields = '__all__'


class EstablishmentSerializer(serializers.ModelSerializer):

    events = EventSerializer(many = True)
    gallery = GallerySerializer(many = True)
    skills = SkillForEstablishmentSerializer(many = True)

    class Meta:
        model = Establishment
        fields = '__all__'


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'