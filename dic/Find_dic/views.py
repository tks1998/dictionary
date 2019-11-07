from django.shortcuts import render
from django.http import HttpResponse
from . import process

# Create your views here.
def index(request):
    return render(request, 'pages/search.html')
def process_data(request):
    x = request.POST.get("chuoi")
    if (x!=""):
        kq = process.get_request_and_find(x)
        return render(request, 'pages/product.html', kq)
    
    word_del = request.POST.get("worddel")
    print(word_del)
    if (word_del!=""):
        print(word_del)
        kq = process.get_request_and_delete(word_del)
        return render(request,'pages/product.html')
    return render(request,'pages/product.html')