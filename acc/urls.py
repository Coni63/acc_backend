"""acc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    # application endpoints
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('fuel/', include('fuel.urls')),
    path('ratings/', include('ratings.urls')),

    # rest_framework_jwt endpoints
    # path('auth/api-token-auth/', obtain_jwt_token),  # not required as it is provided with django-rest-auth login
    path('auth/api-token-refresh/', refresh_jwt_token),
    path('auth/api-token-verify/', verify_jwt_token),

    # authentication endpoints
    # refer to https://django-rest-auth.readthedocs.io/en/latest/api_endpoints.html for endpoints
    path('auth/', include('rest_auth.urls')),  
    path('auth/registration/', include('rest_auth.registration.urls')),

    # endpoints for email verification
    # https://stackoverflow.com/questions/48390749/reverse-for-account-email-verification-sent-not-found-account-email-verifica
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^auth/account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(), name='account_confirm_email'),
]
