from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

class Credit_Card_Fraud_Detection(models.Model):

    Fraud_Cases= models.CharField(max_length=300)
    Valid_Transactions= models.CharField(max_length=300)


class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_results(models.Model):

    model_name= models.CharField(max_length=300)
    precision1= models.CharField(max_length=300)
    recall= models.CharField(max_length=300)
    F1_Score= models.CharField(max_length=300)

class detection_ratio(models.Model):
    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



