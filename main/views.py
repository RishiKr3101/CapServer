from unicodedata import name
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import SurveyResponse
from .serializers import SurveyResponsesSerializer
from rest_framework.parsers import JSONParser
import json
# Create your views here.

@api_view(['GET','POST'])
def home(request):
    if request.method == "POST":
        data= request.data
        print(data)
        res=SurveyResponse.objects.create(Name="Anonymous", Data=data)
        res.save()
        return (Response('created'))

    return(Response('Home it is'))

@api_view(['GET'])
def response(request):
    responses= SurveyResponse.objects.values()
    if not(responses):
        return Response('Nothing to show')
    responses_api= SurveyResponse.objects.values("Data")
    print(responses_api[0]["Data"])
    count=0
    res=""
    for i in responses_api:
        count=count+1
        if not(count== len(responses_api)):
            res=res+"'"+str(count)+"'"+":"+ str(i["Data"])+","
        else:
            res=res+"'"+str(count)+"'"+":"+ str(i["Data"])
        
    res="{"+res+"}"
    res=res.replace("\'", "\"")
    
    print(res)
    


    
    serializer= SurveyResponsesSerializer(responses_api, many=False)
    return Response(json.loads(res))
        