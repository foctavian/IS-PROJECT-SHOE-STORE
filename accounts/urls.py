from django.urls import path

from .views.homepage import HomePage
from .views.login import logout, login
from .views.user_config import account, settings
from .views.validator import send_email_for_settings_change_approval,validate_settings_change_request

urlpatterns = [
    path('', HomePage.as_view(), name="home", ),
    path('login/', login, name="login",),
    path('logout', logout, name='logout',),
    path('account/<int:user_id>', account, name='account'),
    path('account/user-settings/set=<str:setting>/<int:user_id>', settings, name='settings'),
    path('account/user-settings/validate-email/<int:user_id>', send_email_for_settings_change_approval, name='validate-email'),
    path('account/user-settings/validate-email/<int:key>',validate_settings_change_request, name='validate-email-key'),
]
