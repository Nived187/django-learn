from django.contrib import admin

# Register your models here.
from .models import Product,Example

admin.site.register(Product)
admin.site.register(Example)