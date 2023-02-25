# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import datetime
import re
from frappe.model.document import Document
from frappe.utils import now

class ConstituencyEntry(Document):
	pass
	# def before_save(self):
	# 	self.sync_corresponding_application()
  
	# def before_update(self):
	# 	self.create_corresponding_application()
	
	# def sync_external(self):
	# 	availible_fields = ["amount","response","level","name_of_beneficiary","school","grade","sex","age", 
    #                   "training_institution","name_of_project","location","name_of_contractor", "contact_number","group_type"
    #                   ,"group_name","projects","type"]
	# 	tables = ['community_projects','skills_development', 'loans', 'secondary_school','grants']
	# # Method to push table entries to constituencies
	# def sync_corresponding_application(self):
		
	# 	# frappe.msgprint(str(self.secondary_school[0].__dict__))
	# 	# All the available fields that we want to modify in application
	# 	# The tables in the Doctypes
	# 	availible_fields = ["amount","response","level","name_of_beneficiary","school","grade","sex","age", 
    #                   "training_institution","name_of_project","location","name_of_contractor", "contact_number","group_type"
    #                   ,"group_name","projects","type"]
	# 	tables = ['community_projects','skills_development', 'loans', 'secondary_school','grants']
	# 	# Looks at the child tables then loops through all its values
	# 	pro_name = str(frappe.db.exists("Province Entry", self.province))
	
	# 	# province = frappe.get_doc("Province Entry",self.province)
	# 	prov = frappe.get_doc("Province Entry",pro_name)
	# 	# Basically we just loop through all the tables and looks at the entries then if no corresponding application exists
	# 	# it creates on then also handles syncing
	# 	for table in tables:
	# 		con_table = list(getattr(prov,table))
	# 		con_table_applications = [str(x.linked_application) for x in con_table]
	# 		for entry in getattr(self,table):
				
	# 			#  Fo syncing with the constitunecy table
	# 			application = frappe.get_doc("Application",str(entry.linked_application))
	# 			fields = entry.__dict__.keys()
	# 			# frappe.msgprint(str(entry.name))
	# 			for field in availible_fields:
	# 				if field in fields:
	# 					setattr(application,field,getattr(entry,field))
	# 					application.save()
	# 			# frappe.msgprint(f"Updated {entry.name}")
	# 			# entry.save()

	# 			if not str(entry.linked_application) in con_table_applications and entry.response == "Accepted":
	# 				entry_copy  = frappe.new_doc(entry.__dict__['doctype'])
	# 				entry_copy.update(entry.as_dict())
	# 				entry_copy.insert()
	# 				con_table.append(entry_copy)
	# 			elif str(entry.linked_application) in con_table_applications:
	# 				for table1 in tables:
	# 					for entry1 in getattr(prov,table1):
	# 						fields1 = entry1.__dict__.keys()
	# 						#  Fo syncing with the constitunecy table
	# 						application1 = frappe.get_doc("Application",str(entry1.linked_application))
	# 						for field1 in availible_fields:
	# 							if field1 in fields1:
	# 								if(field1 == "response"):
	# 									continue
	# 								setattr(entry1,field1,getattr(application1,field1))

	# 		# frappe.msgprint(str(con_table))
	# 		setattr(prov,table,con_table)
	# 		prov.save()


	