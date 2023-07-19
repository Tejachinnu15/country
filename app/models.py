from django.db import models

# Create your models here.
class Country(models.Model):
    COUNTRY_ID=models.IntegerField(max_length=100,primary_key=True)
    COUNTRY_NAME=models.CharField(max_length=100)
class Capital(models.Model):
    CAPITAL_ID=models.IntegerField(max_length=100,primary_key=True)
    CAPITAL_NAME=models.CharField(max_length=100)
    CAPITAL_ID=models.ForeignKey(Country,on_delete=models.CASCADE)