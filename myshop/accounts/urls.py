from django.urls import path
from . import views
from accounts.views import logout

urlpatterns = [
    path("register", views.register, name="register"),
    path("accounts/register", views.register, name="accounts_register"),
    path('logout/', logout, name='logout'),
]
