from django.shortcuts import render
from .serializers import DefectSerializer
from .serializers import LocationSerializer, UserSerializer, GroupSerializer
from .models import Location, Defect
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def locations_list(request):
    if request.method == "GET":
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = LocationSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def location_detail(request, pk):
    try:
        location = Location.objects.get(pk=pk)

    except Location.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = LocationSerializer(location)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def defects_list(request):
    if request.method == "GET":
        defects = Defect.objects.all()
        serializer = DefectSerializer(defects, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DefectSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def defect_detail(request, pk):
    try:
        defect = Defect.objects.get(pk=pk)

    except Defect.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        serializer = DefectSerializer(defect)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = DefectSerializer(defect, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        defect.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class DefectViewSet(viewsets.ModelViewSet):
#     queryset = Defect.objects.all().order_by('creation_date')
#     serializer_class = DefectSerializer
#     permission_classes = [permissions.AllowAny]
#
#     def create(self, request, *args, **kwargs):
#         defect_data = request.data
#         serializer = DefectSerializer(data=defect_data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class LocationViewSet(viewsets.ModelViewSet):
#     search_fields = ['location_name']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Location.objects.all()
#     serializer_class = LocationSerializer
#     permission_classes = [permissions.AllowAny]
#     pagination_class = None
#
#     # def create(self, request, *args, **kwargs):
#     #     location_data = request.data
#     #     serializer = LocationSerializer(data=location_data)
#     #     if serializer.is_valid():
#     #         # print(f"serializer: {serializer.data}")
#     #         serializer.save()
#     #         return Response(status=status.HTTP_201_CREATED)
#     #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
