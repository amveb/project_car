from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from orders.models import Service
from orders.serializers import ServiceSerializer


def services_page(request):
    return render(request, "pages/service_page.html", {'services': Service.objects.all()})



class ServiceView(ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

@login_required
def dashboard_user_page(request):
    return render(request, "pages/dashboard_user.html")
