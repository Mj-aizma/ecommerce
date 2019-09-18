from django.shortcuts import render
from shop.models import Object
from django.views import generic
# Create your views here.

class ObjectDetailView(generic.DetailView):
    model = Object

    template_name = 'shop/product_detail.html'
