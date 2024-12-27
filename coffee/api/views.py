from rest_framework import viewsets
from .models import CoffeeType, Ingredient, Order, MaintenanceTask
from .serializers import CoffeeTypeSerializer, IngredientSerializer, OrderSerializer, MaintenanceTaskSerializer
from rest_framework import status
from rest_framework.response import Response
from .utils import ingrediant_calc
from rest_framework.decorators import api_view
from .models import Ingredient
from .serializers import IngredientSerializer


class CoffeeTypeViewSet(viewsets.ModelViewSet):
    queryset = CoffeeType.objects.all()
    serializer_class = CoffeeTypeSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        instance = serializer.instance
      
        ingrediant_calc(instance)
        
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class MaintenanceTaskViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceTask.objects.all()
    serializer_class = MaintenanceTaskSerializer


@api_view(['POST'])
def updateingredients(request):
    
    try:
        ingredient_name = request.data.get('name')
        quantity = request.data.get('quantity')

        if not ingredient_name or not quantity:
            return Response({"error": "Both 'name' and 'quantity' are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the ingredient already exists
        ingredient, created = Ingredient.objects.get_or_create(name=ingredient_name)

        if created:
            ingredient.quantity = quantity  # Set quantity for the new ingredient
        else:
            ingredient.quantity += int(quantity)  # Update quantity for the existing ingredient

        ingredient.save()

        serializer = IngredientSerializer(ingredient)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)