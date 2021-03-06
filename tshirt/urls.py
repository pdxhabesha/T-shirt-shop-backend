"""tshirt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tshirtapp import views

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'shipping', views.ShippingViewSet)
router.register(r'tax', views.TexViewSet)
router.register(r'department', views.DepartmentViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('signup/customer/', views.signup_customer, name='signup_seeker'),
    path('signup/admin/', views.signup_admin, name='signup_admin'),
    path('api/upload', views.upload, name="uplaod"),

    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]


