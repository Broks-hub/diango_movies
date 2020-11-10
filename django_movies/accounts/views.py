from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .forms import SubmittableAuthenticationForm, SubmittablePasswordChangeForm, SignUpForm
from django.urls import reverse_lazy


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('index')


class SubmittableLoginView(LoginView):
    form_class = SubmittableAuthenticationForm
    template_name = 'form.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    form_class = SubmittablePasswordChangeForm
    template_name = 'form.html'
    success_url = reverse_lazy('index')


class SuccessMessageLogoutView(LogoutView):
    def get_next_page(self):
        result = super().get_next_page()
        messages.success(self.request, 'Successfully logged out!')
        return result
