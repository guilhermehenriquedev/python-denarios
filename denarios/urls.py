import debug_toolbar
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from django.urls import path, include
from denarios.core.views import (
    homeviews,
    exchanges,
)

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

router.register(r'exchanges', exchanges.ExchangeViewSet, basename='exchanges') #exchanges/criptos/

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('integracao/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='permanent_auth_token'),
    path('jwt-token/', TokenObtainPairView.as_view(), name='jwt_auth_token_obtain'),
    path('jwt-token/refresh/', TokenRefreshView.as_view(), name='jwt_auth_token_refresh')
]
