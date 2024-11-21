from django.db import models

# Create your models here.


class User(models.Model):
    first_name = models.CharField(("first_name"), max_length=254, null=True)
    last_name = models.CharField(("last_name"), max_length=254, null=True)
    email = models.EmailField(("email"), max_length=254, unique=True)

    def __str__(self):
        return self.email


class EmailContent(models.Model):
    subject = models.CharField(max_length=256, null=True)
    body = models.TextField(("body"), null=True)
