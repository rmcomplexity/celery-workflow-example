"""
.. module:: project.tasks
   synopsis: Celery tasks.
"""
import logging
from celery import shared_task
from project.apps.user_login.models import user_login_data


LOGGER = logging.getLogger(__name__)


@shared_task(bind=True)
def check_device(self, username, login_data_id):
    """Check if device is new for user.

    :param str username: Username.
    :param int login_data_id: Data id.
    """
    LOGGER.debug('check_device id: %s', self.request.id)
    login_data = user_login_data(username, login_data_id)
    return login_data


@shared_task(bind=True)
def notify_user(self, login_data, username):
    """Notify user.

    :param dict login_data: Login Data.
    :param dict username: Username.
    """
    LOGGER.debug(
        "notify_user id: %s\n"
        "username: %s",
        self.request.id,
        username
    )
    is_new = login_data.get('is_new')
    if is_new:
        LOGGER.debug("Notifying user.")
    return {"user_notified": is_new}


@shared_task(bind=True)
def save_event(self, login_data, username):
    """Save data.

    :param dict login_data: Login Data.
    :param dict username: Username.
    """
    LOGGER.debug(
        "save_event id: %s \n"
        "username: %s",
        self.request.id,
        username
    )
    LOGGER.debug("Saving data.: %s", login_data)
    return {"Data saved": True}


@shared_task(bind=True)
def post_to_api(self, data):
    """Post to external api.

    :param dict data: Data
    """
    LOGGER.debug(
        "post_to_api id: %s\n"
        "data: %s",
        self.request.id,
        data
    )
    _data = {}
    for response in data:
        _data = {**_data, **response}
    LOGGER.debug("Posting to eternal API: %s", _data)
    return {
        "response":
        {
            "data": "some data"
        }
    }


@shared_task(bind=True)
def process_response(self, data):
    """Process response.

    :param dict data: Data.
    """
    LOGGER.debug(
        "process_response id: %s\n"
        "data: %s",
        self.request.id,
        data
    )
    LOGGER.debug("Processing response.")
    return True
