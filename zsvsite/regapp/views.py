from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CustomUserForm


# Create your views here.


# Отображение базового шаблона
class BaseView(TemplateView):
    template_name = "regapp/base.html"


class RegisteredView(TemplateView):
    template_name = "regapp/registered.html"


# Регистрация нового пользователя
class RegisterView(CreateView):
    form_class = CustomUserForm
    template_name = "regapp/reg-page.html"
    success_url = reverse_lazy("regapp:registered")

    # Авторизация пользователя, после его регистрации
    def form_valid(self, form):
        response = super().form_valid(form)

        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password1")
        user = authenticate(
            self.request,
            username=username,
            password=password,
        )
        login(request=self.request, user=user)

        return response


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "regapp/autorisation.html"

    def get_success_url(self):
        return reverse_lazy("regapp:registered")

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy("regapp:base-page")