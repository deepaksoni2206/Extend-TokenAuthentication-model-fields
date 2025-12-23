from django.db import models
from rest_framework.authtoken.models import Token as DefaultToken

class CustomToken(DefaultToken):
    origin = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Custom Token'
