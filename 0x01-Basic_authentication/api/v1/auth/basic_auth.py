#!/usr/bin/env python3
"""The basic_auth module"""
from .auth import Auth
from flask import request


class BasicAuth(Auth):
    """Defines the BasicAuth class
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]
