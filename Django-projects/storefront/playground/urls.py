from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.say_hello),
    path('guess-game/<slug:guess>', views.GuessView.as_view()),
    path('guess-game/', views.GuessView.as_view()),
]