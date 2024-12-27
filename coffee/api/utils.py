from .models import Ingredient


def ingrediant_calc(instance):
    sugar = Ingredient.objects.get(name="Sugar")
    milk = Ingredient.objects.get(name="Milk")
    coffee_bean = Ingredient.objects.get(name="coffee-beans")

    if instance.sugar_level == "None":
        pass
    
    elif instance.sugar_level == "Low":
        sugar.quantity = sugar.quantity - 10
        sugar.save()

    elif instance.sugar_level == "Medium":
        sugar.quantity = sugar.quantity - 15
        sugar.save()

    if instance.milk_preference:
        milk.quantity -= 10
        milk.save()
    else:
        pass

    if instance.size == "Small":
        coffee_bean.quantity -= 10
        coffee_bean.save()
    
    elif instance.size == "Medium":
        coffee_bean.quantity -= 20
        coffee_bean.save()
    
    elif instance.size == "Large":
        coffee_bean.quantity -= 25
        coffee_bean.save()