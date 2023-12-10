from django.urls import path, include
from . import views as user_view
from django.contrib.auth import views as auth_views
from . import forms
from . import views
urlpatterns = [
      path('register/', user_view.register, name='user-register'),
      path('profile/', user_view.profile, name='user-profile'),
      path('profile/update/', user_view.profile_update, name='user-profile-update'),
      path('phone/update/', user_view.phone_update, name='user-phone-update'),
      path('phone/delete/<int:phone>/', user_view.remove_phone, name='user-phone-delete'),



      # login and logout url with its forms if exists...
      path('', auth_views.LoginView.as_view(template_name='accounts/login.html', 
      authentication_form=forms.UserLoginForm), name='user-login'),

      path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
      name='user-logout'),


      # To change your password using the ordinal way...
      # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
      # name='password_change'),

      # To change your password using the updated ChangePasswordForm in django auth
      path('password_change/', views.CustomPasswordChangeView.as_view(template_name='accounts/password_change.html', form_class=forms.CustomPasswordChangeForm), 
      name='password_change'),


      # To reset your password if you forget...
      # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', form_class=forms.ResetPasswordForm),
      # name='password_reset'),


      path('password_reset/', views.CustomPasswordResetView.as_view(template_name='accounts/password_reset.html', form_class=forms.CustomPasswordResetForm),
      name='password_reset'),



      path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
      name='password_reset_confirm'),

      path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
      name='password_reset_done'),

      path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
      name='password_reset_complete'),

]