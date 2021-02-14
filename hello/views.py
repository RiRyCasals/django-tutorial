from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello django !!")

def index1(request):
    if 'msg' in request.GET:
        msg = request.GET['msg']
        result = 'you typed: "' + msg + '".'
    else:
        result = 'please send msg parameter'
    return HttpResponse(result)

def index2(request, id, nickname):
    result = 'your id: ' + str(id) + ', name: "' + nickname + '".'
    return HttpResponse(result)

def index3(request, nickname, age):
    result = 'your account: "' + nickname + '" (' + str(age) + ').'
    return HttpResponse(result)
