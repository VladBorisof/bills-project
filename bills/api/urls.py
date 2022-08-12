from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import BillsViewSet

router = DefaultRouter()
router.register('bills', BillsViewSet, basename='bills')

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/', include('djoser.urls.jwt')),
]