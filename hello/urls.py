# from django.urls import path
from django.conf.urls import url
from .views import HelloView

urlpatterns = [
    url(r'', HelloView.as_view(), name='index'),
]