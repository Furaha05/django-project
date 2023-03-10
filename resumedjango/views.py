from django.shortcuts import render
def index(request):
    return render(request,'index.html')
def reachus(request):
    return  render(request,'reachus.html')