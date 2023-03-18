from django.db import models

class City(models.Model):
    city = models.CharField('City', max_length=255)


class Product(models.Model):
    product_name = models.CharField('Product Name', max_length=255)
    price = models.FloatField('Price', max_length=255)

class Person(models.Model):
    first_name = models.CharField('Name', max_length=255)
    email = models.CharField('Email', max_length=255)
    products = models.ManyToManyField(Product)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Provider(models.Model):
    provider = models.CharField('Provider Name', max_length=255)
    city = models.OneToOneField(
        City,
        on_delete=models.CASCADE,
        primary_key=True
    )


