from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from assessment.models import TbBimCertificationTest, TbBimCertificationManager, VBaseUser, UploadFileModel

# Create your views here.



@api_view(['GET'])
def test_list_view(request):
    param = request.query_params
    print("====request====")
    manager_list = TbBimCertificationManager.objects.all().values()
    user_list = VBaseUser.objects.all().values()
    print("====manager_list====")
    print(manager_list)
    test_list = TbBimCertificationTest.objects.all().values()
    
    return Response(test_list, status=status.HTTP_200_OK)
    
    
@api_view(['POST'])
def upload_file_view(request):
    data = request.data
    print("====data====")
    print(data)
    file = data.values()
    print("====file====")
    print(file)
    files = request.FILES['files']
    print("====files====")
    print(files)
    if (files):
        upload_file = UploadFileModel(files=files)
        upload_file.save()
    
    return Response("Success", status=status.HTTP_200_OK)