from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    name = models.CharField("Название", max_length=250)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"


class Order(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField("дата", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    services = models.ManyToManyField(Service)

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"


class Account(models.Model):
    phone = models.CharField("телефон", max_length=50)
    photo = models.ImageField("Фотография", upload_to="orders/users", default="", blank=True)
    car = models.CharField("Автомобиль", max_length=250)
    testimonial = models.TextField("Отзыв")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Личный кабинет"
        verbose_name_plural = "Личный кабинет"
