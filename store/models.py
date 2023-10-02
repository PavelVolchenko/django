from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser


# class User(models.Model):
class User(AbstractBaseUser):
    username = models.CharField(max_length=36, unique=True)
    email = models.EmailField(blank=True)
    password = models.CharField(max_length=256)
    phone_number = models.CharField(max_length=16, null=True)
    address = models.CharField(max_length=256, null=True)
    registered = models.DateField(auto_now_add=True)
    USERNAME_FIELD = "username"

    def __str__(self):
        return (f""
                # f"+---------------------------------------"
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
        return (f""
                # f"+---------------------------------------"
                f"\n|        name: {self.product_name}\n"
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
    products = models.ManyToManyField(Product)
    total_price = models.IntegerField(null=True)
    date_ordered = models.DateTimeField(auto_now_add=False)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.BASKET)

    object = models.Manager()  # менеджер по умолчанию
    completed = CompletedOrderManager()  # конкретно-прикладной менеджер

    class Meta:
        ordering = ['-date_ordered']  # сортировка результатов в обратном хронологическом порядке
        indexes = [
            models.Index(fields=['-date_ordered'])  # индексация в убывающем порядке
        ]

    # def __str__(self):
    #     return self.customer
