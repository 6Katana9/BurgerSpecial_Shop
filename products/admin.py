from django.contrib import admin
from .models import Products, Cotegory, Company

admin.site.register(Products)
admin.site.register(Company)
admin.site.register(Cotegory)