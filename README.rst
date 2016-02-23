=================================
``gs.group.member.invite.resend``
=================================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Resend an invitation to join a group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2016-02-23
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

Sometimes, for whatever reason, an invitation to join a group
fails to be delivered. This product provides the `Resend page`_
that allows the invitation to be resent.

Resend page
===========

The Resend page, ``resend_invitation.html`` in the group context,
provides a entry to write a message, a button to preview the
message, and one to send the invitation. The *Preview* button,
and sending the invitation itself, is handled by the base
Invitation product [#base]_. The page presents itself as being in
the context of the *Mange members* page, because the Manage
members page provides the one and only link here.

Resources
=========

- Code repository:
  https://github.com/groupserver/gs.group.member.invite.resend
- Translations:
  https://www.transifex.com/projects/p/gs-group-member-invite-resend
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17

.. [#base] See
          <https://source.iopen.net/groupserver/gs.group.member.invite.base>
