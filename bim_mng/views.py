from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from bim_mng.models import Menu

@api_view(['GET'])
def menu_list_view(request):
    param = request.query_params
    print("====request====")
    menu_list = Menu.objects.using('mng_dev').all().values().order_by('parent_cd')
    print("====menu_list====")
    print(menu_list)
    
    # DB 저장 예시
    # new_menu = Menu(name='New Menu')
    # new_menu.save(using='second_db')
    
    return Response(menu_list, status=status.HTTP_200_OK)