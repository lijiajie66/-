# -*- coding: utf-8 -*-

# Copyright (c) 2022. All rights reserved.

"""
@author: wenjie
@file: middlewares.py
@time: 2022/5/20 14:16
@desc:

Supported platforms:

 - Linux
 - Windows

Works with Python versions 3.X.
"""

from flask import request, current_app, g, abort

from util.jwt_util import verify_jwt


def jwt_authentication():
    pass
    """主要校验接口传递过来的token是否有效"""
    if not request.path.startswith('/app/v1_0/sms/codes/') and \
            not request.path.startswith('/app/v1_0/authorizations'):
        token = request.headers.get('Authorization', '')
        if not token:
            abort(403)
        if not token.startswith('Bearer '):
            abort(403)
        token = token.split('Bearer ')[1]
        payload = verify_jwt(token=token, secret=current_app.config['JWT_SECRET'])
        if not payload:
            abort(403)
        g.user_id = payload.get('user_id')
