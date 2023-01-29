from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    description = models.TextField()
    amount = models.IntegerField()
    is_active = models.BooleanField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name