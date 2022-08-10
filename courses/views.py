import re
import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseSerializer
from .models import Course
from users.models import User
from users.serializers import UserSerializer
from rest_framework.parsers import JSONParser

@csrf_exempt
def course_list(request, id):
    if request.method =='GET':
        queryset = Course.objects.filter(user_id=id)
        serializer = CourseSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def course(request, cid, id):
    obj = Course.objects.get(id=cid)

    if request.method == 'GET':
        serializer = CourseSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = CourseSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)


