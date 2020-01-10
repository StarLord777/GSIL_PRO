# -*- coding: utf-8 -*-

"""
    notification
    ~~~~~~~~~~~~

    Implements notification(mail)

    :author:    Feei <feei@feei.cn>
    :homepage:  https://github.com/FeeiCN/gsil
    :license:   GPL, see LICENSE for more details.
    :copyright: Copyright (c) 2018 Feei. All rights reserved
"""
import random
import smtplib
import traceback
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import get
from .log import logger


class Notification(object):
    def __init__(self, subject, to=None, cc=None):
        """
        Initialize notification class
        :param subject:
        :param to:
        """
        self.subject = subject
        if to is None:
            self.to = get('mail', 'to')
        else:
            self.to = to
        if cc is None:
            self.cc = get('mail', 'cc')
        else:
            self.cc = cc

    def notification(self, html):
        """
        Send notification use by mail
        :param html:
        :return:
        """
        text = html
        filepath = "/root/"+str(self.subject)+".html"
        with open(filepath,'w') as f:
	        f.write(text)
	        f.close()
