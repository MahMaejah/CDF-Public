# Copyright (c) 2022, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
from cdf_management.cdf_management.doctype.ward.ward import Ward
from frappe.model.document import Document

class Constituency(Document):
	def before_save(self):
		self.calculate_table_total()
	def calculate_table_total(self):
		constituency_table = self.constituency_entries
		constituency_entries_total = 0.00
		for amount in constituency_table:
			if amount.response == "Accepted":
				constituency_entries_total += int(amount.amount)
		setattr(self,"constituency_entries_total", f"ZMW {constituency_entries_total:,}")
		setattr(self,"clean_total", constituency_entries_total)
		# frappe.msgprint(str(self.clean_total))
		# call grand_total_per_summary function
	
		


