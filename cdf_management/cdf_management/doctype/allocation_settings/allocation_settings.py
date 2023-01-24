# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AllocationSettings(Document):
	pass
	def on_update(self):
		self.calculate_amount_per_constituency()
	def calculate_amount_per_constituency(self):
		# this is gonna be a ka quick fix
		try:
			amount_allocated_to_whole_country = self.total_amount_allocated_for_community_development_country_wide
			amount_alloacated_to_each_constituency = round(amount_allocated_to_whole_country/156)
			self.total_amount_allocated_per_constituency = f"ZMW {amount_alloacated_to_each_constituency:,}"
		except:
			frappe.msgprint("Something went wrong in allocation settings")
		# self.total_amount_allocated_for_community_development_country_wide = f"ZMW {amount_allocated_to_whole_country:,}"