from django.conf import settings
from datetime import datetime

class UserSession(object):
    '''
    classdocs:
    '''
    def __init__(self, request):
        '''
        initialize the session
        '''
        self.session = request.session
        user_session = self.session.get(settings.USER_SESSION_ID)
        if not user_session:
            user_session = self.session[settings.USER_SESSION_ID] = {}
        self.user_session = user_session
    
    def add(self, user):
        self.user_session['user'] = user
        self.save()

    def clear(self):
        self.user_session = {}
        self.session[settings.USER_SESSION_ID] = {}
        self.save()
    
    def save(self):
        self.session[settings.USER_SESSION_ID] = self.user_session
        self.session.modified = True

    def __iter__(self):
        for item in self.session.values():
            yield item