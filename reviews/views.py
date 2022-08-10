import re
import json
import os
import chardet
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.parsers import JSONParser

from tqdm import tqdm
from twkorean import TwitterKoreanProcessor

from .review_scorer.review_scorer import ReviewScorer

DATA_FOLDER = os.getcwd() + '/review_scorer/data/'
SENTI_PATH = DATA_FOLDER + 'SentiWord_info.json'


@csrf_exempt
def review_list(request, id):
    if request.method == 'GET':
        queryset = Review.objects.filter(store_id=id)
        serializer = ReviewSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ReviewSerializer(data=data)
        #give_score(data['contents'])
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


def give_score(review):
    processor = TwitterKoreanProcessor()
    tokenize = processor.tokenize_to_strings
    tokens = tokenize(review)
    rs = ReviewScorer(sentences=tokens, senti_dict_path=SENTI_PATH)
    rs.tag(categories={'taste': ['맛', '맛있다', '맛없다'],
                   'price': ['가격', '싸다', '비싸다', '저렴'],
                   'service': ['서비스', '친절', '싸가지'],
                   'atmosphere': ['인테리어', '분위기']}, topn=500)
    print(review)
    print(rs.score_review(tokenize(review)))
