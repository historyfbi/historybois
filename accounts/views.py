from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth import logout
from . import forms

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('accounts:login'))


class SignUpView(CreateView):
    form_class = forms.SignUp
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'

    def get(self, *args, **kwargs):

        if self.request.user.is_authenticated:
            return redirect("/accounts/profile/")
        else:
            return super().get(*args, **kwargs)

class ProfileView(View):

    def get(self, request):
        return redirect("/")
