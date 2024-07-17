# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ... other URL patterns ...
    path('register', views.register, name='register'),
    path('', views.user_login, name='user_login'),
    # path('chart', views.chat, name='chat'),
    path("chatpage", views.chatPage, name="chatpage"),
    path('logout', views.logout_user, name='logout-user'),
    path('otpcheck' ,views.otpcheck, name='otpcheck'),
    ##reset Password
    path('forgot_password/', auth_views.PasswordResetView.as_view(template_name='forgot_password.html'), name='forgot_password'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
    
    

