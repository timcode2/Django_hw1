from django.urls import path

from users.apps import UsersConfig
from users.views import LoginView, LogoutView, RegisterView, UserUpdateView, generate_new_password, \
    EmailConfirmationSentView, EmailConfirmView, UserConfirmEmailView

app_name = UsersConfig.name


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('email_confirm/<str:token>/', UserConfirmEmailView.as_view(), name='email_confirm'),
    path('email-sent/', EmailConfirmationSentView.as_view(), name='email_sent'),
    path('email_verified/', EmailConfirmView.as_view(), name='email_verified')
]