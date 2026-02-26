# Ex.04 Design a Website for Server Side Processing
## Date:26.02.2026

## AIM:
To create a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts.

## FORMULA:
Bill = P + (P * GST / 100)
<br> P --> Price (in Rupees)
<br> GST --> GST (in Percentage)
<br> Bill --> Total Bill Amount (in Rupees)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the total bill amount (including GST).

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
math.html

<html>
    <head>
        <title>
            GST Calculator
        </title>
        <style>
            body
            {
               background-color: rgb(177, 94, 147); 
            }
            .box
            {
               width: 700px;
               height: 400px;
               background-color: rgb(0, 174, 255);
               border:dotted 3px black;
               padding: 8px;
               margin-left: 270px;
               margin-top: 110px;
               position:fixed;
               top: 100px;
               left: 270px; 
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1 align="center" textcolor="orange">GST BILL CALCULATOR</h1>
            <h3 align="center">KAVIDHARSHINI RAMESH (25012397) </h3>
            <h2 align="center">CALCULATION</h2>
            <form method="POST" align="center">
                <label>PRICE:</label>
                <input type="text" name="prize" value="{{ price }}">
                <br>
                <br>
                <label>GST:</label>
                <input type="text" name="gst" value="{{ gst }}">
                <br>
                <br>
                <input type="submit" value="calculate">
                <br>
                <br>
                <label>TOTAL BILL</label>
                <input type="text" name="total_bill" value="{{ total_bill }}">
            </form>
        </div>
    </body>
</html>

views.py

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

url.py

from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.calculate_gst, name='Total')
]


## OUTPUT - SERVER SIDE:
![alt text](<Screenshot 2026-02-26 225508.png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot 2026-02-26 224657.png>)

## RESULT:
The a web page to calculate total bill amount with GST from price and GST percentage using server-side scripts is created successfully.
