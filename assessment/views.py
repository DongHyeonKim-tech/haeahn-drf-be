from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from pymongo import MongoClient
from bson.json_util import dumps, loads
from assessment.models import TbBimCertificationTest, TbBimCertificationManager, VBaseUser

# Create your views here.



@api_view(['GET'])
def mssql_view(request):
    param = request.query_params
    print("====request====")
    manager_list = TbBimCertificationManager.objects.all().values()
    user_list = VBaseUser.objects.all().values()
    print("====manager_list====")
    print(manager_list)
    test_list = TbBimCertificationTest.objects.all().values()
    
    # return Response("Success")
    return Response(test_list, status=status.HTTP_200_OK)
    