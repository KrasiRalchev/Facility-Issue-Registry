from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import RegisterForm


class HomePageView(LoginView):
    template_name = 'home.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('facilities:facility-dashboard')


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('facilities:facility-dashboard')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response



