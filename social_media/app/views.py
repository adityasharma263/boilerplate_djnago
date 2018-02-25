from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from social_media.constant.response_obj import ReturnObj
from social_media.app.serializer import UserSerializer
from social_media.app.models import User


@api_view(['GET', 'POST'])
@parser_classes((JSONParser,))
def user(request):
    print("yoooooooo")
    if request.method == 'POST':
        try:
            obj = request.data
            serializer = UserSerializer(data=obj)
            if serializer.is_valid():
                serializer.save()
                return_obj = ReturnObj.ret(201)
                return_obj['content']['result']['user'] = serializer.data
                return Response(data=return_obj['content'], status=return_obj['status'])
            else:
                return_obj = ReturnObj().ret(400)
                return_obj['content']['result'] = serializer.errors
                return Response(data=return_obj['content'], status=return_obj['status'])
        except ObjectDoesNotExist:
            return_obj = ReturnObj().ret(404)
            return Response(data=return_obj['content'], status=return_obj['status'])
    elif request.method == 'GET':
        obj = User.objects.all()
        serializer = UserSerializer(obj, many=True)
        return_obj = ReturnObj().ret(200)
        return_obj['content']['result']['user'] = serializer.data
        return Response(data=return_obj['content'], status=return_obj['status'])
