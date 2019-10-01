from django.shortcuts import render, get_object_or_404
from accounts.models import User

# django 기본 login
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

# Create your views here.
def social_login(request):
    # print(request)
    # print(request.user)
    # print(request.user.username)

    return render(request, "api/base.html")