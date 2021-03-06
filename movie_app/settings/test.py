"""
This is an example settings/test.py file.
Use this settings file when running tests.
These settings overrides what's in settings/base.py
"""

from .base import *


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    },
}

SECRET_KEY = 'm$2x(c2c^@&jq&wl!^3!kk4+ke!rz-e&hz%7a1hhgijh!vf!aq'
