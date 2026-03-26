from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView
from accounts.forms import RegisterForm, ProfileEditForm
from accounts.models import Profile


class LoginUserView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('facilities:dashboard')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('accounts:login')


class RegisterUserView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('facilities:dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileUserView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/user_profile.html'
    context_object_name = 'profile'


class ProfileEditView(UpdateView):
    model = Profile
    template_name = 'accounts/profile_edit.html'
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse('accounts:profile', kwargs={'pk': self.object.pk})





