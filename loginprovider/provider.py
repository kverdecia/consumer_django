from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class LoginTestingProvider(OAuth2Provider):
    id = 'logintesting'
    name = 'Login Testing'
    account_class = ProviderAccount

    def extract_uid(self, data):
        return data.get('user').get('id')

    def extract_common_fields(self, data):
        return data.get('user')

    def get_default_scope(self):
        return ['read', 'write']


providers.registry.register(LoginTestingProvider)
