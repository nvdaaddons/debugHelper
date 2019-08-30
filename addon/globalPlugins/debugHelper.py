# -*- coding: utf-8 -*-
# Debug Helper (debugHelper.py), version 1.0.3
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

# This add-on complies with Semantic Versioning: https://semver.org/

# Debug Helper is intended to make debugging tasks easier for developers. If you make frequent use of the NVDA log, this may provide features that help you.
# Other things are planned, but currently the only implemented feature is:
# Press NVDA+shift+F1, to insert a sequentially numbered line in the log. (Can be remapped under Tools in Input Gesture settings.)
# This makes it easier to find where you were last, before or after you performed a certain action.
# The lines are modeled after the old Linux Syslog mark lines, and look like this:
# -- MARK 1 --
# They are currently logged at the info loglevel.

from __future__ import unicode_literals
from globalCommands import SCRCAT_TOOLS
import config
import globalPluginHandler, globalVars
import gui, wx
import addonHandler

addonHandler.initTranslation()	# Makes translations work correctly.

# CONSTANTS:
DH_DEFAULT_BLANKS_BEFORE = 1
DH_DEFAULT_BLANKS_AFTER = 0

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	# CONFIG
	# In case you don't like "-- MARK <number> --" as your text. The number is represented by {0}.
	# Translators: the message entered in the log, containing the mark and its sequence number (number represented by {0} placeholder)
	markString = _("-- MARK {0} --")
	# END CONFIG

	# Sets the next to be used mark count, initializing it to 1 if not set. Persists across plugin reloads.
	globalVars.debugHelperMarkCount = getattr(globalVars, 'debugHelperMarkCount', 1)

	# __init__, onConfigDialog, and terminate methods borrowed heavily from Joseph Lee's stuff.

	# Needed for NVDA configuration dialog setup.
	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.getAppRestriction = None	# FixMe: why do we do this?
		self.restriction = False	# FixMe: why do we do this?
		# Dialog or the panel.
		if hasattr(gui.settingsDialogs, "SettingsPanel"):
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(DebugHelperSettings)
		else:
			self.prefsMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
			# Translators: first is the NVDA Preferences menu item for the debugHelper settings dialog
			# Translators: second is help text for the menu item
			self.dhSettings = self.prefsMenu.Append(wx.ID_ANY, _("&Debug Helper..."), _("Debug Helper add-on settings"))
			gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onConfigDialog, self.dhSettings)

	# Needed for NVDA configuration dialog setup
	def onConfigDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(DebugHelperSettings)

	# Needed for NVDA configuration dialog cleanup
	def terminate(self):
		if hasattr(gui.settingsDialogs, "SettingsPanel"):
			gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(DebugHelperSettings)
		else:
			try:
				if wx.version().startswith("4"):
					self.prefsMenu.Remove(self.dhSettings)
				else:
					self.prefsMenu.RemoveItem(self.dhSettings)
			except:
				pass

	# Script to insert a numbered mark line in the log, and announce the insertion and number to the user.
	def script_logAMarkLine(self, gesture):
		import ui
		from logHandler import log
		if len(self.markString) == 0: return	# Sanity check
		markStringWithNumber = self.markString.format(globalVars.debugHelperMarkCount)
		newlinesBeforeString = "\n" * config.conf["debugHelper"]["newlinesBefore"]
		newlinesAfterString = "\n" * config.conf["debugHelper"]["newlinesAfter"]
		message = "{0}{1}{2}".format(newlinesBeforeString, markStringWithNumber, newlinesAfterString)
		# Translators: a message telling the user that a mark has been inserted in the log, and giving its sequence number
		ui.message(_("Logging mark {0}!".format(globalVars.debugHelperMarkCount)))
		log.info(message)
		globalVars.debugHelperMarkCount += 1	# Increase the sequence number for next time

	script_logAMarkLine.category=SCRCAT_TOOLS
	# Translators: input help message for a Debug Helper command
	script_logAMarkLine.__doc__ = _("Inserts a mark line in the log to aid in debugging")
	__gestures = { "kb:nvda+shift+f1":"logAMarkLine" }

# Add-on config database
# Pretty well ripped off from Enhanced Touch Gestures and Golden Cursor by Joseph Lee
confspec = {
	"newlinesBefore": "integer(min=0, max=10, default=1)",
	"newlinesAfter": "integer(min=0, max=10, default=0)",
}
config.conf.spec["debugHelper"] = confspec

# Present either the old settings dialog or a settings panel.
if hasattr(gui.settingsDialogs, "SettingsPanel"):
	class DebugHelperSettings (gui.settingsDialogs.SettingsPanel):
		# Translators: This is the label for the Debug Helper settings category in NVDA Settings screen.
		title = _("Debug Helper")

		def makeSettings(self, settingsSizer):
			dhHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
			# Translators: The label for a setting in Debug Helper settings dialog to set blank lines inserted before marks
			self.newlinesBefore=dhHelper.addLabeledControl(_("Number of blank lines before each mark (can make marks easier to find with fast arrowing)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=config.conf["debugHelper"]["newlinesBefore"])
			# Translators: The label for a setting in Debug Helper settings dialog to set blank lines inserted after marks
			self.newlinesAfter=dhHelper.addLabeledControl(_("Number of blank lines after each mark"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=config.conf["debugHelper"]["newlinesAfter"])

		def onSave(self):
			config.conf["debugHelper"]["newlinesBefore"] = self.newlinesBefore.Value
			config.conf["debugHelper"]["newlinesAfter"] = self.newlinesAfter.Value

else:
	class DebugHelperSettings (gui.SettingsDialog):
		# Translators: This is the label for the Debug Helper settings dialog (used in NVDA versions before settings category panel).
		title = _("Debug Helper Settings")

		def makeSettings(self, settingsSizer):
			dhHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
			# Translators: The label for a setting in Debug Helper settings dialog to set blank lines inserted before marks
			self.newlinesBefore=dhHelper.addLabeledControl(_("Number of blank lines before each mark (can make marks easier to find with fast arrowing)"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=config.conf["debugHelper"]["newlinesBefore"])
			# Translators: The label for a setting in Debug Helper settings dialog to set blank lines inserted after marks
			self.newlinesAfter=dhHelper.addLabeledControl(_("Number of blank lines after each mark"), gui.nvdaControls.SelectOnFocusSpinCtrl, min=0, max=10, initial=config.conf["debugHelper"]["newlinesAfter"])

		def onOk(self, evt):
			config.conf["debugHelper"]["newlinesBefore"] = self.newlinesBefore.Value
			config.conf["debugHelper"]["newlinesAfter"] = self.newlinesAfter.Value
			super(DebugHelperSettings, self).onOk(evt)
