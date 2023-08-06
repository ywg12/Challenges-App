from django.urls import path
from . import views

#url config
urlpatterns = [
    path("",views.index), #for /challenges
    path("<int:month>", views.monthly_challenge_by_num),
    path("<str:month>", views.monthly_challenge, name="month-challenge")
]