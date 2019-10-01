from django.urls import path
from . import views

# jwt
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token

app_name= "winery"

urlpatterns = [
    # jwt
    path("token/create/", obtain_jwt_token),
    path("token/verify/", verify_jwt_token),
    path("token/refresh/", refresh_jwt_token),

    # wine api
    path("wines/", views.wines, name="winery_wines"),
    path("", views.test, name="winery_test")
]
