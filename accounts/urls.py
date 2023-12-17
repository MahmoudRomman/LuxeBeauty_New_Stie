from django.urls import path, include
from . import views as user_view
from django.contrib.auth import views as auth_views
from . import forms


urlpatterns = [
      path('register/', user_view.register, name='user-register'),
      path('profile/', user_view.profile, name='user-profile'),
      path('profile/update/', user_view.profile_update, name='user-profile-update'),
      path('phone/update/', user_view.phone_update, name='user-phone-update'),
      path('phone/delete/<int:phone>/', user_view.remove_phone, name='user-phone-delete'),



      # login and logout url with its forms if exists...
      path('', auth_views.LoginView.as_view(template_name='accounts/login.html', 
      authentication_form=forms.UserLoginForm), name='user-login'),

      # path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),
      # name='user-logout'),


      # here i use the custom logoutview which i inherit and override it from the logoutview in django auth
      # and i make this to prevent the user to back and enter the content of the website after he logged out
      path('logout/', user_view.CustomLogoutView.as_view(template_name='accounts/logout.html'),
      name='user-logout'),



      # To change your password using the ordinal way...
      # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change.html'), 
      # name='password_change'),

      # To change your password using the updated ChangePasswordForm in django auth
      path('password_change/', user_view.CustomPasswordChangeView.as_view(template_name='accounts/password_change.html'), 
      name='password_change'),


      path('password_change_complete/', user_view.password_change_complete, name='password_change_complete'),


      # To reset your password if you forget...
      path('password_reset/', user_view.CustomPasswordResetView.as_view(template_name='accounts/password_reset.html', form_class=forms.CustomPasswordResetForm),
      name='password_reset'),


      # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
      # name='password_reset'),



      path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
      name='password_reset_confirm'),

      path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'),
      name='password_reset_done'),

      path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
      name='password_reset_complete'),

]