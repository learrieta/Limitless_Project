from django.urls import path
from Workouts import views

urlpatterns = [
    path('', views.workout_list, name="home_page"),
    path('members/<int:id>', views.details, name='details'),
]