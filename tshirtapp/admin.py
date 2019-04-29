from django.contrib import admin
from tshirtapp.models import User, Customer


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', "email", 'is_customer', 'is_admin', 'last_login', 'date_joined']

    def __str__(self):
        return self.username


@admin.register(Customer)
class UserAdmin(admin.ModelAdmin):
    list_display = ["credit_card","address_1", "city", "region", "postal_code", "country", "shipping_region_id", "day_phone"]
