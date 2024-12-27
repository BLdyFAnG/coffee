from django.db import models

class CoffeeType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(help_text="Quantity in grams/ml")

    def __str__(self):
        return self.name

class Order(models.Model):
    coffee_type = models.ForeignKey(CoffeeType, on_delete=models.CASCADE)
    sugar_level = models.CharField(max_length=50, choices=[('None', 'None'), ('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High')])
    milk_preference = models.BooleanField(default=True)
    size = models.CharField(max_length=50, choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.coffee_type.name}"

class MaintenanceTask(models.Model):
    task_name = models.CharField(max_length=200)
    scheduled_date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name


