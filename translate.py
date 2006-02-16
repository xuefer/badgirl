#!/usr/bin/env python

# Copyright (c) 2002 Daniel DiPaolo, et. al.
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

from moobot_module import MooBotModule
handler_list = ["rot13", "reverse"]

class rot13(MooBotModule):
	def __init__(self):
		self.regex = "^rot13 .+$"

	def handler(self, **args):
		"Qbrf n fvzcyr ebg13, abguvat snapl"
		from irclib import Event, nm_to_n
		import string
		if args["type"] == "privmsg": target=nm_to_n(args["source"])
		else: target=args["channel"]
	
		msg = " ".join(args["text"].split(" ")[2:])
		newstring = msg.encode("rot_13")
		return Event("privmsg", "", target, [newstring])

class reverse(MooBotModule):
	def __init__(self):
		self.regex = "^reverse .+"

	def handler(self, **args):
		"gnirts a sesreveR"
		from irclib import Event, nm_to_n
		if args["type"] == "privmsg": target=nm_to_n(args["source"])
		else: target=args["channel"]
	
		from string import join
		orig_string = join(args["text"].split(" ")[2:])
		newstring = ""
		for i in range(1, len(orig_string)+1):
			newstring += orig_string[-i]
		return Event("privmsg", "", target, [newstring])
	
def escapes(text):
	import string
	text = string.replace(text, "\\", "\\\\")
	text = string.replace(text, '"', '\\"')
	return text
