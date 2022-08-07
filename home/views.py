from django.http import HttpResponse
from django.shortcuts import render
from .forms import Regisform
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'home/information.html')

def contact(request):
    return render(request, 'home/contact.html')

def error(request, *args, **kwargs):
    return render(request, 'home/error.html')

def register(request):
    form = Regisform()
    if request.method == 'POST':
        form = Regisform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'home/register.html', {'form': form})