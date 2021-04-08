import time

from django.shortcuts import render
from django.http import JsonResponse, QueryDict
from rest_framework import viewsets
from .models import Text
import json
import base64
from django.db.models import Q
#from elasticsearch import Elasticsearch
#from drf_haystack.viewsets import HaystackViewSet
from django.views.decorators.http import require_http_methods
from django.core import serializers
import json


# Create your views here.
# 创建viewset
def ret_user(request):
    if request.method == 'GET':
        # db=Text.objects.all()#取出来一个QuerySet
        # db=[i.name for i in db]#遍历QuerySet
        db = Text.objects.all().values()
        db = list(db)

        # json = serializers.serialize("json",Text.objects.all())#使序列化容易vue识别 前端用JSON.parse(response.data.data)
        return JsonResponse({"status": 0, "data": db})
    else:
        return JsonResponse({"status": 1, "data": "need GET method"})


def feature(request):
    try:
        if request.method == "POST":
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            obj_text = Text.objects.filter(Q(content__icontains=data['text'])).values()
            print(obj_text)
            db = list(obj_text)
            print(db)
            # data = json.loads(request.body)
            # put = QueryDict(request.body)
            return JsonResponse({"status": 0, "data": db})
        else:
            return JsonResponse({"status": 1, "data": "error"})
    except Exception as e:
        return JsonResponse({"code": 0, "msg": str(e)})


def GetData(request):
    # 测试用
    # if request.method=="GET":
    #   try:
    #
    #       re=[]
    #       db=Text.objects.all().values()
    #       db=list(db)
    #       print(db)
    #       dsl={
    #           "query":{
    #           'match':{
    #               'content':"学习"
    #           }
    #       }
    #       }
    #       es=Elasticsearch()
    #       result = es.search(index="site",body=dsl)
    #       print(result)
    #       result2=list(result["hits"]["hits"])
    #       i=1
    #       for info in result2:
    #
    #           dic={"id":i,"contents":info["_source"]["content"]}
    #           re.append(dic)
    #           i=i+1
    #       return JsonResponse({"status":0,"data":re})
    #   except Exception as e:
    #       return JsonResponse({"status":1,"data":str(e)})
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            print(data)
            re = []
            dsl = {
                "query": {
                    'match': {
                        'content': data["text"]
                    }
                }
            }
            es = Elasticsearch()
            result = es.search(index="site", body=dsl)
            # print(result)
            result2 = list(result["hits"]["hits"])
            i = 1
            for info in result2:
                dic = {"id": i, "contents": info["_source"]["content"]}
                re.append(dic)
                i = i + 1
            print(re)
            return JsonResponse({"status": 0, "data": re})
        except Exception as e:
            return JsonResponse({"status": 1, "data": str(e)})


def test(request):
    if request.method == "POST":
        imgName = request.POST.get('imgName')
        imgPath = request.POST.get('imgPath')
        ines = imgPath.split('base64,')
        imgData = base64.b64decode(ines[1])
        #L:\django_project\vuedjango
        file_url = 'L:/django_project/vuedjango/input_image/%s %s' % (imgName, '')
        leniyimg = open(file_url, 'wb')
        leniyimg.write(imgData)
        leniyimg.close()
        #print(imgPath)
        print(file_url)
        print(imgName)
        return JsonResponse({"imgName":imgName,"imgPath":imgPath})
    return JsonResponse({"status": 0, "data": 1})
