#!/usr/bin/env python3
"""The session_exp_auth module"""
from .session_auth import SessionAuth
from datetime import datetime, timedelta
from os import getenv


class SessionExpAuth(SessionAuth):
    """Defines the SessionExpAuth class
    """
    def __init__(self):
        """Constructor method"""
        try:
            self.session_duration = int(getenv("SESSION_DURATION"))
        except Exception:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a user_id
        """
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.user_id_by_session_id[session_id] = {"user_id": user_id,
                                                  "created_at": datetime.now()}
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Returns a User ID based on a Session ID
        """
        if session_id is None:
            return None
        session_dictionary = self.user_id_by_session_id.get(session_id)
        if session_dictionary is None:
            return None
        if self.session_duration <= 0:
            return session_dictionary.get("user_id")

        if session_dictionary.get("created_at") is None:
            return None
        if session_dictionary.get("created_at") \
                + timedelta(seconds=self.session_duration) < datetime.now():
            return None
        return session_dictionary.get("user_id")
