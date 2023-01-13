from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL


GENDER = (
    ("MALE", "MALE"),
    ("FEMALE", "FEMALE"),
    ("OTHER", "OTHER")
)
TYPEACCOUNT = (
    ("SAVINGS" , "SAVINGS ACCOUNT"),
    ("CURRENT","CURRENT ACCOUNT")
)
DISTRICT = (
    ("KOZHIKODE", "KOZHIKODE"),
    ("ALAPUZHA", "ALAPUZHA"),
    ("MALAPPURAM", "MALAPPURAM"),
    ("TRISUR", "TRISUR")
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    dob = models.DateTimeField( blank=True, null=True)
    age= models.IntegerField(blank=True, null=True)
    phone= models.IntegerField(blank=True, null=True)
    email = models.EmailField(max_length=200, blank=True, null=True)
    address=models.CharField(max_length=200, blank=True, null=True)
    district =models.CharField(max_length=20,choices=DISTRICT)
    # branch=models.CharField(max_length=20,choices=BRANCH)
    gender =models.CharField(max_length=20,choices=GENDER)
    account_type =models.CharField(max_length=20,choices=TYPEACCOUNT)
    debitcard=models.BooleanField(default=False)
    creditcard=models.BooleanField(default=False)
    passbook=models.BooleanField(default=False)
    
    


    def __str__(self):
        return str(self.user)