from catalog.api.serializers import (ProductDetailsSerializer,
                                     ProductSerializer, StoreSerializer)
from catalog.models import Product, Store
from rest_framework import viewsets


class StoreViewSet(viewsets.ModelViewSet):
    model = Store
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


class ProductViewSet(viewsets.ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = None

    def list(self, request, *args, **kwargs):
        self.serializer_class = ProductSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, pk=None, *args, **kwargs):
        self.serializer_class = ProductDetailsSerializer
        return super().retrieve(request, pk, *args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        store_id = self.request.query_params.get('store')
        if store_id is not None:
            if Store.objects.filter(id=store_id).exists():
                return queryset.filter(store_id=store_id)
            return None
        return queryset
