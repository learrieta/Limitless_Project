from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SignUpForm
from django.shortcuts import get_object_or_404
from recommendations.models import Recommendation
from .forms import UserProfileForm
from Workouts.models import Workout, WorkoutExercise, Exercise
from Meals.models import *
from datetime import datetime



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the User and get a reference to it
            UserProfile.objects.create(
                user=user,
                bio = form.cleaned_data['bio'],
                age = form.cleaned_data['age'], 
                profile_picture = form.cleaned_data['profile_picture'],
                height = form.cleaned_data['height'] , # Height in meters
                weight = form.cleaned_data['weight']  ,# Weight in kilograms
                monthly_goals1 = form.cleaned_data['monthly_goals1'],
                monthly_goals2 = form.cleaned_data['monthly_goals2'],
                monthly_goals3 = form.cleaned_data['monthly_goals3'],
                sleep_goals = form.cleaned_data['sleep_goals'],
                water_goals = form.cleaned_data['water_goals'],


            )  # Create UserProfile and saves the user input into userprofile, works as a foreignkey
            login(request, user)
            return redirect('user_profile')  # Redirect to home view after successful registration
    else:
        form = SignUpForm()
    return render(request, 'Logins/register.html', {'form': form})


def login_user(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile')
        else:
            messages.success(request,("There was an error login in"))
            return redirect('login')
    return render (request,'Logins/login.html',{'page':page})

def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to home view after logout

@login_required
def user_profile(request):
    global levels
    global training_level_name
    global meal_name
    global work_name
    user_profile = UserProfile.objects.filter(user=request.user)

    current_weight = UserProfile.objects.filter(user=request.user).values_list('weight', flat = True)
    for cw in current_weight:
        print(cw)
    original_w = cw

    goal_weight = UserProfile.objects.filter(user=request.user).values_list('monthly_goals1', flat = True)
    for gw in goal_weight:
        print(gw)
    goal_w = float(gw)

    intensity = original_w - goal_w
    print (intensity)

    if intensity <= 10:
        levels = 'B'
        training_level_name = 'Beginner'
        meal_name = 'Mediterranean Plan'
        work_name ='5 Weeks to Your Best Body Ever'
        
    elif intensity > 11 and intensity <= 20:
        levels = 'I'
        training_level_name = 'Intermediate'
        meal_name = 'DASH Diet Plan'
        work_name ='Mass Building Hypertrophy Workout'
    elif intensity > 20:
        levels = 'A'
        training_level_name = 'Advanced'
        meal_name = 'Whole30 Plan'
        work_name ='12 Week Fat Destroyer: Complete Fat Loss'
    
    training_intensity = levels
    training_name = training_level_name
    recommended_workout_name = work_name
    recommended_meal_name = meal_name
    print(training_intensity)
    print(training_name)
    print(recommended_workout_name)
    print(recommended_meal_name)
    update_intensity = UserProfile.objects.filter(user=request.user).update(recommended_workout = recommended_workout_name, recommended_meal = recommended_meal_name, training_level = training_name)

    print(update_intensity)
    """workout_routine = UserProfile.objects.filter(user=request.user).values_list('training_level', flat = True)
    for results in workout_routine:
        print( results)
    stores = results"""


    current_date = datetime.now()
    today = current_date.strftime('%A')
    assign_meal = MealPlan.objects.filter(name = recommended_meal_name )
    assign_workout = WorkoutExercise.objects.filter(training_level = training_intensity)
    context = {'userp' : user_profile, 'usere' : assign_workout, 'userm': assign_meal, 'dayof': today }
    return render(request,'Logins/profile_dashboard.html', context) 

@login_required
def user_dashboard(request):
    global levels
    global training_level_name
    global meal_name
    global work_name
    user_profile = UserProfile.objects.filter(user=request.user)

    current_weight = UserProfile.objects.filter(user=request.user).values_list('weight', flat = True)
    for cw in current_weight:
        print(cw)
    original_w = cw

    goal_weight = UserProfile.objects.filter(user=request.user).values_list('monthly_goals1', flat = True)
    for gw in goal_weight:
        print(gw)
    goal_w = float(gw)

    intensity = original_w - goal_w
    print (intensity)

    if intensity <= 10:
        levels = 'B'
        training_level_name = 'Beginner'
        meal_name = 'Mediterranean Plan'
        work_name ='5 Weeks to Your Best Body Ever'
        
    elif intensity > 11 and intensity <= 20:
        levels = 'I'
        training_level_name = 'Intermediate'
        meal_name = 'DASH Diet Plan'
        work_name ='Mass Building Hypertrophy Workout'
    elif intensity > 20:
        levels = 'A'
        training_level_name = 'Advanced'
        meal_name = 'Whole30 Plan'
        work_name ='12 Week Fat Destroyer: Complete Fat Loss'
    
    training_intensity = levels
    training_name = training_level_name
    recommended_workout_name = work_name
    recommended_meal_name = meal_name
    print(training_intensity)
    print(training_name)
    print(recommended_workout_name)
    print(recommended_meal_name)
    update_intensity = UserProfile.objects.filter(user=request.user).update(recommended_workout = recommended_workout_name, recommended_meal = recommended_meal_name, training_level = training_name)

    print(update_intensity)
    """workout_routine = UserProfile.objects.filter(user=request.user).values_list('training_level', flat = True)
    for results in workout_routine:
        print( results)
    stores = results"""
    current_date = datetime.now()
    today = current_date.strftime('%A')
    assign_meal = MealPlan.objects.filter(name = recommended_meal_name )
    print(assign_meal)
    assign_workout = WorkoutExercise.objects.filter(training_level = training_intensity)
    context = {'userp' : user_profile, 'usere' : assign_workout, 'userm': assign_meal, 'dayof': today }
    return render(request,'Logins/side_navbar.html', context) 


@login_required
def user_workout_b(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = WorkoutExercise.objects.filter(training_level = 'B')
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,'dayof': today }
    return render(request, 'Logins/workout_dashboard_b.html', context)

@login_required
def user_workout_i(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = WorkoutExercise.objects.filter(training_level = 'I')
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,'dayof': today }
    return render(request, 'Logins/workout_dashboard_i.html', context)

@login_required
def user_workout_a(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = WorkoutExercise.objects.filter(training_level = 'A')
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,'dayof': today }
    return render(request, 'Logins/workout_dashboard_a.html', context)










@login_required
def user_meal_b(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = MealPlan.objects.filter(name = 'Mediterranean Plan')
    nutrients1 = Nutrition.objects.filter(name = 'Oatmeal')
    nutrients2= Nutrition.objects.filter(name = 'Chicken Salad')
    nutrients3= Nutrition.objects.filter(name = 'Beef Steak')
    print(projectObj)
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,  'nuts1':nutrients1,'nuts2':nutrients2,'nuts3':nutrients3, 'dayof': today }
    return render(request, 'Logins/meal_dashboard_b.html', context)

@login_required
def user_meal_i(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = MealPlan.objects.filter(name = 'DASH Diet Plan')
    nutrients1 = Nutrition.objects.filter(name = 'Quinoa Salad')
    nutrients2= Nutrition.objects.filter(name = 'Vegetable Curry')
    nutrients3= Nutrition.objects.filter(name = 'Salmon Fillet')
    #tags = projectObj.tags.all()
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,  'nuts1':nutrients1,'nuts2':nutrients2,'nuts3':nutrients3, 'dayof': today }
    return render(request, 'Logins/meal_dashboard_i.html', context)

@login_required
def user_meal_a(request):
    current_date = datetime.now()
    today = current_date.strftime('%A')
    projectObj = MealPlan.objects.filter(name = 'Whole30 Plan')
    nutrients1 = Nutrition.objects.filter(name = 'Scrambled Eggs and Avocado')
    nutrients2= Nutrition.objects.filter(name = 'Grilled Chicken and Veggies')
    nutrients3= Nutrition.objects.filter(name = 'Shrimp Pasta')
    #tags = projectObj.tags.all() Whole30 Plan
    #reviews = projectObj.review_set.all()
    context = {'project' : projectObj,  'nuts1':nutrients1,'nuts2':nutrients2,'nuts3':nutrients3, 'dayof': today }
    return render(request, 'Logins/meal_dashboard_a.html', context)

# def update_profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, instance=request.user.userprofile)
#         if form.is_valid():
#             form.save()
#             update_recommendations(request)
#             return redirect('some_page_after_updating')

#     else:
#         form = UserProfileForm(instance=request.user.userprofile)
    
#     return render(request, 'profile_update.html', {'form': form})


# def update_recommendations(request):
#     user_profile = UserProfile.objects.get(user=request.user)
#     recommended_mealplan, recommended_workout = user_profile.calculate_recommendations()
#     Recommendation.objects.create(
#         user_profile=user_profile,
#         recommended_meal=recommended_mealplan,
#         recommended_workout=recommended_workout,
#     )

