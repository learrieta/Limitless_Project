from django.shortcuts import render
from .models import Workout, Exercise, WorkoutExercise, WorkoutLog
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts/workout_list.html', {'workouts': workouts})

def details(request, id):
    workout = WorkoutExercise.objects.get(pk= id)
    template = loader.get_template('workout_detail.html')
    context = {
        'mymember': workout,
     }
    return HttpResponse(template.render(context, request))




