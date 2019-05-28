from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    """
    Django abstract model has auto create and update datetime fields.
    This acts as the base model for all other models.
    """
    created_at = models.DateTimeField(verbose_name=_('created time'), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name=_('updated time'), auto_now=True, db_index=True)

    class Meta:
        abstract = True


class User(AbstractUser, BaseModel):
    is_customer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = (('username', 'email'),)

    def __str__(self):
        return f'{self.id}: {self.username} {self.first_name} {self.last_name}'


class Admin(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Admin {self.user.first_name}:'


class Customer(BaseModel):
    customer_id=models.AutoField(primary_key=True, serialize=False,)
    credit_card = models.TextField(blank=True, null=True)
    address_1 = models.CharField(max_length=100, blank=True, null=True)
    address_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    day_phone = models.CharField(max_length=100, blank=True, null=True)
    eve_phone = models.CharField(max_length=100, blank=True, null=True)
    mob_phone = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(verbose_name=_('user'), to='User', related_name='%(class)s', on_delete=models.CASCADE)
    shipping_region = models.ForeignKey(verbose_name=_('shipping_region'), to="ShippingRegion", default=1,
                                        on_delete="CASCADE", blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'customer'

    def __str__(self):
        return f'Customer {self.user.first_name}:'


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
    attribute = models.ManyToManyField(to=AttributeValue, default=1, verbose_name="product_attribute")
    category = models.ManyToManyField(to=Category, default=1, verbose_name="product_category")

    class Meta:
        db_table = "product"


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
    created_on = models.DateTimeField(verbose_name=_('created on'), auto_now_add=True, db_index=True)
    shipped_on = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    auth_code = models.CharField(max_length=50, blank=True, null=True)
    reference = models.CharField(max_length=50, blank=True, null=True)
    customer = models.ForeignKey(Customer, verbose_name="customer_id", on_delete=models.CASCADE, null=True, blank=True)
    tax = models.ForeignKey(Tax, verbose_name="tax_id", on_delete=models.CASCADE, null=False, blank=False, default=1)
    shipping = models.ForeignKey(Shipping, verbose_name="shipping_id", on_delete=models.CASCADE,
                                 default=3, null=False)

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


# class Transaction(models.Model):
#     description = models.CharField(max_length=500, blank=False, null=False)
#     user = models.ForeignKey(to="User", related_name='transaction', on_delete=models.PROTECT, blank=True, null=True)
#     item = models.ForeignKey(to="Product", on_delete=models.PROTECT)
#     amount = models.IntegerField()
#     currency = models.CharField(max_length=3, default='usd')
