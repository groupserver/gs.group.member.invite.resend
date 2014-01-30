=================================
``gs.group.member.invite.resend``
=================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Resend an invitation to join a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-01-29
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

Sometimes, for whatever reason, an invitation fails to be delivered. This
product provides the `Resend page`_ that allows the invitation to be
resent.

Resend page
===========

The Resend page, ``resend_invitation.html`` in the group context, provides
a entry to write a message, a button to preview the message, and one to
send the invitation. The *Preview* button, and sending the invitation
itself, is handled by the base Invitation product [#base]_.

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.member.invite.resend
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#base] See
          <https://source.iopen.net/groupserver/gs.group.member.invite.base>
