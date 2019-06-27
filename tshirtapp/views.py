from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from tshirt import settings
from tshirtapp.serializers import ProductSerializer, ShippingSerializer, TaxSerializer, DepartmentSerializer, \
    SignupCustomerSerializer, SignupAdminSerializer, OrderSerializer, CustomerSerializer, ShippingRegionSerializer
from tshirtapp.models import Product, Shipping, Tax, Department, Category, Customer, ShippingRegion

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_customer(request):
    """Signs up a Customer and returns an access and refresh JSON web token pair"""

    serializer = SignupCustomerSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response(data=serializer.data)


@api_view(http_method_names=['POST'])
@permission_classes([])
def signup_admin(request):
    """Signs up a Admin and returns an access and refresh JSON web token pair"""

    serializer = SignupAdminSerializer(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(data=serializer.data)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class TexViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class ShippingRegionViewSet(viewsets.ModelViewSet):
    queryset = ShippingRegion.objects.all()
    serializer_class = ShippingRegionSerializer


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


@api_view(http_method_names=['GET'])
@permission_classes([])
def upload(request):
    """
    INTO `product_category` (`product_id`, `category_id`) VALUES
       (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
       (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1),
       (18, 1), (19, 2), (20, 2), (21, 2), (22, 2), (23, 2), (24, 2), (25, 2),
       (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 3),
       (34, 3), (35, 3), (36, 4), (37, 4), (38, 4), (39, 4), (40, 4), (41, 4),
       (42, 4), (43, 4), (44, 4), (45, 4), (46, 4), (47, 4), (48, 4), (49, 4),
       (50, 4), (51, 4), (52, 4), (53, 4), (54, 4), (55, 4), (56, 4), (57, 4),
       (58, 4), (59, 4), (60, 4), (61, 4), (62, 4), (63, 4), (64, 4), (81, 4),
       (97, 4), (98, 4), (65, 5), (66, 5), (67, 5), (68, 5), (69, 5), (70, 5),
       (71, 5), (72, 5), (73, 5), (74, 5), (75, 5), (76, 5), (77, 5), (78, 5),
       (79, 5), (80, 6), (81, 6), (82, 6), (83, 6), (84, 6), (85, 6), (86, 6),
       (87, 6), (88, 6), (89, 6), (90, 6), (91, 6), (92, 6), (93, 6), (94, 6),
       (95, 6), (96, 7), (97, 7), (98, 7), (99, 7), (100, 7), (101, 7);
    """
    ids = ((1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1),
       (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 1), (16, 1), (17, 1),
       (18, 1), (19, 2), (20, 2), (21, 2), (22, 2), (23, 2), (24, 2), (25, 2),
       (26, 2), (27, 2), (28, 2), (29, 3), (30, 3), (31, 3), (32, 3), (33, 3),
       (34, 3), (35, 3), (36, 4), (37, 4), (38, 4), (39, 4), (40, 4), (41, 4),
       (42, 4), (43, 4), (44, 4), (45, 4), (46, 4), (47, 4), (48, 4), (49, 4),
       (50, 4), (51, 4), (52, 4), (53, 4), (54, 4), (55, 4), (56, 4), (57, 4),
       (58, 4), (59, 4), (60, 4), (61, 4), (62, 4), (63, 4), (64, 4), (81, 4),
       (97, 4), (98, 4), (65, 5), (66, 5), (67, 5), (68, 5), (69, 5), (70, 5),
       (71, 5), (72, 5), (73, 5), (74, 5), (75, 5), (76, 5), (77, 5), (78, 5),
       (79, 5), (80, 6), (81, 6), (82, 6), (83, 6), (84, 6), (85, 6), (86, 6),
       (87, 6), (88, 6), (89, 6), (90, 6), (91, 6), (92, 6), (93, 6), (94, 6),
       (95, 6), (96, 7), (97, 7), (98, 7), (99, 7), (100, 7), (101, 7));
    idx = 1
    products = Product.objects.all()
    for product in products:
        product.product_category.add(Category.objects.get(category_id=ids[idx][1]))
        idx += 1

    serializer = ProductSerializer(instance=products, context={'request': request})

    return Response(data=serializer.data)


@swagger_auto_schema(methods=['post'], request_body=OrderSerializer)
@api_view(http_method_names=['POST'])
@permission_classes([])
def charge(request):
    amount = request.data['total_amount'] or 250
    currency = 'usd'
    comments = 'Test Description'

    status = stripe.Charge.create(
        amount=amount,
        currency=currency,
        description=comments,
        source=request.data['token']
    )
    serializer = OrderSerializer(data=request.data, context={'request': request})

    serializer.is_valid()
    if serializer.errors:
        return Response(data=serializer.errors, status=404)

    else:
        serializer.save()
        return Response(data=status)
