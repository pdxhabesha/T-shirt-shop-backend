# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    credit_card = models.TextField(blank=True, null=True)


class Customer(models.Model):
    user = models.OneToOneField(verbose_name=_('user'), to='User', related_name='%(class)s', on_delete=models.CASCADE)
    credit_card = models.TextField(blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    shipping_region_id = models.IntegerField(blank=True, null=True)
    day_phone = models.CharField(max_length=100, blank=True, null=True)
    eve_phone = models.CharField(max_length=100, blank=True, null=True)
    mob_phone = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f'{self.user.first_name}:'

#
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_id = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
#
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
#
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
#
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'


class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'attribute'


class AttributeValue(models.Model):
    attribute_value_id = models.AutoField(primary_key=True)
    attribute_id = models.IntegerField()
    value = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'attribute_value'


class Audit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    created_on = models.DateTimeField()
    message = models.TextField()
    code = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audit'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    department_id = models.IntegerField()
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class OrderDetail(models.Model):
    item_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_detail'


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField()
    shipped_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    comments = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.IntegerField(blank=True, null=True)
    auth_code = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    shipping_id = models.IntegerField(blank=True, null=True)
    tax_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150, blank=True, null=True)
    image_2 = models.CharField(max_length=150, blank=True, null=True)
    thumbnail = models.CharField(max_length=150, blank=True, null=True)
    display = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'product'


class ProductAttribute(models.Model):
    product_id = models.IntegerField()
    attribute_value_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_attribute'
        unique_together = (('product_id', 'attribute_value_id'),)


class ProductCategory(models.Model):
    product_id = models.IntegerField()
    category_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_category'
        unique_together = (('product_id', 'category_id'),)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    product_id = models.IntegerField()
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'review'


class Shipping(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    shipping_type = models.CharField(max_length=100)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_region_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'shipping'


class ShippingRegion(models.Model):
    shipping_region_id = models.AutoField(primary_key=True)
    shipping_region = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'shipping_region'


class ShoppingCart(models.Model):
    item_id = models.AutoField(primary_key=True)
    cart_id = models.CharField(max_length=32)
    product_id = models.IntegerField()
    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.IntegerField()
    added_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'shopping_cart'


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_type = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tax'







class Attribute(models.Model):
    attribute_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'attribute'


class AttributeValue(models.Model):
    attribute_value_id = models.AutoField(primary_key=True)
    attribute = models.ForeignKey(Attribute, verbose_name="attribute_id",
                                  on_delete=models.CASCADE, default=1, null=False)
    value = models.CharField(max_length=100)

    class Meta:
        db_table = 'attribute_value'
        # indexes = "attribute_id"


class Cart(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'cart'


class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'department'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000, blank=True, null=True)
    department = models.ForeignKey(verbose_name="department_id", to="Department",
                                   on_delete=models.CASCADE, default=1, null=False)

    class Meta:
        db_table = 'category'


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=150, blank=True, null=True)
    image_2 = models.CharField(max_length=150, blank=True, null=True)
    thumbnail = models.CharField(max_length=150, blank=True, null=True)
    display = models.SmallIntegerField()
    product_attribute = models.ManyToManyField(to="AttributeValue")
    product_category = models.ManyToManyField(to="Category")

    class Meta:
        db_table = "product"


# class ProductAttribute(models.Model):
#     product_id = models.ForeignKey(Product, on_delete="CASCADE")
#     attribute_value = models.ForeignKey(verbose_name="attribute_value_id", to='AttributeValue', on_delete="CASCADE")
#
#     class Meta:
#         db_table = "product_attribute"
#         # unique_together = (('product_id', 'attribute_value'),)
#
#
# class ProductCategory(models.Model):
#     product = models.OneToOneField(verbose_name="product_id", to="Product", on_delete="CASCADE")
#     category = models.ForeignKey(verbose_name="category_id", to='AttributeValue', on_delete="CASCADE")
#     name = models.CharField(max_length=100, null=True, blank=True, default="name")
#
#     class Meta:
#         db_table = "product_category"
#         # unique_together = (('product', 'category'),)
#

class OrderDetail(models.Model):
    item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(to="Orders", verbose_name="order_id", on_delete=models.CASCADE,
                              default=1, null=False)
    product = models.ForeignKey(Product, verbose_name="product_id", on_delete=models.CASCADE,
                                default=1, null=False)

    attributes = models.CharField(max_length=1000)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'order_detail'


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, verbose_name="customer_id", on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, verbose_name="product_id", on_delete=models.CASCADE,
                                default=1, null=False)
    review = models.TextField()
    rating = models.SmallIntegerField()
    created_on = models.DateTimeField()

    class Meta:
        db_table = "review"


class Shipping(models.Model):
    shipping_id = models.AutoField(primary_key=True)
    shipping_type = models.CharField(max_length=100)
    shipping_cost = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_region = models.ForeignKey(to="ShippingRegion", verbose_name="shipping_region_id",
                                        on_delete=models.CASCADE, default=1, null=False)

    class Meta:
        db_table = "shipping"


class ShippingRegion(models.Model):
    shipping_region_id = models.AutoField(primary_key=True)
    shipping_region = models.CharField(max_length=100)

    class Meta:
        db_table = "shipping_region"


class ShoppingCart(models.Model):
    item_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, verbose_name="product_id", on_delete=models.CASCADE,
                                default=1, null=False)
    cart = models.ForeignKey(Cart, verbose_name="cart_id", on_delete=models.CASCADE,
                             default=1, null=False)

    attributes = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    buy_now = models.IntegerField()
    added_on = models.DateTimeField()

    class Meta:
        db_table = "shopping_cart"


class Tax(models.Model):
    tax_id = models.AutoField(primary_key=True)
    tax_type = models.CharField(max_length=100)
    tax_percentage = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = "tax"


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_on = models.DateTimeField()
    shipped_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    comments = models.CharField(max_length=255, blank=True, null=True)
    auth_code = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(Customer, verbose_name="customer_id", on_delete=models.CASCADE,
                                 default=1, null=False)
    tax = models.ForeignKey(Tax, verbose_name="tax_id", on_delete=models.CASCADE, null=True)
    shipping = models.ForeignKey(Shipping, verbose_name="shipping_id", on_delete=models.CASCADE,
                                 default=1, null=False)

    class Meta:
        db_table = 'orders'


class Audit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Orders, verbose_name="order_id", on_delete=models.CASCADE, null=True)
    created_on = models.DateTimeField()
    message = models.TextField()
    code = models.IntegerField()

    class Meta:
        db_table = 'audit'
