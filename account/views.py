from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def account(request):
    return render(request, 'account/account.html')

def signup(request):
    if (request.method == "POST"):
        #user has info and wants sign up
        if (request.POST['password1'] == request.POST['password2']):
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'account/signup.html', {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request, user)
                return redirect('homepage')
        else:
            return render(request, 'account/signup.html', {'error':'Passwords must match' })
    else:    
        #user wants enter inf
        return render(request, 'account/signup.html')
def login(request):
    if(request.method == 'POST'):
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if(user is not None):
           auth.login(request, user)
           return redirect('homepage') 
        else:
            return render(request, 'account/login.html', {'error': "Username or password is invalid."})
    else:
        return render(request, 'account/login.html')
def logout(request):
    # TODO Need to route to homepage
    if (request.method =='POST'):
        
        auth.logout(request)
        return redirect('homepage')