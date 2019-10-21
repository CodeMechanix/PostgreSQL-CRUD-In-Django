from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls', namespace='users')),
]
