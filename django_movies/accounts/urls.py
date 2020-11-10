from django.urls import path
from accounts.views import SubmittableLoginView, SuccessMessageLogoutView, SubmittablePasswordChangeView, SignUpView


app_name = 'accounts'
urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', SuccessMessageLogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password_change'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
