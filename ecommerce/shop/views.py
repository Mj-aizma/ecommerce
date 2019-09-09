from django.shortcuts import render
from .models import Object
# Create your views here.

def index(request):
    object = Object.objects.reverse().all()[:4]
    context = {
        'objects' : object,
    }
    return render(request, 'shop/example.html', context)