from django.shortcuts import render , redirect
from .forms import ContactUsForm
from .models import ContactUs
# Create your views here.


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            ContactUs.objects.create(title = form.cleaned_data['title'] , description = form.cleaned_data['description'])
            # ContactUs.objects.create( title=request.POST.get('title') , description=request.POST.get('description') )
            return redirect('/')

    else:
        form = ContactUsForm()
        return render(request , 'shop/contactus.html' , {'form' : form})