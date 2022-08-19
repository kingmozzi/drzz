import re
import json
import os
import chardet
import pandas as pd
import gensim
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.parsers import JSONParser

from stores.models import Store
from stores.serializers import StoreSerializer
from users.models import User
from users.serializers import UserSerializer

from tqdm import tqdm
from twkorean import TwitterKoreanProcessor

from .review_scorer.review_scorer import Doc2Category

DATA_FOLDER = os.getcwd() + '/reviews/review_scorer/review_scorer/data/'
SENTI_PATH = DATA_FOLDER + 'SentiWord_info.json'
DATA_PATH = DATA_FOLDER + 'data_origin.csv'
# data: pd.DataFrame

# with open(SENTI_PATH, mode='rt', encoding='UTF8') as f:
#     senti = pd.DataFrame.from_dict(json.load(f))

# data = pd.read_csv(DATA_PATH, encoding='UTF8')
# data = data.dropna(axis=0)
# data = data.sample(frac=1).reset_index(drop=True)

# processor = TwitterKoreanProcessor()
# tokenize = processor.tokenize_to_strings
# tokens = [tokenize(_) for _ in tqdm(data.review)]

# rs = Doc2Category(sentences=tokens, senti_dict_path=SENTI_PATH)
# rs.tag(categories={'taste': ['맛', '맛있다', '맛없다'],
#                    'price': ['가격', '싸다', '비싸다', '저렴'],
#                    'service': ['서비스', '친절'],
#                    'atmosphere': ['인테리어', '분위기']},
#        width=4, depth=4)


#rs = gensim.models.Word2Vec.load(os.getcwd()+'/reviews/DrChomp.model')
       

@csrf_exempt
def review_list(request, id):
    if request.method == 'GET':
        queryset = Review.objects.filter(store_id=id)
        serializer = ReviewSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        #give_score(data['content'], data)
        user_update(data['user_id'], data)
        store_update(data['store_id'], data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def review(request, id, rid):
    obj = Review.objects.get(id=rid)

    if request.method == 'GET':
        serializer = ReviewSerializer(obj)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'PUT':
        data  = JSONParser().parse(request)
        serializer = ReviewSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

# 리뷰작성시 리뷰내용을 기반으로 채점
def give_score(review, data):
    tokens = tokenize(str(review))
    scored = rs.score_review(tokenize(review))
    data['taste'] = scored['taste']
    data['price'] = scored['price']
    data['service'] = scored['service']
    data['atmosphere'] = scored['atmosphere']

# 채점된 점수와 자신이 쓴 모든 리뷰를 평균치로 내어 유저 가중치 업데이트
def user_update(uid, data):
    obj = Review.objects.filter(user_id=uid)
    user_obj = User.objects.get(id=uid)
    taste_sum = 0#data['taste']
    price_sum = 0#data['price']
    service_sum = 0#data['service']
    atmosphere_sum = 0#data['atmosphere']
    count = 1

    for x in obj:
        taste_sum += x.taste
        price_sum += x.price
        service_sum += x.service
        atmosphere_sum += x.atmosphere
        count+=1
    taste_sum /= count
    price_sum /= count
    service_sum /= count
    atmosphere_sum /= count
    
    new_data = {
        'email': user_obj.email,
        'taste': taste_sum,
        'price': price_sum,
        'service': service_sum,
        'atmosphere': atmosphere_sum }

    serializer = UserSerializer(user_obj, data=new_data)
    if serializer.is_valid():
        serializer.save()

# 채점된 점수와 가게에 쓰인 몯느 리뷰를 평균치로 내어 가게 가중치 업데이트
def store_update(sid, data):
    obj = Review.objects.filter(store_id = sid)
    store_obj = Store.objects.get(id=sid)
    taste_sum = 0#data['taste']
    price_sum = 0#data['price']
    service_sum = 0#data['service']
    atmosphere_sum = 0#data['atmosphere']
    count = 1

    for x in obj:
        taste_sum += x.taste
        price_sum += x.price
        service_sum += x.service
        atmosphere_sum += x.atmosphere
        count+=1
    taste_sum /= count
    price_sum /= count
    service_sum /= count
    atmosphere_sum /= count

    new_data = {
        'taste': taste_sum,
        'price': price_sum,
        'service': service_sum,
        'atmosphere': atmosphere_sum }

    serializer = StoreSerializer(store_obj, data=new_data)
    if serializer.is_valid():
        serializer.save()
