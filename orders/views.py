from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import Service, Account
from orders.serializers import ServiceSerializer


def index_page(request):
    return render(request, "pages/index_page.html", {'services': Service.objects.all()})


class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


@login_required
def dashboard_user_page(request):
    return render(request, "pages/dashboard_user.html", {'accounts': Account.objects.all()})


@login_required
def order_app(request):
    return render(request, "pages/order_app.html")
