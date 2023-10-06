import random
import secrets

from django.conf import settings
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserForm
from users.models import User


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:email_verify')
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        token = secrets.token_urlsafe(nbytes=16)

        user.token = token

        url = reverse_lazy('users:email_confirm', kwargs={'token': user.token})
        send_mail(
            subject='Подтверждение регистрации',
            message=f'Для подтверждения регистрации перейдите по ссылке: http://127.0.0.1:8000/{url}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email],
            fail_silently=False
        )
        user.save()

        return redirect('users:login')


def verify(request, token):
    user = User.objects.get(token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect('users:login')


class UserUpdateView(UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self):
        return self.request.user


def generate_new_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы успешно поменяли пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:home'))
