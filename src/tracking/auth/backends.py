# encoding=utf-8

from tracking.models import Participant


class TokenBackend(object):

    def authenticate(self, token=None):
        if not token:
            return None

        user = None
        try:
            user = Participant.objects.get(login_token=token)
        except Participant.DoesNotExist:
            # FIXME: デモのため生成する
            user = Participant(login_token=token, username=token)
            user.save()

        return user

    def get_user(self, user_id):
        try:
            return Participant.objects.get(pk=user_id)
        except Participant.DoesNotExist:
            return None
