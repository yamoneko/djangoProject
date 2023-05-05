from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def next_page(request):
    return render(request,'n_page.html')

def add(request):
    name=request.POST('name')
    password = request.POST('password')
    ph_no = request.POST('ph-no')
    return render(request,'n_page.html')
