from django.shortcuts import render
from .models import DefectSerializer, LocationSerializer, UserSerializer, GroupSerializer
from .models import Location, Defect
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters, status


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all().order_by('creation_date')
    serializer_class = DefectSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        defect_data = request.data
        serializer = DefectSerializer(data=defect_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocationViewSet(viewsets.ModelViewSet):
    search_fields = ['location_name']
    filter_backends = (filters.SearchFilter,)
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = None

    def create(self, request, *args, **kwargs):
        location_data = request.data
        serializer = LocationSerializer(data=location_data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
