from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='login'),
    path('search/', views.search, name='search'),
    path('auth/', views.auth, name='auth')
]