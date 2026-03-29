from django.urls import path

from accounts.views import RegisterUserView, LoginUserView, LogoutUserView, ProfileUserView, ProfileEditView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),
    path('profile/<int:pk>/', ProfileUserView.as_view(), name='profile'),
    path('profile/edit/<int:pk>', ProfileEditView.as_view(), name='profile-edit'),

]