# -*- coding: utf-8 -*-

# Copyright (c) 2022. All rights reserved.

"""
@author: wenjie
@file: id_worker.py
@time: 2022/5/21 10:48
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

import snowflake.client


def get_id(): return snowflake.client.get_guid()
