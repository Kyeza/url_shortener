from django.urls import path, include
from rest_framework.routers import DefaultRouter

from shortener.api import ShortUrlViewSet
from shortener.views import root, index

router = DefaultRouter()
router.register('short_urls', ShortUrlViewSet)

app_name = 'shortener'
urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),
    path('<str:slug>/', root, name='root'),
]
