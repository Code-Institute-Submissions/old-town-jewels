from django.urls import Path
from . import views
urlpatterns = [path("register", views.register, name="register")
               ]
