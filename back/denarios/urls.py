import debug_toolbar
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from django.views.generic import TemplateView
from denarios.core import views as core_views
from django.urls import path, include
from denarios.core.views import (
    homeviews,
    exchanges,
)

router = DefaultRouter()

router.register(r'exchange_lisy', exchanges.ExchangeViewSet, basename='exchange_list')

urlpatterns = [
    path('', homeviews.index, name="index"),
    path('test-sentry/', lambda request: 1/0),
    path('integracao/', include(router.urls)),
    path('__debug__/', include(debug_toolbar.urls)),
]
