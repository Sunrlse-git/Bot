from django.db import models

# Create your models here.
class Message(models.Model):
    m = models.TextField(verbose_name="Поле для ввода текста")