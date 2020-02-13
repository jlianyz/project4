from django.db import models
from pyuploadcare.dj.models import ImageField

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return "{} (id: {})".format(self.name, self.id)


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    product_id = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    price = models.IntegerField(blank=False) # cents for stripe to work
    quantity = models.PositiveIntegerField(blank=False, default=0)
    category = models.CharField(
        max_length=100,
        choices=[
            ("Cake pops", "Cake pops"),
            ("Chocolates", "Chocolates"),
            ("Macarons", "Macarons"),
            ("Pastries", "Pastries"),
            ("Cookies", "Cookies"),
            ("Cupcakes", "Cupcakes"),
            ("Tarts", "Tarts"),
        ],
        default="Cake pops"
    )
    tags = models.ManyToManyField("Tag")
    photo = ImageField(null=True)

    def __str__(self):
        return self.name + " : " + self.product_id

    def showPriceInDollars(self):
        return self.price / 100
