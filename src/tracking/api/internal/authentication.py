# coding=utf-8

from django.conf import settings
from rest_framework import authentication
from rest_framework import exceptions


class InternalAPIUser(object):

    def is_authenticated(self):
        return True


class InternalAPIKeyAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        api_key = request.META.get('HTTP_X_API_KEY')
        if api_key != settings.INTERNAL_API_KEY:
            return None
        return (InternalAPIUser(), None)
