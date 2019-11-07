from django.shortcuts import render
from django.http import HttpResponse
from . import process

# Create your views here.
def index(request):
    return render(request, 'pages/search.html')
def process_data(request):
    x = request.POST.get("chuoi")
    
    if (x is not None ):
        kq = process.get_request_and_find(x)
        return render(request, 'pages/product.html', kq)

    word_del = request.POST.get("worddel")
    if (word_del is not None): 
        kq = process.get_request_and_delete(word_del)
        return render(request,'pages/product.html')
    word = request.POST.get("wordadd")
    if (word is not None):
        mean = request.POST.get("meaningadd")
        kq = process.get_request_and_add(word,mean)
        return render(request,'pages/product.html')
    return render(request,'pages/product.html')
    
