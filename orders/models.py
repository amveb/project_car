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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    service = models.ManyToManyField(Service, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Заказы"
        verbose_name_plural = "Заказы"


class UserCar(models.Model):
    phone = models.IntegerField()
    photo = models.ImageField("Фотография", upload_to="orders/users", default="", blank=True)
    orders = models.OneToOneField(Order, on_delete=models.CASCADE, null=True)



