from django.contrib import admin
from .models import MealPlan, Meal, Nutrition, Recipe

admin.site.register(MealPlan)
admin.site.register(Meal)
admin.site.register(Nutrition)
admin.site.register(Recipe)
