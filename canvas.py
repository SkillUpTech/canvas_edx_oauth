"""
Canvas OAuth2 backend, docs at:
    https://bcconted.instructure.com/login/oauth2/auth
"""
from .oauth import BaseOAuth2


class CanvasOAuth2(BaseOAuth2):
    """Canvas OAuth2 authentication backend"""
    name = 'canvas-oauth2'
    AUTHORIZATION_URL = 'https://bcconted.instructure.com/login/oauth2/auth'
    ACCESS_TOKEN_URL = 'https://bcconted.instructure.com/login/oauth2/token'
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('refresh_token', 'refresh_token', True),
        ('expires_in', 'expires'),
    ]

    def _get_username_from_response(self, response):
        user = response.get('user', {})
        return user.get('name')


    def get_user_details(self, response):
        """Return user details from Canvas account"""
         
        return {'username': self._get_username_from_response(response),
                'email': response.get('primary_email'),
                'first_name': response.get('short_name')
               }

    def get_user_id(self, details, response):
        return response['user']['id']

    def user_data(self, access_token, *args, **kwargs):
        """Grab user profile information from Canvas instance."""
        userid = kwargs['response']['user']['id']
        return self.get_json(
            'https://bcconted.instructure.com/api/v1/users/%s/profile' % userid,
            headers={'Authorization': 'Bearer %s' % access_token}
        )

