#!/usr/bin/env python3
"""The auth module"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Defines the Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks if a route requires authentication
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        # Allow wildcard matching for excluded_paths
        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                if path.startswith(excluded_path[:-1]):
                    return False

        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns the value of the authorization header
        """
        if request is None or request.headers.get('Authorization') is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user
        """
        return None
