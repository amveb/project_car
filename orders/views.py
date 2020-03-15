from django.shortcuts import render
from orders.models import Service

def services_page(request):
    return render(request, "pages/service_page.html", {'services': Service.objects.all()})


def account_page(request):
    return render(request, "pages/account_page.html")
