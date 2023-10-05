from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


class User(AbstractBaseUser):
    username = models.CharField(max_length=36, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16, null=True)
    address = models.CharField(max_length=256, null=True)
    registered = models.DateField(auto_now_add=True)
    USERNAME_FIELD = "username"

    def __str__(self):
        return (f"\n| username: {self.username}\n"
                f"|    email: {self.email}\n")


class Product(models.Model):
    product_name = models.CharField(max_length=128)
    description = models.CharField(max_length=1024, null=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(default=0)
    was_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"\n|        name: {self.product_name}\n"
                f"| description: {self.description}\n"
                f"|       price: {self.price}")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('store.views.add_to_cart', args=[str(self.id)])


class CompletedOrderManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Order.Status.COMPLETED)


class Order(models.Model):
    class Status(models.TextChoices):
        BASKET = 'BS', 'Basket'
        COMPLETED = 'CP', 'Completed'

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order_products', through='OrderProductCount')
    total_price = models.IntegerField(default=0)
    date_ordered = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.BASKET)

    objects = models.Manager()  # менеджер по умолчанию
    completed = CompletedOrderManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-date_ordered']  # сортировка результатов в обратном хронологическом порядке
        indexes = [
            models.Index(fields=['-date_ordered'])  # индексация в убывающем порядке
        ]

class OrderProductCount(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)