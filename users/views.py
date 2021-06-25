from django.shortcuts import render
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django import forms as d_forms
from . import models, forms


class UserProfileView(LoginRequiredMixin, DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    model = models.User
    template_name = "users/update-profile.html"
    success_message = "Профиль обновлён."

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_class(self):
        if self.request.user.guide:
            return forms.UpdateGuideProfileForm
        else:
            return forms.UpdateUserProfileForm

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        if not self.request.user.guide:
            form.fields["first_name"].widget.attrs = {"placeholder": "Имя", "class": "update-input"}
            form.fields["last_name"].widget.attrs = {"placeholder": "Фамилия", "class": "update-input"}
        else:
            form.fields["first_name"].widget.attrs = {"placeholder": "Имя", "class": "update-input"}
            form.fields["last_name"].widget.attrs = {"placeholder": "Фамилия", "class": "update-input"}
            form.fields["bio"].widget.attrs = {"placeholder": "О себе", "class": "update-input"}
            form.fields["phone"].widget.attrs = {"placeholder": "Телефон: +79780000000", "class": "update-input"}
        return form
