from django.contrib.auth.models import Group
from django.db import transaction
from rest_framework import serializers
from .models import Product, Shipping, Tax, Department, Customer, User, Admin


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = ("name", "description", "image", "thumbnail", "display")
        fields = "__all__"


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


class SignupCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    @transaction.atomic  # Ensure creation of both models is done in a single transaction not to create inconsistencies
    def create(self, validated_data):
        """
        Creates new User and Seeker profile.
        """
        # Create auth user model first
        validated_user_data = validated_data.pop('user', {})
        user = User.objects.create(is_customer=True, **validated_user_data)
        print("user", user)
        print("validated_user_data", validated_user_data)
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
        # Create Seeker profile
        return Admin.objects.create(user=user, **validated_data)
