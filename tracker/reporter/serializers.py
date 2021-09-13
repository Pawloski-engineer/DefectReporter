from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Location, Defect


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name',)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['location_id', 'location_name', 'parent_location_id']


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['defect_id', 'defect_name', 'defect_description', 'defect_status', 'defect_location',
                  'defect_respondent', 'creation_date', 'media_files', 'reporter']
