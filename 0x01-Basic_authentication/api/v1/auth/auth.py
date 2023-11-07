#!/usr/bin/env python3
"""The auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Defines the Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if path requires authentication
        """
        return False

    def authorization_header(self, request=None) -> str:
        """Returns the value of the authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user
        """
        return None
