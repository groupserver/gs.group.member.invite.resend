# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals
from zope.schema import ASCIILine, Text, TextLine
from zope.interface.interface import Interface


class IGSResendInvitation(Interface):
    userId = ASCIILine(title='User Identifier',
      description='The user ID of the person receiving the '
          'invitation.',
      required=True)
    subject = TextLine(title='Subject',
        description='The subject-line of the invitation.',
        required=True)
    fromAddr = ASCIILine(title='From',
        description='The email address of the person sending the '
            'invitation.',
        required=True)
    toAddr = ASCIILine(title='To',
        description='The email address of the person receiving the '
            'invitation.',
        required=True)
    fn = TextLine(title='Name',
        description='The name of the invited member.',
        required=True)
    message = Text(title='Invitation Message',
      description='The message that appears at the top of the email '
          'invitation to the new group member. The message will '
          'appear before the two links that allow the user to accept '
          'or reject the invitation.',
      required=True)
