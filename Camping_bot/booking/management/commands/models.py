from django.db import models


class Booking(models.Model):
    user_id = models.PositiveIntegerField(verbose_name="Внешний id пользователя")
    date = models.DateField(verbose_name="Дата")
    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирование'

class External_id(models.Model):
    ind_id = models.PositiveIntegerField(verbose_name= "ID пользователя", unique=True)

class Message(models.Model):
    m = models.TextField(verbose_name="Введите сообщение для публикации в боте")
    class Meta:
        verbose_name = 'Рассылка сообщения'
        verbose_name_plural = 'Рассылка сообщения'
