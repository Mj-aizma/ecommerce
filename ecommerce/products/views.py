from django.shortcuts import render
from shop.models import Object
from django.views import generic
# Create your views here.

class ObjectListView(generic.ListView):
    model = Object
    paginate_by = 16
    template_name = 'shop/product.html'
