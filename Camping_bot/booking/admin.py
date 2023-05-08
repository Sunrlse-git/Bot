from django.contrib import admin
from telebot import telebot

import Camping_bot
from booking.management.commands.models import Booking
from .models import Message
# from .views import bot_mailing


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'date')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('m',)

