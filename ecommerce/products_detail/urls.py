from django.urls import path ,re_path
from products_detail import views

urlpatterns = [

    re_path(r'^(?P<pk>\d+)$', views.ObjectDetailView.as_view())
]