# -*- coding: utf-8 -*-
# Log Helper (logHelper.py), version 0.2-dev.
# An NVDA global plugin to make dealing with the NVDA log easier and more efficient.

#    Copyright (C) 2019 Luke Davis <newanswertech@gmail.com>
#
# This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License
# as published by    the Free Software Foundation; either version 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
# You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

# This add-on is intended to make debugging tasks easier for developers. If you make frequent use of the NVDA log, this may provide features that help you.
# Other things are planned, but currently the only implemented feature is:
# Press NVDA+shift+F1, to insert a sequentially numbered line in the log.
# This makes it easier to find where you were last, before or after you performed a certain action.
# The lines are modeled after the old Linux Syslog mark lines, and look like this:
# -- MARK 1 --
# They are currently logged at the info loglevel.
# Note: reloading plugins currently resets the number inserted in the log, thus making the numeric part of the mark line somewhat useless.
# This will be fixed later if possible.
# Note also that configuration from within NVDA is planned for later; for now see the CONFIG section below.

from __future__ import unicode_literals
import globalPluginHandler
from scriptHandler import script

# A global variable to track mark number
logHelper_markNumber = 0

class GlobalPlugin (globalPluginHandler.GlobalPlugin):

# CONFIG
	# The mark lines can include an arbitrary number of blank lines after them, to further help divide your log into sections.
	trailingNewlines = 0
	# In case you don't like "-- MARK <number> --" as your text. The number is represented by {0}.
	markString = "-- MARK {0} --"

	@script(
		gesture="kb:nvda+shift+F1",
		description="Inserts a mark line in the log to aid in debugging"
		)
	def script_logAMarkLine(self, gesture):
		global logHelper_markNumber
		from logHandler import log
		import ui
		logHelper_markNumber += 1
		message = self.markString.format(logHelper_markNumber)
		if self.trailingNewlines > 0: message += "\n" * self.trailingNewlines
		if len(message) <= 0: return	# Sanity check
		ui.message("Log marked!")
		log.info(message)
