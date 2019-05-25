from django.contrib import admin
from tshirtapp.models import User, Customer, Admin, Product


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', "email", 'is_customer', 'is_admin', 'last_login', 'date_joined']

    def __str__(self):
        return self.username


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["user", "credit_card", "address_1", "city", "region", "postal_code", "country",
                    "shipping_region_id", "day_phone"]

    def __str__(self):
        return f'Customer {self.user.first_name}:'


@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['user', "credit_card"]

    def __str__(self):
        return f'Admin {self.user.first_name}:'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', "description", 'price']

    def __str__(self):
        return f'Admin {self.user.first_name}:'


