"""
.. module:: project.apps.user_login.views
   synopsis: Views.
"""
# from django.shortcuts import render
import logging
from celery import group
from django.http import HttpResponse
from project.apps.user_login.tasks import (
    check_device,
    notify_user,
    save_event,
    post_to_api,
    process_response
)


LOGGER = logging.getLogger(__name__)


# Create your views here.
def process_login(request):
    """Process Login."""
    res = (
        check_device.s(username="username", login_data_id=123) |
        group(
            notify_user.s(username="username"),
            save_event.s(username="username")
        ) |
        post_to_api.s() |
        process_response.s()
    ).apply_async()
    return HttpResponse(
        f"<html>"
        "    <body>"
        "        <h1>res: {res}</h1>"
        "    </body>"
        "</html>"
    )
