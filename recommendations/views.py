from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Recommendation
from Logins.models import UserProfile

@login_required
def recommendation_view(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recommendation = Recommendation.objects.filter(user_profile=user_profile).first()
    return render(request, 'recommendations.html', {'recommendation': recommendation})
