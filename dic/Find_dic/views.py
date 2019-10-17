from django.shortcuts import render
from django.http import HttpResponse
from . import process

# Create your views here.
def index(request):
    return render(request, 'pages/search.html')
def process_data(request):
    x = request.POST.get("chuoi")
    kq = process.test(x)
    return render(request, 'pages/product.html', kq)