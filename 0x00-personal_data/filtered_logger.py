#!/usr/bin/env python3
"""The filtered_logger module"""
import re


def filter_datum(fields, redaction, message, separator):
    """Returns an obfuscated log message"""
    for field in fields:
        message = re.sub(field + "=.*?" + separator,
                         field + "=" + redaction + separator, message)
    return message
