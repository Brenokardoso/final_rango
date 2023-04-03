from django.urls import path,include
from .views import home,registration_view

urlpatterns = [
    path('',home),
    path('login',registration_view)

]