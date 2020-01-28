from django.contrib import admin
from .models import Service, Order, Account


@admin.register(Service)
class AdminService(admin.ModelAdmin):
    list_display = ["name", "price"]


@admin.register(Order)
class AdminService(admin.ModelAdmin):
    list_display = ["date", "amount"]


@admin.register(Account)
class AdminService(admin.ModelAdmin):
    list_display = ["phone", "photo", "car", "testimonial"]
