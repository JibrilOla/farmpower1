from django.urls import path, include

# Create your tests here.
from .views import *

app_name = "registration"

urlpatterns = [
    path("register/<str:ref_code>/", Register, name="register"),
    path("team/", my_recommendations_view, name="team"),
    path("login/", Login, name="login"),
    path("dashboard/", Dashboard, name="dashboard"),
]
