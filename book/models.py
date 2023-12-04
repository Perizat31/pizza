from django.db import models
from django.urls import reverse


# Create your models here.

class menu(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class pizza(models.Model):
    pizzaname=models.CharField(max_length=255)
    pizzaimg=models.ImageField(upload_to="photos/%Y/%m/%d")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    menu=models.ForeignKey("menu",on_delete=models.PROTECT,null=True)
    cost=models.IntegerField(null=True)
    description=models.TextField()
    def __str__(self):
        return self. pizzaname
    def get_absolute_url(self):
        return  reverse ('post',kwargs={'post_id':self.pk})
   

class City(models.Model):
    city=models.CharField(max_length=255)
    def __str__(self):
        return self.city


class Street(models.Model):
    city=models.ForeignKey("City",on_delete=models.PROTECT,null=True)
    street=models.CharField(max_length=255)
    def __str__(self):
        return self.street


class Address(models.Model):
    cityname=models.ForeignKey("City",on_delete=models.PROTECT)
    streetname=models.ForeignKey("Street",on_delete=models.PROTECT)
    housenumber=models.IntegerField()
    flatnumber=models.IntegerField()


class Orderstatus(models.Model):
    orderstatus=models.CharField(max_length=255)

    def __str__(self):
        return self.orderstatus

class Deliveryuser(models.Model):
    deliveryfirstname=models.CharField(max_length=255)
    deliverysurname=models.CharField(max_length=255,null=True)
    telephonenumber=models.IntegerField()
    def __str__(self):
        return self.deliveryfirstname+self.deliverysurname

class CustomerUser(models.Model):
    customfirstname = models.CharField(max_length=255)
    customsurname = models.CharField(max_length=255)
    email = models.EmailField(max_length=70)
    telephonenumber = models.IntegerField()



class Order(models.Model):
    pizza=models.ForeignKey("pizza",on_delete=models.PROTECT)
    countofbook=models.IntegerField()
    toaddress = models.ForeignKey("Address", on_delete=models.PROTECT)
    departuredate=models.DateTimeField()
    arrivaldate=models.DateTimeField()
    orderstatus=models.ForeignKey("Orderstatus",on_delete=models.PROTECT)
    deliveryusers=models.ForeignKey("Deliveryuser",on_delete=models.PROTECT)
    customerusers=models.ForeignKey("Customeruser",on_delete=models.PROTECT)

class Paymentstatus(models.Model):
    paystatus=models.CharField(max_length=255)

class Cardholder(models.Model):
    cardholdername=models.CharField(max_length=255)

class Cardtype(models.Model):
    cardtypename=models.CharField(max_length=255)


class UserCard(models.Model):
    cardholder=models.ForeignKey("Cardholder",on_delete=models.PROTECT)
    cardnumber=models.IntegerField()
    dateissue=models.DateTimeField()
    cardyear=models.IntegerField()
    cvc=models.IntegerField()
    cardtype=models.ForeignKey("Cardtype",on_delete=models.PROTECT)

class Card(models.Model):
    order=models.ForeignKey("Order",on_delete=models.PROTECT)
    paymentstatus=models.ForeignKey("Paymentstatus",on_delete=models.PROTECT)
    card=models.ForeignKey("UserCard",on_delete=models.PROTECT)