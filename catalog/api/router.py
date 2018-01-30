from catalog.api.views import ProductViewSet, StoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stores', StoreViewSet)
