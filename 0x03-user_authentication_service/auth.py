#!/usr/bin/env python3
"""The auth module"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """Generates a salted hash of a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
