from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('id','firstname','lastname','email','phone',)    

admin.site.register(Categories)

@admin.register(Subcategories)
class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = ('id','subcat','name')
    list_editable = ('name',)
    list_display_links = ('id','subcat')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','categories','image','price')

@admin.register(Mycart)
class MycartAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity')


