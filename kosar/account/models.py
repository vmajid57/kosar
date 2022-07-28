from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


# Create your models here.
class CustomUser(AbstractUser):
    age = models.IntegerField(null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits"
                                         " allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True, default=None, null=False)


class Loan(models.Model):
    # customUser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    amount = models.IntegerField()
    created_at = models.DateTimeField(default=None)
    end_at = models.DateTimeField(default=None)
    numberOf = models.DateTimeField(default=30)
