from django.shortcuts import render
from .models import Meal, MealPlan, Recipe, Nutrition
from django.http import HttpResponse


# Create your views here.
def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

def meal_detail(request, meal_id):
    meal = Meal.objects.get(pk=meal_id)
    return render(request, 'meals/meal_detail.html', {'meal': meal})

# fetches all meal plans for a specific user and renders them in a template:
def meal_plans(request):
    meal_plans = MealPlan.objects.filter(user=request.user)
    context = {'meal_plans': meal_plans}
    return render(request, 'meals/meal_plans.html', context)

def meal_plans_testing(request):
    return render(request, 'Meals/meal_plans.html') 



