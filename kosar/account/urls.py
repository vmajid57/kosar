from django.urls import path
from .views import *  # Import the view here
from django.contrib.auth import views as auth_views
from account.views import CustomLoginView
from account.forms import LoginForm


urlpatterns = [
    path('', home, name='account-home'),
    # redirect_authenticated_user=True means that users who try to access the login page after
    # they are authenticated will be redirected back.
    path('register/', RegisterView.as_view(), name='account-register'),
    path('login/', CustomLoginView.as_view(template_name='account/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('profile/', profile, name='account-profile'),
]
