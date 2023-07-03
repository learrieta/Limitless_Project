from django.db import models
from Logins.models import UserProfile
from Meals.models import MealPlan
from Workouts.models import Workout


class Recommendation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    recommended_meal = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    recommended_workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    def __str__(self):
        return self.recommended_workout.name