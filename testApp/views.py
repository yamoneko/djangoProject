from django.shortcuts import render,redirect
from  django.http import  HttpResponse

def home(request):
   return render(request,'home.html')

data = []
def add(request):
    d_list = request.POST['list']
    #data = ['Sleeping','Reading','Walking','Travelling','Sport']
    if len(data)-1 < 3:
        d_list=request.POST['list']
        data.append(d_list)
        return redirect('/test')
    else:
        # my_data =[]
        # for i in range(len(data)):
        #     my_data.append(data[i])
        # data= []
        return render(request,'do_list.html',{'list':data})
