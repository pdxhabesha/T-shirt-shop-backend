from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# from tshirtapp.serializers import ProductSerializer, \
#     ShippingSerializer, TaxSerializer, DepartmentSerializer, SignupCustomerSerializer, SignupAdminSerializer
# from tshirtapp.models import Product, Shipping, Tax, Department
from tshirtapp.serializers import SignupAdminSerializer, SignupCustomerSerializer


@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_customer(request):
    """Signs up a Seeker and returns an access and refresh JSON web token pair"""

    serializer = SignupCustomerSerializer(data=request.data, context={'request': request})
    print("before is_valid")
    serializer.is_valid(raise_exception=True)
    # print("serializer error: ", serializer.errors)
    print("after is_valid, before save")

    serializer.save()
    print("after save")

    return Response(data=serializer.data)


@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_admin(request):
    """Signs up a Seeker and returns an access and refresh JSON web token pair"""

    serializer = SignupAdminSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)

#
# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#
# class ShippingViewSet(viewsets.ModelViewSet):
#     queryset = Shipping.objects.all()
#     serializer_class = ShippingSerializer
#
#
# class TexViewSet(viewsets.ModelViewSet):
#     queryset = Tax.objects.all()
#     serializer_class = TaxSerializer
#
#
# class DepartmentViewSet(viewsets.ModelViewSet):
#     queryset = Department.objects.all()
#     serializer_class = DepartmentSerializer
#
