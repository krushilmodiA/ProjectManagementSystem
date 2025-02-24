from django.shortcuts import render,redirect
from .models import User

# for login authentication check
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
# Create your views here.

# this is a login function
def login(request):
    if request.method == "POST":
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        #check login authentication of using in-build authenticate method. 
        if email and password:
            user = authenticate(request, email = email, password = password)
            
            if user is not None:
                auth_login(request, user)

                print("User:", user)

                print(request.user)
                print(request.user.is_authenticated)

                return redirect('/')
             
    return render(request, 'account/login.html')

# this is Logout function.
def logout(request):
         
         auth_logout(request)
         return redirect('/login/')           

# this is a signup function
def signup(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')

        if name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)

            print("User created:", user)

            return redirect('/login/')
        else:
            print("something went wrong!!!") 

    else:
        print("show the form")
    return render(request, 'account/signup.html')