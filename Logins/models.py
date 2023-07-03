from django.db import models
from django.contrib.auth.models import User
import uuid
from Meals.models import MealPlan
from Workouts.models import Workout, WorkoutExercise, Exercise

class UserProfile(models.Model):
    TRAINING_LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.SmallIntegerField(default=0)
    bio = models.TextField(max_length=500, blank=True)
    height = models.FloatField(default=5.0)  # Height in meters
    weight = models.FloatField(default=200)  # Weight in kilograms
    monthly_goals1 = models.CharField( max_length=1000, default="goals")
    monthly_goals2 = models.CharField( max_length=1000, default="goals")
    monthly_goals3 = models.CharField( max_length=1000, default="goals")
    profile_picture = models.ImageField( null=True, blank=True,default ="default.png")
    recommended_meal = models.CharField( max_length=1000, default="goals")
    recommended_workout = models.CharField( max_length=1000, default="goals")
    training_level = models.CharField(max_length=1, choices=TRAINING_LEVEL_CHOICES, default='B')
    sleep_goals = models.CharField( max_length=40, default="8 hours")
    water_goals = models.CharField( max_length=1000, default="3 Liters")

    def __str__(self):
        return self.user.first_name
    
    @property
    def imageUrl(self):
        img = ''
        try:
            if self.profile_picture.url:
                img = self.profile_picture.url
        except:
            img = ''

        return img



    # def calculate_recommendations(self):
    #     # decide the right MealPlan and Workout based on the UserProfile attributes.
    #     # This could involve fetching different MealPlan and Workout objects from the database.
    #     ...
    #     return recommended_mealplan, recommended_workout