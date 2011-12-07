__kupfer_name__ = _("More Image Tools")
__kupfer_actions__ = ("MirrorImage", "VerticallyMirrorImage")
__description__ = _("More image transformation tools")
__version__ = "2011-11-25"
__author__ = "Karl Svartholm <karl@passionismandatory.com>"

from os import path as os_path

from kupfer.objects import Action, FileLeaf
from kupfer import utils

class MirrorBase (Action):
	def __init__(self, name, method):
		Action.__init__(self, name)
		self.method = method

	def has_result(self):
		return False

	def activate(self, leaf):
		fpath = leaf.object
		if self.method == "vertical":
			argv = ["mogrify", "-flip", fpath]
		else:
			argv = ["mogrify", "-flop", fpath]
		# TODO Somethin like this?
		#runtimehelper.register_async_file_result(ctx, fpath)
		utils.spawn_async(argv)
		# TODO ...and then return something like this?
		#return FileLeaf(fpath)
		return

	def item_types(self):
		yield FileLeaf

	def valid_for_item(self, item):
		root, ext = os_path.splitext(item.object)
		# Note that more formats are supported (by ImageMagick)
		return ext.lower() in (".jpeg", ".jpg", ".gif", ".png", ".bmp", ".xbm", ".wbmp", ".dib", ".esp", ".ico", ".tga", ".tiff", ".tif", ".svg")

	def get_icon_name(self):
		return "gnome-graphics"

	def get_description(self):
		return None

class MirrorImage (MirrorBase):
	def __init__(self):
		MirrorBase.__init__(self, _("Mirror Image"), "horizontal")

	def get_icon_name(self):
		# TODO Replace with better icon
		return "gnome-graphics"

class VerticallyMirrorImage (MirrorBase):
	def __init__(self):
		MirrorBase.__init__(self, _("Vertically Mirror Image"), "vertical")

	def get_icon_name(self):
		# TODO Replace with better icon
		return "gnome-graphics"
