__kupfer_name__ = _("Define")
__kupfer_sources__ = ()
__kupfer_actions__ = ("Define", )
__description__ = _("Define with Google")
__version__ = "2011-12-06"
__author__ = "Karl Svartholm <karl@passionismandatory.com>"

import urllib

from kupfer.objects import Action, TextLeaf
from kupfer import utils, plugin_support


__kupfer_settings__ = plugin_support.PluginSettings(
	{
		"key": "lang",
		"label": _("Language"),
		"type": str,
		# TRANS: Default language code
		"value": _("en"),
	},
)


class Define (Action):
	def __init__(self):
		Action.__init__(self, _("Define"))

	def activate(self, leaf):
		# Send in UTF-8 encoding
		lang_code = __kupfer_settings__["lang"]

		search_url="http://www.google.se/#hl=%s&tbs=dfn:1" % lang_code
		# will encode search=text, where `text` is escaped
		query_url = search_url + "&" + urllib.urlencode({"q": leaf.object})
		utils.show_url(query_url)
	def item_types(self):
		yield TextLeaf
	def get_description(self):
		lang_code = __kupfer_settings__["lang"]
		return _("Define this term with Google")
	def get_icon_name(self):
		return "edit-find"

