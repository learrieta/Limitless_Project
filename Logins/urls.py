from django.urls import path
from Logins.views import login_user, user_logout, user_profile,register,user_dashboard, user_workout_b,user_workout_i,user_workout_a, user_meal_a, user_meal_b, user_meal_i
from Home.views import home
import Workouts

urlpatterns = [
    path('login_user', login_user, name="login"),
    path('register_user',register, name = "registration"),
    path('user_logout', user_logout, name="user_logout"),
    path('profile', user_profile, name="user_profile"),
    path('dashboard', user_dashboard, name="user_dashboard"),
    path('workoutb', user_workout_b, name="user_workout_b"),
    path('workouti', user_workout_i, name="user_workout_i"),
    path('workouta', user_workout_a, name="user_workout_a"),
    path('mealb', user_meal_b, name="user_meal_b"),
    path('meali', user_meal_i, name="user_meal_i"),
    path('meala', user_meal_a, name="user_meal_a"),
    path('', home, name="home_page")
    
]