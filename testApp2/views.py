from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def next_page(request):
    return render(request,'n_page.html')

def insert(request):
    name = request.POST['name']
    ph_no = request.POST['ph']
    password = request.POST['password']
    return render(request,'user_data.html', {'name':name, 'ph_no': ph_no, 'password': password})