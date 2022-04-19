from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    edition = models.IntegerField()

    def __str__(self) -> str:
        return self.title

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Cart(models.Model):
    customer = models.OneToOneField(Customer, null=True, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book)

    def __str__(self) -> str:
        return str(self.customer)