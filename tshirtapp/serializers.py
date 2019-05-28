from django.db import transaction
from rest_framework import serializers
from .models import Product, Shipping, Tax, Department, Customer, User, Admin


class SignupCustomerSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', max_length=255)
    email = serializers.EmailField(source='user.email', max_length=255)
    password = serializers.CharField(source='user.password', max_length=128, write_only=True)
    old_password = serializers.CharField(max_length=128, write_only=True, required=False)
    first_name = serializers.CharField(source='user.first_name', allow_blank=True, max_length=30, required=False)
    last_name = serializers.CharField(source='user.last_name', allow_blank=True, max_length=150, required=False)
    is_customer = serializers.ReadOnlyField(source='user.is_customer')
    is_admin = serializers.ReadOnlyField(source='user.is_admin')

    class Meta:
        model = Customer
        fields = ['email', 'username',  "first_name", "password", "last_name", "old_password", "is_customer", "is_admin"]

    @transaction.atomic  # Ensure creation of both models is done
    # in a single transaction not to create inconsistencies
    def create(self, validated_data):
        """
        Creates new User and Seeker profile.
        """
        # Create auth user model first
        validated_user_data = validated_data.pop('user', {})
        user = User.objects.create_user(is_customer=True, **validated_user_data)
        # Create Seeker profile
        return Customer.objects.create(user=user, **validated_data)


class SignupAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = "__all__"

    @transaction.atomic  # Ensure creation of both models is done in a single transaction not to create inconsistencies
    def create(self, validated_data):
        """
        Creates new User and Seeker profile.
        """
        # Create auth user model first
        validated_user_data = validated_data.pop('user', {})
        user = User.objects.create_user(is_customer=True, **validated_user_data)
        # Create Admin profile
        return Admin.objects.create(user=user, **validated_data)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        depth = 2


class ShippingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shipping
        fields = "__all__"


class TaxSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tax
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = "__all__"

