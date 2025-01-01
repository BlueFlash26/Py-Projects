from django.urls import path
from . import views

app_name="Products"

urlpatterns = [
    path('new/', views.newproducts),
    path('redir/', views.redirect),
    path('<str:name>/', views.product),
    path('', views.products, name='single'),
]