import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StoreSerializer
from .models import Store
from rest_framework.parsers import JSONParser

@csrf_exempt
def store_list(request):
    if request.method == 'GET':
        queryset = Store.objects.all()
        serializer = StoreSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def store(request, id):
    obj = Store.objects.get(id=id)

    if request.method == 'GET':
        serializer = StoreSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data  = JSONParser().parse(request)
        serializer = StoreSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)