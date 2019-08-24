#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: binary -*-

from core.libs.paint import color

class notifications(object):

    # Notification variables
    INFO = color.W + '[INFO]' + color.N + ": "
    ERROR = color.R + '[ERROR]' + color.N + ": "
    FAIL = color.R + '[FAIL]' + color.N + ": "
    FOUND = color.W + '[FOUND]' + color.N + ": "
    STATUS = color.Y + "[RESULTS]" + color.N + ": "
