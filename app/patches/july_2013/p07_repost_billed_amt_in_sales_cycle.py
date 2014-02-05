# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

def execute():
	import webnotes
	webnotes.reload_doc('stock', 'doctype', 'packed_item')
	for si in webnotes.conn.sql("""select name from `tabSales Invoice` where docstatus = 1"""):
		webnotes.get_obj("Sales Invoice", si[0], 
			with_children=1).update_qty(change_modified=False)
		webnotes.conn.commit()
