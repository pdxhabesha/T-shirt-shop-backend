from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from tshirtapp.serializers import ProductSerializer, ShippingSerializer, TaxSerializer, DepartmentSerializer, \
    SignupCustomerSerializer, SignupAdminSerializer
from tshirtapp.models import Product, Shipping, Tax, Department, Category
# from tshirtapp.models import Product, Shipping, Tax, Department


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


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(data=serializer.data)


class ShippingViewSet(viewsets.ModelViewSet):
    queryset = Shipping.objects.all()
    serializer_class = ShippingSerializer


class TexViewSet(viewsets.ModelViewSet):
    queryset = Tax.objects.all()
    serializer_class = TaxSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


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
