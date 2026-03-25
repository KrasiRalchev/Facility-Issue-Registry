from django.urls import path

from accounts.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileUserView

app_name = 'accounts'

urlpatterns = [
    path('', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileUserView.as_view(), name='profile')
]