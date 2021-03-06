from django.shortcuts import render

import requests

from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter,
    OAuth2LoginView, OAuth2CallbackView)
from allauth.socialaccount.providers.oauth2.client import OAuth2Error

from .provider import LoginTestingProvider


class LoginTestingOAuth2Adapter(OAuth2Adapter):
    provider_id = LoginTestingProvider.id

    access_token_url = 'http://localhost:8000/oauth2/token/'
    authorize_url = 'http://localhost:8000/oauth2/authorize/'
    identity_url = 'http://localhost:8000/identity/'

    supports_state = True

    def complete_login(self, request, app, token, **kwargs):
        extra_data = self.get_data(token.token)
        return self.get_provider().sociallogin_from_response(request,
            extra_data)

    def get_data(self, token):
        resp = requests.get(
            self.identity_url,
            headers={'Authorization': 'Bearer {}'.format(token)}
        )
        resp = resp.json()
        if not resp.get('ok'):
            raise OAuth2Error()
        info = {
            'user': resp.get('user'),
        }
        return info


oauth2_login = OAuth2LoginView.adapter_view(LoginTestingOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(LoginTestingOAuth2Adapter)