from rest_framework.routers import DefaultRouter
from .views import LocationViewSet, InventoryViewSet

router = DefaultRouter()
router.register('location', LocationViewSet, basename='location')
router.register('inventory', InventoryViewSet, basename='inventory')
urlpatterns = router.urls
