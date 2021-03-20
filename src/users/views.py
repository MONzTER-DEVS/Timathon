from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
def register(request):
    if request.method == "GET":
        return render(request, "users/signup.html")
    else:
        username = request.POST["username"]
        name = request.POST["name"]
        password = request.POST["password"]
        password2 = request.POST["confirm_password"]

        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "users/signup.html")

        if len(User.objects.filter(username=username)) > 0:
            messages.error(request, "username is taken")
            return render(request, "users/signup.html")

        user = User.objects.create_user(username=username, password=password, first_name=name)
        user.save()
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)

        return redirect("home:index")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))