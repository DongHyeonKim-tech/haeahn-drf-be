from django.urls import path, include, re_path

from level_measurement.views import *

app_name = 'level-measurement'


urlpatterns = [
    path('mongo-connection-test-view', mongo_connection_test_view),
    path('list-database-view', list_database_view),
    path('create-collection-view', create_collection_view),
    path('drop-collection-view', drop_collection_view),
    path('find-one-view', find_one_view),
    path('find-all-view', find_all_view),
    path('find-max-view', find_max_view),
    path('find-min-view', find_min_view),
    path('insert-one-view', insert_one_view),
    path('update-one-view', update_one_view),
    path('delete-one-view', delete_one_view),
    path('insert-many-view', insert_many_view),
]