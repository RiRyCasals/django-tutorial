from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index1/', views.index1, name='index1'),
    path('<int:id>/<nickname>/', views.index2, name='index2'),
    path('my_name_is_<nickname>.I_am_<int:age>_years_old.', views.index3, name='index3'),
]