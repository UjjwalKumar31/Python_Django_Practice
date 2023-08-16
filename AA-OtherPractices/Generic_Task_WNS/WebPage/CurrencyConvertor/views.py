from django.shortcuts import render
from .models import Currency
# Create your views here.

def mainpage(request):
    dataset = Currency.objects.all()
    context = {'entries' : dataset}
    for rec in dataset:
        context[rec.Currency_name] = rec.RoE

    return render(request,'CurrConv/mainpage.html', context=context)