# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
class ProvinceEntry(Document):
	
	def before_save(self):
		self.sync_corresponding_application()
	
	def sync_corresponding_application(self):
		
		# frappe.msgprint(str(self.secondary_school[0].__dict__))
		# All the available fields that we want to modify in application
		# The tables in the Doctypes
		availible_fields = ["amount","response","level","name_of_beneficiary","school","grade","sex","age", 
                      "training_institution","name_of_project","location","name_of_contractor", "contact_number","group_type"
                      ,"group_name","projects","type"]
		tables = ['community_projects','skills_development', 'loans', 'secondary_school','grants']
		# Looks at the child tables then loops through all its values
		# frappe.msgprint("=======================")
		
		# Basically we just loop through all the tables and looks at the entries then if no corresponding application exists
		# it creates on then also handles syncing
		# for table in tables:
		# 	for entry in getattr(self,table):
		# 		fields = entry.__dict__.keys()
		# 		#  Fo syncing with the constitunecy table
		# 		application = frappe.get_doc("Application",str(entry.linked_application))

				# for field in availible_fields:
				# 	if field in fields:
				# 		setattr(entry,field,getattr(application,field))
