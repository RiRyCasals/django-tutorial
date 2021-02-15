from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    params = {
        'title': 'hello/index',
        'msg': 'これはサンプルページです',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'hello/next',
        'msg': 'これはもう1つのページです',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)


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
