from django.shortcuts import render,HttpResponseRedirect,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate



def user_register(request):

    if request.method == "POST":

        username = request.POST.get("registerUsername")
        email = request.POST.get("registerEmail")
        password = request.POST.get("registerPassword")

        user = User.objects.create(username=username,email=email)
        user.set_password(password)
        user.save()

        return HttpResponseRedirect("/")

    return render(request,"accounts/register.html")

def user_login(request):

    if request.method == "POST":

        username = request.POST.get("loginUsername")
        password = request.POST.get("loginPassword")

        user = authenticate(request, username=username, password=password)

        if user:

            login(request,user)

            return HttpResponseRedirect("/")

    return render(request,"accounts/login.html")

def user_logout(request):

    logout(request)

    return redirect("user-login")


