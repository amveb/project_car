from django.db import models


class Service(models.Model):
    name = models.CharField("Название", max_length=250)
    price = models.IntegerField()

    class Meta:
        verbose_name = "Услуги"
        verbose_name_plural = "Услуги"

