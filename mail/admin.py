from django.contrib import admin
from .models import User, EmailContent

# Register your models here.


@admin.register(User)
class MailAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "mail_body_field")


@admin.register(EmailContent)
class MailbodyAdmin(admin.ModelAdmin):
    list_display = ("subject", "body")
