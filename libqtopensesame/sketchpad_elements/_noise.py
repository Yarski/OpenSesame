#-*- coding:utf-8 -*-

"""
This file is part of openexp.

openexp is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

openexp is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with openexp.  If not, see <http://www.gnu.org/licenses/>.
"""

from libqtopensesame.dialogs.noise_settings import noise_settings
from libqtopensesame.sketchpad_elements._base_element import base_element
from libopensesame.sketchpad_elements import noise as noise_runtime

class noise(base_element, noise_runtime):

	def show_edit_dialog(self):

		"""
		desc:
			The show-edit dialog for the noise shows the settings dialog.
		"""

		d = noise_settings(self.main_window)
		d.set_properties(self.properties)
		properties = d.get_properties()
		if properties == None:
			return
		self.properties.update(properties)
		self.sketchpad.draw()

	@classmethod
	def mouse_press(cls, sketchpad, pos):

		d = noise_settings(sketchpad.main_window)
		properties = d.get_properties()
		if properties == None:
			return
		properties.update({
				u'x':			pos[0],
				u'y':			pos[1],
				u'show_if' : 	sketchpad.current_show_if()
			})
		return noise(sketchpad, properties=properties)
