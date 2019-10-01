from django.urls import path
from . import views

app_name= "accounts"

urlpatterns = [
    # social login
    path("profile/", views.social_login, name="login_check"),
]
