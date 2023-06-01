from django.http import Http404
from django.shortcuts import render
from rest_framework.decorators import api_view
from .ModelSerializer import formSerialzer
from rest_framework.response import Response
from .models import RegisteredUser
from re import compile


def isValidNumber(number):
    ptrn = compile(r'^(\+91|\+91\-|0)?[6789]\d{9}$')
    res = ptrn.match(number)
    if not res:
        return False
    return True


@api_view(["POST", "GET"])
def saveData(request):
    if request.method == "POST":
        try:
            formData = request.data
            number = request.data['contact']
            if not isValidNumber(number):
                raise Exception("Invalid Number")
            serData = formSerialzer(data = formData)
            if serData.is_valid():
                serData.save()
            else:
                return Response(serData.errors)
            return Response(serData.data)
        except Exception as e:
            if str(e) == 'Invalid Number':
                raise Http404("Invalid Number")
            else:
                return Response({"error":str(e)})
        
    if request.method == "GET":
        try:
            dataObj = RegisteredUser.objects.all()
            serData = formSerialzer(dataObj, many=True)
            return Response(serData.data)
        except Exception as e:
            return Response({"Error":str(e)})
