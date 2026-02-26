from django.shortcuts import render
def calculate_gst(request):
    price=int(request.POST.get('price','0'))
    gst=int(request.POST.get('gst','0'))
    total_bill=price+(price*gst/100) if request.method=='POST'else 0
    print("Price=",price)
    print("GST=",gst)
    print("Total Bill=",total_bill)
    return render(request,'mathapp/math.html',{'Price':price,'GST':gst,'Total Bill':total_bill})

    urls.py

    from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_gst, name='Total')
]