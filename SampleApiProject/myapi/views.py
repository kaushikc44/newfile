from django.shortcuts import render
from django.conf import settings
from django.http import Http404
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

# Create your views here.

@api_view(['POST'])
def IdealWeight(heightdata):
    try:
        height = json.loads(heightdata.body)
        weight = str(height*10)

        return JsonResponse("Ideal weight should be:"+weight+"kg",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)