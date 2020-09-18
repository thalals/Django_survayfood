from django.shortcuts import render, redirect
from . import models
from django.db.models import Sum
# Create your views here.
def list(request):
    lists = models.Food.objects.all()
    sum_price = models.sum.objects.all()

    count = 0
    if request.method == 'POST':
        prices = request.POST.getlist('food[]')
        print("post dat=>>>>>> : ",prices)          #출력확인

        for a in prices:
            count = count + int(a)
        sum_price.sum = count
        print(sum_price.sum)

    return render(request, 'home.html',{'lists': lists, 'sum_price':sum_price})

