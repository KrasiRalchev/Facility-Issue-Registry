from django.urls import path

from accounts.views import RegisterView, LoginPageView, LogoutPageView, ProfileDetailView

app_name = 'accounts'

urlpatterns = [
    path('', LoginPageView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('profile/<int:id>/', ProfileDetailView.as_view(), name='profile')
]