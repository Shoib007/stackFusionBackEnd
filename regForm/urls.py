from django.urls import path, include
from .views import saveData

urlpatterns = [
    path('register', saveData, name="Save Data"),
]
