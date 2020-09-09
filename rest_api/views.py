from django.core.serializers import serialize
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import UpdateModel


def json_example(request):
    obj = UpdateModel.objects.get(id = 1)
    json_data = obj.serialize()
    return HttpResponse(json_data, content_type='application/json')

def json_list_example(request):
    obj = UpdateModel.objects.all()
    json_data = obj.serialize()
    return HttpResponse(json_data, content_type='application/json')
