from django.shortcuts import render
# from .serializers import DefectSerializer
from .serializers import LocationSerializer, UserSerializer, GroupSerializer
from .models import Location, Defect
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters, status
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def locations_list(request):
    if request.method == "GET":
        locations = Location.objects.all()
        serializer = LocationSerializer(locations, many=True)
        return JsonResponse(serializer.data, safe = False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = LocationSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def location_detail(request, pk):
    try:
        location = Location.objects.get(pk=pk)

    except Location.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = LocationSerializer(location)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = LocationSerializer(location, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        location.delete()
        return HttpResponse(status=204)

#
# @csrf_exempt
# def defects_list(request):
#     if request.method == "GET":
#         defects = Defect.objects.all()
#         serializer = DefectSerializer(defects, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == "POST":
#         data = JSONParser().parse(request)
#         serializer = DefectSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def defect_detail(request, pk):
#     try:
#         defect = Defect.objects.get(pk=pk)
#
#     except Defect.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == "GET":
#         serializer = DefectSerializer(defect)
#         return JsonResponse(serializer.data)
#
#     elif request.method == "PUT":
#         data = JSONParser().parse(request)
#         serializer = DefectSerializer(defect, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == "DELETE":
#         defect.delete()
#         return HttpResponse(status=204)


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
