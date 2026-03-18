from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
import json
from .models import Poll, PollResponse,EventPolls,school_opinion_poll,PollQuestion
from django.http import JsonResponse


# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            # Pass error to template
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    
    return render(request, 'login.html')


# register page
def register_view(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
# Check if passwords match
        if password != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

 # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

 # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.first_name = full_name
        user.save()

        return render(request, 'register.html', {'success': 'Account created successfully! You can now login.'})
    return render(request, 'register.html')


# home page
def home_view(request):
    # Count polls per category
    academic_count = Poll.objects.filter(category='academic').count()
    events_count = Poll.objects.filter(category='events').count()
    opinion_count = Poll.objects.filter(category='opinion').count()

    # Pass counts as JSON for JavaScript
    category_counts = {
        'academic': academic_count,
        'events': events_count,
        'opinion': opinion_count
    }
    context = {
        'category_counts_json': json.dumps(category_counts)
    }

    return render(request, 'homeee.html', context)



# academic page
def academic_subjects_view(request):
    questions = PollQuestion.objects.filter(category='academic_subject')
    return render(request, 'academic_subject.html', {'questions': questions})

def submit_academic_poll(request):
    if request.method == "POST":
        # Save responses to database
        for key, value in request.POST.items():
            if key.startswith('q'):
                PollResponse.objects.create(
                    user=request.user,
                    question=key,
                    answer=value,
                    category='academic'
                )
        return JsonResponse({"status": "success"})
        



# event page
def events_view(request):
    questions = PollQuestion.objects.filter(category='event')
    return render(request, 'event.html', {'questions': questions})

def submit_event_poll(request):
    if request.method == "POST":
        # Save responses to database
        for key, value in request.POST.items():
            if key.startswith('q'):
                EventPolls.objects.create(
                    user=request.user,
                    question=key,
                    answer=value,
                    category='event'
                )
        return JsonResponse({"status": "success"}) 
    return JsonResponse({"status": "error"})  


# school opinion page
def school_opinion_view(request):
    questions = PollQuestion.objects.filter(category='school_opinion')
    return render(request, 'school_opinion.html', {'questions': questions})

def submit_school_opinion_poll(request):
    if request.method == "POST":
        for key, value in request.POST.items():
            if key.startswith('q'):
                school_opinion_poll.objects.create(
                    user=request.user,
                    question=key,
                    answer=value,
                    category='opinion'
                )
        return JsonResponse({"status": "success"}) 
    return JsonResponse({"status": "error"})  


#  logout 
def logout_view(request):
    logout(request)
    return redirect('login')


