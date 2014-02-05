# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

# For license information, please see license.txt

from __future__ import unicode_literals
import webnotes
from webnotes import _

class DocType:
	def __init__(self, d, dl):
		self.doc, self.doclist = d, dl

	def validate(self):
		for key in ["item_naming_by", "item_group", "stock_uom",
			"allow_negative_stock"]:
			webnotes.conn.set_default(key, self.doc.fields.get(key, ""))

		from setup.doctype.naming_series.naming_series import set_by_naming_series
		set_by_naming_series("Item", "item_code",
			self.doc.get("item_naming_by")=="Naming Series", hide_name_field=True)

		stock_frozen_limit = 356
		submitted_stock_frozen = self.doc.stock_frozen_upto_days
		if submitted_stock_frozen > stock_frozen_limit:
			self.doc.stock_frozen_upto_days = stock_frozen_limit
			webnotes.msgprint (_("`Freeze Stocks Older Than` should be smaller than %d days.") %stock_frozen_limit)
