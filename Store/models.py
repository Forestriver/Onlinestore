import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms


class Profile(models.Model):
    class Meta:
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Customer")
    birthdate = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=30, blank=True)
    notes = models.TextField(blank=True, verbose_name=u"Additional notes")

    def __str__(self):
        return self.user.username

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Order(models.Model):
    class Meta:
        verbose_name_plural = "Orders"
    action_text = models.CharField(max_length=200)
    order_date = models.DateTimeField('Date and time of the order')
    notes = models.TextField(blank=True, verbose_name="Additional information")

    def order_planned(self):
        return self.order_date >= timezone.now('Europe/London') - datetime.timedelta(days=1)

    def __str__(self):
        return self.action_text


# contact form model
