# views.py

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, VotingForm
from .models import Question, Option, Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)  # This line logs the user in
                return redirect('voting')  # Redirect to voting page after login
            else:
                # Handle invalid login credentials
                # You might want to display an error message
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def voting(request):
    questions = Question.objects.all()  # Fetch all questions from the database
    submitted_options = Vote.objects.filter(user=request.user).values_list('option_id', flat=True)
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])  # Extract the question ID from the key
                option_id = int(value)  # Extract the option ID from the form data
                question = Question.objects.get(pk=question_id)  # Retrieve the question
                option = Option.objects.get(pk=option_id)  # Retrieve the selected option
                Vote.objects.create(user=request.user, option=option, question=question)  # Create a new vote
                messages.success(request, 'Your vote has been recorded.')
                return redirect('voting')  # Redirect after successfully voting
    else:
        form = VotingForm()
    return render(request, 'voting.html', {'questions': questions, 'submitted_options': submitted_options,'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')