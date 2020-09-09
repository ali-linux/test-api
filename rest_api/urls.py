from django.urls import path
from . import views
urlpatterns = [
    path('api/',views.json_example, name= 'json'),
    path('api/list',views.json_list_example, name= 'json-list'),
]
