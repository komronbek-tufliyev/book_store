from django.contrib import admin
from .models import Book, Cart, Customer

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'price', 'edition']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['customer',]
