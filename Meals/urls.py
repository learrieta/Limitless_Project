from django.urls import path
from Meals import views

urlpatterns = [
    path('meal_prep/', views.meal_plans_testing, name='meal_prep'),
]

##http://127.0.0.1:8000/meals/meal_prep/
##views need the name of what is being rendered.. name=