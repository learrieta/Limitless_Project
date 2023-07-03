from django.contrib import admin
from .models import Workout, Exercise, WorkoutExercise, WorkoutLog, Equipment

# Register your models here.
admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(WorkoutExercise)
admin.site.register(WorkoutLog)
admin.site.register(Equipment)

