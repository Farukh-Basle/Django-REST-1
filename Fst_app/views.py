from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    emp={
        'eno':101,
        'ename':'Rainy',
        'esal': 10000
    }
    response = "<h1>Emp num is {},<br> Emp name is {},<br> Emp sal is {}</h1>".format(emp['eno'],emp['ename'],emp['esal'])
    return HttpResponse(response)

import json
def json_view(request):
    emp={
        "eno":102,
        "ename":'Farukh',
        'esal':10000
    }
    json_response = json.dumps(emp)
    return HttpResponse(json_response, content_type='application/json')

from django.http import JsonResponse
def json_resp(request):
    emp={
        "eno":103,
        "ename":'FB and Rainy got Married',
        'esal':10000
    }

    return JsonResponse(emp)