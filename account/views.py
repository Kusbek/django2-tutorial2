from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'account/account.html')

def signup(request):
    return render(request, 'account/account.html')
def login(request):
    return render(request, 'account/account.html')