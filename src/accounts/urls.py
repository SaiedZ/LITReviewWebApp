from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views

urlpatterns = [
    path('', LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True,
        ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),
         name='logout'),
    path('signup/', views.signup_page, name='signup'),
]
