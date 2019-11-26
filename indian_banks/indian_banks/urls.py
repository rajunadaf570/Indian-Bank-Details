"""indian_banks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

# Django Inports
from django.contrib import admin
from django.urls import path, include

# Third Party Imports
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import SimpleRouter

# Project Level Imports
from bank import views  as banks_views

# intialize DefaultRouter
router = SimpleRouter()

# register bank app urls with router
router.register(r'banks', banks_views.BanksViewSet, base_name='banks')

urlpatterns = [
    # path(r'admin/', admin.site.urls),
    path(r'api/v1/', include((router.urls, 'api'), namespace='v1')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
