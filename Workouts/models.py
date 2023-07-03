from django.db import models
from django.contrib.auth.models import User
import uuid

class Exercise(models.Model):
    DAY_OF_WEEK_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    muscle_group = models.CharField(max_length=100)  # e.g., 'chest', 'legs', 'arms'
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK_CHOICES)
    equipment_required = models.CharField(max_length=100, blank=True, null=True)  # e.g., 'dumbbell', 'barbell', 'bodyweight'
    workout_picture = models.ImageField( default ='default.png')

    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        img = ''
        try:
            if self.workout_picture.url:
                img = self.workout_picture.url
        except:
            img = ''

        return img

class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Workout(models.Model):
    
    TRAINING_LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
    training_level = models.CharField(max_length=1, choices=TRAINING_LEVEL_CHOICES)
    
    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    TRAINING_LEVEL_CHOICES = [
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    ]
    DAY_OF_WEEK_CHOICES = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
    ]
    name = models.CharField(max_length=100)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK_CHOICES)
    sets = models.IntegerField()
    reps = models.IntegerField()
    rest_time = models.IntegerField()  # Rest time in seconds
    training_level = models.CharField(max_length=1, choices=TRAINING_LEVEL_CHOICES)
    id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable= False)


    def __str__(self):
        return self.name



class WorkoutLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)
    date_completed = models.DateField()
    duration = models.IntegerField()  # Duration in minutes
