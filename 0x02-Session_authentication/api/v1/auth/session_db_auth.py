#!/usr/bin/env python3
"""The session_db_auth module"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """The SessionDBAuth class inherits from SessionExpAuth
    """
    def create_session(self, user_id: str = None) -> str:
        """Creates and stores a new instance of UserSession

        Args:
            user_id (str, optional): The user ID. Defaults to None.

        Returns:
            str: The Session ID
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        new_user_session = UserSession(user_id=user_id, session_id=session_id)
        new_user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID

        Args:
            session_id (str, optional): The Session ID. Defaults to None.

        Returns:
            str: The User ID
        """
        if session_id is None:
            return None
        user_session = UserSession.search({'session_id': session_id})
        if len(user_session) == 0:
            return None
        
        user_session = user_session[0]
        if self.session_duration <= 0:
            return user_session.user_id
        if user_session.created_at + timedelta(seconds=self.session_duration) \
                < datetime.now():
            return None
        return user_session.user_id

    def destroy_session(self, request=None) -> bool:
        """Deletes the user session / logout

        Args:
            request (Request, optional): The request object. Defaults to None.

        Returns:
            bool: True if successful, False otherwise
        """
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        user_session = UserSession.search({'session_id': session_id})
        if len(user_session) == 0:
            return False
        user_session = user_session[0]
        user_session.remove()
        return True
