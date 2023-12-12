from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from pymongo import MongoClient
from bson.json_util import dumps, loads
from assessment.models import TbBimCertificationTest, TbBimCertificationManager, VBaseUser

# Create your views here.
@api_view(['GET'])
def mongoclient_view(request):
    param = request.query_params
    print("====request====")
    print(param)
    print(param['a'])


    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        print(client.list_database_names())
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 단일 조회
        key = collection.find_one({"key": 3})
        print(key)
        # 전체 조회
        all = collection.find({})
        print(list(all))
        # key 최대값 조회
        max_value = loads(dumps(collection.find({}).sort({"key":-1}).limit(1)))
        print("====max====")
        print(type(max_value))
        print(max_value)

        # key 최소값 조회
        min_value = loads(dumps(collection.find({}).sort({"key": 1}).limit(1)))
        print("====min====")
        print(min_value)

        # 단일 insert
        # collection.insert_one({"key": 12, "label": "Number 12"})
        
        # 다중 insert
        # insert_list = []
        # for i in range(max_value[0]['key'] + 1,max_value[0]["key"] + 8,1):
        #     insert_data = {"key": i, "label": "Number %s" %(i)}
        #     print(insert_data)
        #     insert_list.append(insert_data)
        #     i+=1
        # print("====insert_list====")
        # print(insert_list)

        # insert_response = collection.insert_many(insert_list)
        # print('====insert_response====')
        # print(insert_response)
        
        # 단일 delete
        # delete_one_response = collection.delete_one({"key": max_value[0]["key"]})
        # print("====delete_one_response====")
        # print(delete_one_response)
        # 다중 delete는 단일 delete와 같음
        
        # 단일 update
        # update_one_response = collection.update_one({"key": max_value[0]["key"]}, {"$set": {"label": "Number %s (updated)"%(max_value[0]["key"])}})
        # print("====update_one_response====")
        # print(update_one_response)
        # 다중 update는 단일 update와 같음
        
        return Response('Success', status=status.HTTP_200_OK)   
    except:
        print('error')
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)


    # print('data: '+ data)
    
@api_view(['GET'])
def djongo_view(request):
    param = request.query_params
    print("====request====")
    # print(param)
    # print(param['a'])
    
    # MongoDB 데이터 read
    try:
        
    # # MongoDB 데이터 create
    # new_data = MongoModel(name= 'KIM', age= 29)
    
        return Response("Success", status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response("Error", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def mssql_view(request):
    param = request.query_params
    print("====request====")
    manager_list = TbBimCertificationManager.objects.all().values()
    user_list = VBaseUser.objects.all().values()
    print("====manager_list====")
    print(manager_list)
    
    return Response(user_list, status=status.HTTP_200_OK)
    