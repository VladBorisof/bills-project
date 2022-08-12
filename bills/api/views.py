from rest_framework import filters, permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from api.serializers import BillsSerializer
from service.models import Bills


class BillsViewSet(viewsets.ModelViewSet):
    queryset = Bills.objects.all()
    serializer_class = BillsSerializer
    permission_classes = (permissions.AllowAny,)
    pagination_class = LimitOffsetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('client_org', 'client_name')

    def perform_create(self, serializer):
        serializer.save(client_name=self.request.user)
