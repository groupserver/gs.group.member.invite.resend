# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014, 2016 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals, print_function
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from zope.i18n import translate
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from Products.CustomUserFolder.userinfo import userInfo_to_anchor
from Products.XWFCore.XWFUtils import get_the_actual_instance_from_zope
from Products.GSGroup.groupInfo import groupInfo_to_anchor
from gs.group.base import GroupForm
from gs.group.member.base import (FullMembers, InvitedMembers, )
from gs.profile.email.base import EmailUser
from gs.group.member.invite.base.inviter import Inviter
from gs.group.member.invite.base.audit import (Auditor, INVITE_OLD_USER, INVITE_EXISTING_MEMBER)
from .interfaces import IGSResendInvitation
from . import GSMessageFactory as _


class ResendInvitationForm(GroupForm):
    pageTemplateFileName = 'browser/templates/resend_invite.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, group, request):
        super(ResendInvitationForm, self).__init__(group, request)

        if 'form.userId' not in self.request.form:
            raise ValueError('No userId')
        self.userId = self.request.form['form.userId']

    @Lazy
    def label(self):
        retval = _('page-title', 'Resend the invitation to ${userName}',
                   mapping={'userName': self.userInfo.name})
        return retval

    @Lazy
    def form_fields(self):
        retval = form.Fields(IGSResendInvitation, render_context=False)
        return retval

    @Lazy
    def defaultFromEmail(self):
        emailUser = EmailUser(self.context, self.adminInfo)
        addrs = emailUser.get_delivery_addresses()
        retval = addrs and addrs[0] or ''
        return retval

    @Lazy
    def defaultToEmail(self):
        emailUser = EmailUser(self.context, self.userInfo)
        addrs = emailUser.get_addresses()
        retval = addrs and addrs[0] or ''
        return retval

    def setUpWidgets(self, ignore_request=False):
        data = {'fromAddr': self.defaultFromEmail,
                'toAddr': self.defaultToEmail,
                'fn': self.userInfo.name,
                'userId': self.userId}
        subject = _('inviation-email-subject', 'Invitation to join ${groupName} (action required)',
                    mapping={'groupName': self.groupInfo.name})
        data['subject'] = translate(subject)

        body = _('invitation-email-body',
                 '''Please accept this invitation to join ${groupName}. I have set up a
profile for you, so you can start participating in the group as soon as you
accept this invitation.''', mapping={'groupName': self.groupInfo.name})

        data['message'] = translate(body)

        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)

    @form.action(name='resend', label=_('page-button', 'Resend'),
                 failure='handle_invite_action_failure')
    def handle_invite(self, action, data):
        self.actual_handle_add(action, data)

    def handle_invite_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = _('feedback-error', '<p>There is an error:</p>')
        else:
            self.status = _('feedback-errors', '<p>There are errors:</p>')

    @Lazy
    def userInfo(self):
        retval = createObject('groupserver.UserFromId', self.context, self.userId)
        return retval

    @Lazy
    def adminInfo(self):
        return self.loggedInUser

    def already_a_member(self, u, e, g):
        retval = _('feedback-members', '''<ul>
<li>${userName} (with the email address {emailAddress}) is already a member 'of ${groupName}.</li>
<li>No changes have been made.</li>
</ul>''', mapping={'userName': u, 'emailAddress': e, 'groupName': g, })
        return retval

    def resent(self, u, e, g):
        retval = _('feedback-resent', '''<ul>
<li>Resent the invitation to ${userName} (to the email address ${emailAddress}) to join
${groupName}.</li>
</ul>''', mapping={'userName': u, 'emailAddress': e, 'groupName': g, })
        return retval

    def issues(self, u, e, g):
        retval = _('feedback-issues', '''<ul>
<li>Cannot <b>resend</b> an invitation to ${userName}, because they have yet been <i>invited</i> to
join ${groupName}.</li>
<li>No changes have been made.</li>
</ul>''', mapping={'userName': u, 'groupName': g, })
        return retval

    def actual_handle_add(self, action, data):
        u = userInfo_to_anchor(self.userInfo)
        e = '<code class="email">%s</code>' % self.defaultToEmail
        g = groupInfo_to_anchor(self.groupInfo)
        auditor, inviter = self.get_auditor_inviter()
        fullMembers = FullMembers(self.groupInfo.groupObj)
        invitedMembers = InvitedMembers(self.groupInfo.groupObj)
        if self.userId in fullMembers:
            auditor.info(INVITE_EXISTING_MEMBER, self.defaultToEmail)
            self.status = self.already_a_member(u, e, g)
        elif self.userId in invitedMembers:
            self.status = self.resent(u, e, g)
            inviteId = inviter.create_invitation(data, False)
            auditor.info(INVITE_OLD_USER, self.defaultToEmail)
            inviter.send_notification(data['subject'], data['message'],
                                      inviteId, data['fromAddr'], data['toAddr'])
        else:
            self.status = self.issues(u, e, g)
        assert self.status

    def get_auditor_inviter(self):
        ctx = get_the_actual_instance_from_zope(self.context)
        inviter = Inviter(ctx, self.request, self.userInfo, self.adminInfo, self.siteInfo,
                          self.groupInfo)
        auditor = Auditor(self.siteInfo, self.groupInfo, self.adminInfo, self.userInfo)
        return (auditor, inviter)
