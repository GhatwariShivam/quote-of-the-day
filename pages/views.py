# from django.http import HttpResponse 
from django.shortcuts import render 
from .models import Quote
# import random 

def home(request):
    quote = Quote.objects.order_by("?").first()
    
    context = {
        "quote": quote,
    }
    
    return render(request, "home.html", context)