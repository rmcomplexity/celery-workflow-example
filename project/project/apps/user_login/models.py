"""
.. module:: project.apps.user_login.models
   synposis: Model stuff
"""


# Create your models here.
def user_login_data(username, data_id):
    """Return user login data.

    :param int data_id: Data id
    """
    return {
        'username': username,
        'data': {
            'id': data_id,
            'device': 'device_name',
            'is_new': True
        }
    }
