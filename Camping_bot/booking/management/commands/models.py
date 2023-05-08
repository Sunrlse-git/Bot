from django.db import models


class Booking(models.Model):
    user_id = models.PositiveIntegerField(verbose_name="Внешний id пользователя")
    date = models.DateField(verbose_name="Дата")

class External_id(models.Model):
    ind_id = models.PositiveIntegerField(verbose_name= "ID пользователя", unique=True)

