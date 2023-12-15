from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from pymongo import MongoClient
from bson.json_util import dumps, loads

# Create your views here.
@api_view(['GET'])
def mongo_connection_test_view(request):
    # param = request.query_params
    # print("====request====")
    # print(param)
    # print(param['a'])
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        print(client.list_database_names())
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        return Response('Connection Success', status=status.HTTP_200_OK)   
    except Exception as e:
        print(e)
        print('error')
        return Response("Connection Failed", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def list_database_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        print("====list_database_view====")
        list_database = client.list_database_names()
        return Response(list_database, status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def create_collection_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        db = client['test']
        db.create_collection('test_collection')
        list_collection = db.list_collection_names()
        return Response(list_collection, status=status.HTTP_200_OK) 
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def drop_collection_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        db = client['test']
        db.drop_collection('test_collection')
        list_collection = db.list_collection_names()
        return Response(list_collection, status=status.HTTP_200_OK) 
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def find_one_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 단일 조회
        value = collection.find_one({"key": 3})
        print("====find_one_view====")
        return Response("value: {}".format(value), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def find_all_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 전체 조회
        all = loads(dumps(collection.find({})))
        print("====find_all_view====")
        return Response("all: {}".format(all), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def find_max_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # key 최대값 조회
        max_value = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        print("====find_max_view====")
        return Response("max value: {}".format(max_value), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)    
    

@api_view(['GET'])
def find_min_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # key 최소값 조회
        min_value = loads(dumps(collection.find({}).sort("key", 1).limit(1)))
        print("====find_min_view====")
        return Response("min value: {}".format(min_value), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def insert_one_view(request):
    param = request.query_params
    print("====param====")
    print(param)
    
    form_data = request.data.copy()
    print("====form_data====")
    print(form_data)
    
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        if "key" in param:
            collection.insert_one({"key": param["key"], "label":"Number {}".format(param["key"])})
            max_value_aft = collection.find_one({"key": param["key"]})
        else:
            # 최대값 조회
            max_value = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
            max_key = max_value[0]['key']
            # 단일 insert
            collection.insert_one({"key": max_key+1, "label": "Number {}".format(max_key+1)})
            # insert 이후 최대값
            max_value_aft = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        return Response("insert value: {}".format(max_value_aft), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def update_one_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 최대값 조회
        max_value = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        # 단일 update
        collection.update_one({"key": max_value[0]["key"]}, {"$set": {"label": "Number %s (updated)"%(max_value[0]["key"])}})
        # update 이후 최대값
        max_value_aft = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        return Response("update value: {}".format(max_value_aft), status=status.HTTP_200_OK)
        # 다중 update는 단일 update와 같음
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def delete_one_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 최대값 조회
        max_value = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        # 단일 delete
        collection.delete_one({"key": max_value[0]["key"]})
        # delete 이후 최대값
        max_value_aft = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        return Response("after delete max value: {}".format(max_value_aft), status=status.HTTP_200_OK)
        # 다중 delete는 단일 delete와 같음
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def insert_many_view(request):
    try:
        client = MongoClient('mongodb://root:Bim202309B!m@192.168.40.76:27017')
        # db 연결
        db = client['test']
        # collection 연결
        collection = db['test']
        
        # 최대값 조회
        max_value = loads(dumps(collection.find({}).sort("key",-1).limit(1)))
        # 다중 insert
        insert_list = []
        for i in range(max_value[0]['key'] + 1,max_value[0]["key"] + 8,1):
            insert_data = {"key": i, "label": "Number {}".format(i)}
            print(insert_data)
            insert_list.append(insert_data)
            i+=1
        print("====insert_list====")
        collection.insert_many(insert_list)
        all = loads(dumps(collection.find({})))
        return Response("all: {}".format(all), status=status.HTTP_200_OK)
    except Exception as e:
        print("====error====")
        print(e)
        return Response("fail", status=status.HTTP_400_BAD_REQUEST)
