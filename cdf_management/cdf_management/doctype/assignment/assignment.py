# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Assignment(Document):
	def on_update(self):
		app = frappe.get_doc('Application',self.application)
		app.assignment = self.name
		app.save()