# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2013, 2016 OnlineGroups.net and Contributors.
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
from __future__ import unicode_literals, absolute_import, print_function
from zope.schema import ASCIILine, Text, TextLine
from zope.interface.interface import Interface
from . import GSMessageFactory as _


class IGSResendInvitation(Interface):
    userId = ASCIILine(
        title='User Identifier',
        description='The user ID of the person receiving the invitation.',
        required=True)
    subject = TextLine(
        title=_('form-field-subject-h', 'Subject'),
        description=_('form-field-subject-desc', 'The subject-line of the invitation.'),
        required=True)
    fromAddr = ASCIILine(
        title='From',
        description='The email address of the person sending the invitation.',
        required=True)
    toAddr = ASCIILine(
        title=_('form-field-to-h', 'To'),
        description=_('form-field-to-desc',
                      'The email address of the person receiving the invitation.'),
        required=True)
    fn = TextLine(
        title=_('form-field-name-h', 'Name'),
        description=_('form-field-name-desc', 'The name of the invited member.'),
        required=True)
    message = Text(
        title=_('form-field-msg-h', 'Invitation message'),
        description=_('form-field-mesg-desc',
                      'The message that appears at the top of the email invitation to the new '
                      'group member. The message will appear before the two links that allow the '
                      'user to accept or reject the invitation.'),
        required=True)
