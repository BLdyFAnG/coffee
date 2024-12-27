from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import updateingredients, CoffeeTypeViewSet, IngredientViewSet, OrderViewSet, MaintenanceTaskViewSet

router = DefaultRouter()
router.register(r'coffee-types', CoffeeTypeViewSet, basename='coffee-type')
router.register(r'ingredients', IngredientViewSet, basename='ingredient')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'maintenance-tasks', MaintenanceTaskViewSet, basename='maintenance-task')

urlpatterns = [
    path("update-ingredients/", updateingredients),  # Add this line
    path("", include(router.urls)),  # Include ViewSet-generated URLs
]

