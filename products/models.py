from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE


class Menu(models.Model):

    """Menu Model Definition"""

    name = models.CharField(max_length=20)

    class Meta:
        db_table = "menus"


class Category(models.Model):

    """Category Model Definition"""

    name = models.CharField(max_length=20)
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)

    class Meta:
        db_table = "categories"


class Product(models.Model):

    """Product Model Definition"""

    name = models.CharField(max_length=100)
    english_name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    allergies = models.ManyToManyField(
        "Allergy", through="Allergy_Product", related_name="products"
    )

    class Meta:
        db_table = "products"


class Image(models.Model):
    image_url = models.URLField()
    product = models.OneToOneField("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "images"


class Allergy(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = "allergies"


class Allergy_Product(models.Model):
    allergy = models.ForeignKey("Allergy", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        db_table = "allergies_products"
