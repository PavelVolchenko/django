from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# class User(models.Model):
class User(AbstractBaseUser):
    username = models.CharField(max_length=36)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16, null=True)
    address = models.CharField(max_length=256, null=True)
    registered = models.DateField(auto_now_add=True)
    USERNAME_FIELD = "email"

    def __str__(self):
        return (f"+---------------------------------------"
                f"\n| username: {self.username}\n"
                f"|    email: {self.email}\n"
                f"|    phone: {self.phone_number}\n"
                f"|  address: {self.address}")


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    was_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"+---------------------------------------"
                f"\n|        name: {self.product_name}\n"
                f"| description: {self.description}\n"
                f"|       price: {self.price}")


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
