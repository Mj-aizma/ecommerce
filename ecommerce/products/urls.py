from django.urls import path
from products import views

urlpatterns = [

    path('' , views.ObjectListView.as_view())
]