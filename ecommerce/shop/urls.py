from django.urls import path , re_path
from . import views


app_name = 'shop'

urlpatterns = [
    path('', views.index , name = 'index'),
]