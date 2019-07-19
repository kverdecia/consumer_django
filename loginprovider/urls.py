from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from .provider import LoginTestingProvider

urlpatterns = default_urlpatterns(LoginTestingProvider)
