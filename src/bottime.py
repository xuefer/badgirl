#!/usr/bin/env python

# Copyright (c) 2002 Brad Stewart
# Portions taken from Joe Wreschnig's DateTime.pm for Funbot.
#
# Copyright (C) 2008 by FKtPp
# 
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#

"""bottime.py - time-related modules """
import os
import time

import database
from moobot_module import MooBotModule

handler_list=["cputime", "uptime", "date"]

class cputime(MooBotModule):
    def __init__(self):
        self.regex = "^cputime$"

    def handler(self, **args):
        """Reports CPU time usage for the current thread."""
        from os import times
        from irclib import Event
        target=args["channel"]
        if args["type"] == "privmsg":
            from irclib import nm_to_n
            target=nm_to_n(args["source"])
        return Event("privmsg", "", target,
                 ["User time: " + str(times()[0]) + " seconds, " + \
                  "system time: " + str(times()[1]) + " seconds.  "+\
                  "Childrens' user time: " + str(times()[2]) + ", "+\
                  "childrens' system time: " + str(times()[3])])

class uptime(MooBotModule):
    def __init__(self):
        self.regex = "^uptime$"
        self.pid = os.getpid()

        database.doSQL("DELETE FROM data WHERE type = 'uptime' AND " + \
                   "created_by != '" + str(self.pid) + "'");
        if len(database.doSQL("SELECT * FROM data WHERE " + \
                      "type = 'uptime' AND " + \
                      "created_by ='" + str(self.pid) + "'")) == 0:
            database.doSQL("INSERT INTO data (data, type, created_by) "+\
                       "VALUES('" + str(int(time.time())) + "', "+\
                       "'uptime', '" + str(self.pid) + "')")

    def handler(self, **args):
        from irclib import Event
        from seen import time2str
        start_time = database.doSQL("SELECT data FROM data WHERE " + \
                        "type = 'uptime' and " + \
                        "created_by ='" + str(self.pid) + \
                        "'")[0][0]
        result = "I've been awake for " + time2str(int(start_time))

        return Event("privmsg", "", self.return_to_sender(args), [ result ])

class date(MooBotModule):
    def __init__(self):
        """
        >>> import re
        >>> from bottime import date
        >>> d = date()
        >>> r = re.compile(d.regex)
        >>> r.match("date") and True or False
        True
        >>> r.match("date fktpp") and True or False
        True
        >>> r.match("datestz") and True or False
        True
        >>> r.match("datestz fktpp") and True or False
        True
        >>> r.match("datestz fktpp +12") and True or False
        True
        >>> r.match("datestz +0") and True or False
        True
        """
        self.regex = "^date(?:stz)?(?: [^ \t]+)*$"
        self.help_message_date = "date(see also datestz) usage: ~date [nick|+/-offset]"
        self.help_message_datestz = "datestz usage: ~datestz [nick] [+/-offset]"

    def handler(self, **args):
        import os
        from irclib import Event

        input = args["text"].lower().split()
        del input[0]

        request_nick = self.return_to_sender(args, select='nick')

        if input[0] == 'datestz':
            result = self.handle_tz(input, request_nick)
        else:
            result = self.get_time(input, request_nick)

        return Event("privmsg", "", self.return_to_sender(args), \
                 [ result ])

    def get_time(self, input, request_nick):
        """return the requested time string

        .valid input list format:
        --------------
        [0]  [1]
        --------------
        date nick
        date +/-offset
        date help
        date
        --------------
        """
        assert input[0] == "date"

        tz_offset = None
        tz_is_valid = False
        qnick = None

        if len(input) == 1:
            # No Parameter, we assume the user want to know his local time
            qnick = request_nick
        elif len(input) == 2:
            if input[1] == "help":
                return self.help_message_date
            # if input[1] is not a valid tz_offset string, we assume it is 
            # a nick
            tz_offset, tz_is_valid = self.tz_validate(input[1])
            if not tz_is_valid:
                qnick = input[1]
        else:
            return self.help_message_date

        if qnick:
            tz_offset = database.doSQL("select tz_offset from bottime "\
                                            "where nick = '%s'" % self.sqlEscape(qnick))
            if tz_offset:
                tz_offset = tz_offset[0][0]
                tz_is_valid = True

        if not tz_is_valid:
            return "%s have no timezone setting, "\
                "current server time is: %s" % (qnick, time.asctime())
        
        return "%s (GMT %d)" % (time.asctime(
                time.gmtime(
                    time.time() + (60 * 60 * tz_offset)
                    )
                ),
                                tz_offset)


    def handle_tz(self, input, request_nick):
        """change or reset the time zone setting

        .valid input list format
        ----------------------
        [0]     [1]  [2]
        ----------------------
        datestz nick +/-offset
        datestz +/-offset
        ----------------------
        """
        assert input[0] == "datestz"

        tz_offset = None
        tz_is_valid = False
        qnick = request_nick
        show_offset = False
        input_len = len(input)

        if input_len == 1:
            show_offset = True
        elif input_len == 2:
            tz_offset, tz_is_valid = self.tz_validate(input[1])
            if not tz_is_valid:
                qnick = input[1]
                if not qnick == "help":
                    show_offset = True
        elif input_len == 3:
            tz_offset, tz_is_valid = self.tz_validate(input[2])
            qnick = input[1]
    
        if not tz_is_valid:
            if not show_offset:
                return self.help_message_datestz
            else:
                return self.show_tz(qnick)
        else:
            tmp_data = database.doSQL("select nick, tz_offset from bottime "\
                                          "where nick = '%s'" % self.sqlEscape(qnick))

            if tmp_data:
                sql_string = "update bottime "\
                    "set tz_offset  = %s "\
                    "where nick = '%s'" % (tz_offset, self.sqlEscape(qnick))
            else:
                sql_string = "insert into bottime (nick, tz_offset) "\
                    "values ('%s', %s)" % (self.sqlEscape(qnick), tz_offset)

            database.doSQL(sql_string)

        return "datastz: done!"

    def show_tz(self, nick):
        """
        """
        possiable_data = database.doSQL("select tz_offset from bottime "\
                                            "where nick = '%s'" % nick)
        if not possiable_data:
            return "datastz: %s has no timezone setting, please try to "\
                "setup one by using `~datastz %s +/-offset'" % (nick,
                                                                nick)
        else:
            return "%s's timezone was (GMT %d)" % (nick,
                                                   possiable_data[0][0])

    def tz_validate(self, tz_string):
        """validate the time zone offset string

        return the crosponding time zone offset if the tz_string is
        valid, or return False.
        >>> from bottime import date
        >>> d = date()
        >>> d.tz_validate("12")
        (12, True)
        >>> d.tz_validate("-12")
        (-12, True)
        >>> d.tz_validate("13")
        (13, False)
        >>> d.tz_validate("0")
        (0, True)
        >>> d.tz_validate("-0")
        (0, True)
        """
        tz_offset = 0
        result = True
        
        try:
            tz_offset = int(tz_string)
        except ValueError:
            result = False

        if abs(tz_offset) > 12:
            result = False

        return tz_offset, result

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
    
