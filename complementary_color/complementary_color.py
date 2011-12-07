__kupfer_name__ = _("Complementary Color")
__kupfer_actions__ = ("GetComplementaryColor", )
__description__ = _("Get the complementary color of the HEX color you pass it")
__version__ = "0.1"
__author__ = "Karl Svartholm <karl@passionismandatory.com>"

# XXX This plugin in sort of broken and have a really sad dependency :'(

import colors
from kupfer.objects import Action, TextLeaf
from kupfer import kupferstring
from kupfer import plugin_support

class GetComplementaryColor (Action):
	def __init__(self):
		Action.__init__(self, _("Get Complementary Color"))

	def has_result(self):
		return True

	def activate(self, leaf):
		leaf_text = kupferstring.tolocale(leaf.object)
		color = leaf_text[1:]
		result = "None"
		if len(color) == 3:
			r = color[0] + color[0]
			g = color[1] + color[1]
			b = color[2] + color[2]
		elif len(color) == 6:
			r = color[0:2]
			g = color[2:4]
			b = color[4:6]
		else:
			return TextLeaf("Unknown color format")


		color = colors.hex("#"+r+g+b)
		complement = colors.complementary(color)[4]
		r = int(complement.r*255)
		g = int(complement.g*255)
		b = int(complement.b*255)

		r = '%02x'%r
		g = '%02x'%g
		b = '%02x'%b

		result = "#" + str(r) + str(g) + str(b)

		return TextLeaf(result)

	def item_types(self):
		yield TextLeaf

	def valid_for_item(self, leaf):
		text = leaf.object
		return text and text.startswith("#")

	def get_icon_name(self):
		return "gnome-graphics"

	def get_description(self):
		return None

