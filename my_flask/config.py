# -*- coding: utf-8 -*-

# Copyright (c) 2022. All rights reserved.

"""
@author: wenjie
@file: config.py
@time: 2022/5/20 11:38
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""


class Config:
    # JWT
    JWT_SECRET = 'TPmi4aLWRbyVq8zu9v82dWYW17/z+UvRnYTt4P6fAXA'
    JWT_EXPIRY_HOURS = 2
    JWT_REFRESH_DAYS = 14


print(len(Config.JWT_SECRET))
