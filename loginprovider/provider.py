from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class LoginTestingProvider(OAuth2Provider):
    id = 'logintesting'
    name = 'Login Testing'
    account_class = ProviderAccount

    def extract_uid(self, data):
        print("extract_uid", repr(data))
        return "%s_%s" % (str(data.get('team').get('id')),
            str(data.get('user').get('id')))

    def extract_common_fields(self, data):
        print("extract_common_fields", repr(data))
        return dict(name=data.get('name'),
            email=data.get('user').get('email', None))

    def get_default_scope(self):
        return ['read', 'write']


providers.registry.register(LoginTestingProvider)
