from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register', views.registreration, name='register'),
    path('log_in', views.log_in, name='log_in'),  # experimental
    path('log_out', views.log_out, name='log_out'),
# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
#     path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),
#     path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
#     path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
#     path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
#     path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
#     path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]

# path('reg-exp', views.reg_exp),