from django.urls import path, include, re_path

from bim_mng.views import menu_list_view
app_name = 'bim-mng'

urlpatterns = [
    path('menu-list', menu_list_view),

]