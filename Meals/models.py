from django.db import models
from django.contrib.auth.models import User

class MealPlan(models.Model):
    MEAL_TYPE_CHOICES = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class Meal(models.Model):
    MEAL_TYPE_CHOICES = [
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner'),
    ]
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    calories = models.IntegerField()
    meal_type = models.CharField(max_length=1, choices=MEAL_TYPE_CHOICES)
    prep_time = models.IntegerField()  # Preparation time in minutes
    cook_time = models.IntegerField()  # Cooking time in minutes
    servings = models.IntegerField()  # Number of servings
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nutrition(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE)
    protein = models.FloatField()  # Protein in grams
    carbohydrates = models.FloatField()  # Carbohydrates in grams
    fats = models.FloatField()  # Fats in grams
    fiber = models.FloatField()  # Fiber in grams

    def __str__(self):
        return f'Nutrition info for {self.meal.name}'

class Recipe(models.Model):
    meal = models.OneToOneField(Meal, on_delete=models.CASCADE, null=True)
    # a OneToOneField, each Meal must have a Recipe
    #  each Meal can have only one Recipe. If there could be multiple recipes for a single meal 
    # (for instance, variations on the recipe)
    # , use a ForeignKey in the Recipe model.
    ingredients = models.TextField()
    instructions = models.TextField()
    prep_time = models.IntegerField()  # Preparation time in minutes
    cook_time = models.IntegerField()  # Cooking time in minutes

    def __str__(self):
        if self.meal:
            return f'Recipe info for {self.meal.name}'
        else:
            return "Unnamed Recipe"
