from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from allauth.account.forms import LoginForm

from orders.models import Service
from orders.serializers import ServiceSerializer


def services_page(request):
    return render(request, "pages/service_page.html", {'services': Service.objects.all()})


def account_page(request):
    return render(request, "pages/account_page.html")


class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


