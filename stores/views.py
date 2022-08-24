import re
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import pandas as pd

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import StoreSerializer
from .models import Store
from rest_framework.parsers import JSONParser

from users.models import User
from users.serializers import UserSerializer

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

@csrf_exempt
def store_likes(reqeust, id):
    obj = Store.objects.get(id=id)

    if reqeust.method == 'GET':
        serializer = StoreSerializer(obj)
        return JsonResponse(serializer.data['like'], safe=False)

@csrf_exempt
def store_like(request, id, uid):
    obj = Store.objects.get(id=id)

    if request.method == 'POST':
        #user like
        user_obj = User.objects.get(id=uid)
        user_new_data={
            'email': user_obj.email,
            'mucket': user_obj.mucket
        }
        if user_obj.mucket == "":
            user_new_data['mucket'] = str(id)
        else:
            temp = list(map(int, user_obj.mucket.split(',')))
            if id not in temp:
                user_new_data['mucket'] = user_obj.mucket + ','+str(id)
        user_serializer = UserSerializer(user_obj, data=user_new_data)
        if user_serializer.is_valid():
            user_serializer.save()
        # store like 
        new_data ={
            'like' : obj.like
        }
        if obj.like == '"' or obj.like=="":
            new_data['like'] = str(uid)
        else:
            temp = list(map(int, obj.like.split(',')))
            if uid not in temp:
                new_data['like'] = obj.like + ',' + str(uid)
        serializer = StoreSerializer(obj, data=new_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data['like'], safe=False)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # user like 삭제
        user_obj = User.objects.get(id=uid)
        user_new_data={
            'email': user_obj.email,
            'mucket': user_obj.mucket
        }
        if user_obj.mucket != "":
            temp = list(map(int, user_obj.mucket.split(',')))
            if id in temp:
                temp.remove(id)
            user_new_data['mucket'] = ','.join(map(str,temp))
        user_serializer = UserSerializer(user_obj, data=user_new_data)
        if user_serializer.is_valid():
            user_serializer.save()
        # store like 삭제
        if obj.like =="" or obj.like == '"':
            return HttpResponse(status=204)
        new_data ={
            'like' : obj.like
        }
        temp = list(map(int, obj.like.split(',')))
        if uid in temp:
            temp.remove(uid)
            new_data['like'] = ','.join(map(str,temp))
            serializer = StoreSerializer(obj, new_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
        return HttpResponse(status=204)

@csrf_exempt
def store_search(request, keyword):
    if request.method == 'GET':
        criteration1 = Q(address__contains = keyword)
        criteration2 = Q(category__contains = keyword)
        criteration3 = Q(name__contains = keyword)
        queryset = Store.objects.filter(criteration1 | criteration2 | criteration3)
        serializer = StoreSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def store_recommend(request, uid):
    user_obj = User.objects.get(id=uid)
    if request.method == 'GET':
        objs = Store.objects.all()
        innerProductDict = {x.id: x for x in objs}

        store_df = pd.DataFrame({'taste': [obj.taste for obj in objs],
                                 'price': [obj.price for obj in objs],
                                 'atmosphere': [obj.atmosphere for obj in objs],
                                 'service':  [obj.service for obj in objs]},
                                 index=[obj.id for obj in objs])
        user_df = pd.DataFrame(
            [user_obj.taste, user_obj.price, user_obj.atmosphere, user_obj.service],
            index=('taste', 'price', 'atmosphere', 'service'),
            columns=['user']).T

        scored_stores = user_df @ store_df.T
        store_ids = scored_stores.T.sort_values(by='user', ascending=False).index

        serializer = StoreSerializer([innerProductDict[sid] for sid in store_ids], many=True)
        return JsonResponse(serializer.data, safe=False)
        return HttpResponse(stauts=204)
            