from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

from django_countries.fields import CountryField

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True)
    country = CountryField(blank_label="(select country)")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('users_view', args=[self.id])
