from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import UserLogin
from django.contrib.auth import login, authenticate

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("successful-login")

    context = {
        "form": form,
    }

    return render(request, "login.html", context)



def logout_view(request):
    logout(request)
    return redirect("success-page")