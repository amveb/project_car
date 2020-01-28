from django.shortcuts import render

from orders.models import Service


def orders_page(request):
    return render(request, "pages/order_page.html", {'services': Service.objects.all()})
