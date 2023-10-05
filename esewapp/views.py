from django.shortcuts import render
from .models import Card
# Create your views here.
def home(request):
    return render(request,'home.html')

def card(request):
    cards = Card.objects.all()
    return render(request,'base.html',{'cards':cards})

def product_card(request,id):
    product = Card.objects.get(id=id)
    
    return render(request,'esewa.html',{'product':product})