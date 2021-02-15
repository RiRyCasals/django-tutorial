from django.shortcuts import render
from django.http import HttpResponse
from .forms import HelloForm
from django.views.generic import TemplateView

class HelloView(TemplateView):
    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data:',
            'form': HelloForm(),
        }
        
    def get(self, request):
        return render(request, 'hello/index.html', self.params)

    def post(self, request):
        msg = 'あなたは、<b>' + request.POST['name'] + '</b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + '</b>ですね。'
        self.params['message'] = msg
        self.params['form'] = HelloForm(request.POST)
        return render(request, 'hello/index.html', self.params)