#!/usr/bin/env python
from __future__ import absolute_import, unicode_literals

import os
import sys
import socket, re

if __name__ == "__main__":
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    if re.match("^192\.168.*$",ip):
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
    else:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
