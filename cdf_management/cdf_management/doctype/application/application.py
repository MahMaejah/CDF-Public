# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Application(Document):
	def before_save(self):
		res = self.is_assigned()

		if not res:
			frappe.throw("You do not have permission to edit this document")
	
	def on_update(self):
		# res = self.is_assigned()
		# frappe.msgprint(f"Is assigend {res}")
		# if not res:
		# 	frappe.msgprint("You do not have permission to edit this document")
		# 	return
		self.auto_fill_ward_data()
		self.auto_fill_data("constituency",self.constituency,"Constituency Entry")
		self.auto_fill_data("district",self.district,"District")
		self.auto_fill_data("province",self.province,"Province Entry")
		self.calculate_constituency_financial_summary()
	
	def is_assigned(self):
		user = frappe.session.user
		if user == "Administrator":
			
			return True
		frappe.msgprint(user)
		assignments = frappe.db.get_list("Assignment", filters={'user': str(user)})
		is_level_above = False
		levels = {
			"Ward": 0, "Constituency": 1, "District": 2, "Province": 3
		}
		frappe.msgprint(str(assignments))
		for ass in assignments:
			ass1 = frappe.get_doc("Assignment", ass)
			if ass1.level != "Ward":
				# frappe.msgprint(ass.constituency)
				if ass1.constituency == self.constituency or ass1.province == self.province or ass1.province == self.province:
					is_level_above = True
					break
		if is_level_above:
			# frappe.msgprint("Is assigned larger applications")
			return True
		assignments = frappe.db.get_list("Assignment", filters={'user':user, 'application':str(self)})
		return len(assignments) > 0

	
	def validate(self):
		# frappe.msgprint("Running!")
		if self.type == "Secondary School Bursaries" or self.type == "Skill Development Bursaries":
			threshold_amount = frappe.db.get_single_value('Allocation Settings', 'bursaries')
		elif self.type == "Community Project":
			threshold_amount = frappe.db.get_single_value('Allocation Settings', 'community_projects')
		elif self.type == "Community Loans" or self.type == "Community Grants":
			threshold_amount = frappe.db.get_single_value('Allocation Settings', 'community_grants_and_loans')
		# frappe.msgprint(str(threshold_amount))
		if float(self.amount) > threshold_amount:
			frappe.throw("Amount allocated cannot exceed Threshold!")
	def auto_fill_ward_data(self):
		secondary_school_total = 0
		skills_development_total = 0
		communtiy_projects_total = 0
		loans_total = 0
		grants_total = 0
		ward_grand_total = 0
		approved_applications_in_ward = frappe.db.get_list("Application", filters = {"docstatus": 1,"ward":self.ward_name}, fields = ["name","type", "ward_name", "amount", "name_of_beneficiary", "school", "grade", "sex", "age", "training_institution","name_of_project","location","name_of_contractor", "contact_number","group_type","group_name","projects"])
		parent_ward = frappe.get_doc("Ward", self.ward_name)
		for application in approved_applications_in_ward:
			ward_grand_total += float(application.amount)
			
			if application.type == "Secondary School Bursaries":
				secondary_school_total += float(application.amount)
				child_table_data = {
					"name_of_the_beneficiary": application.name_of_beneficiary,
					"school": application.school,
					"grade": application.grade,
					"sex": application.sex,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_ward.secondary_school]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_ward.append("secondary_school", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_ward.append("secondary_school", child_table_data)
					row.insert()
					
			elif application.type == "Skill Development Bursaries":
				skills_development_total += float(application.amount)
				child_table_data = {
					"name_of_beneficiary": application.name_of_beneficiary,
					"sex": application.sex,
					"age": application.age,
					"contact_number": application.contact_number,
					"training_institution": application.training_institution,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_ward.skills_development]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_ward.append("skills_development", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_ward.append("skills_development", child_table_data)
					row.insert()
			
			elif application.type == "Community Project":
				communtiy_projects_total += float(application.amount)
				child_table_data = {
					"name_of_the_project": application.name_of_project,
					"location": application.location,
					"name_of_contractor": application.name_of_contractor,
					"contact_number": application.contact_number,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_ward.community_projects]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_ward.append("community_projects", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_ward.append("community_projects", child_table_data)
					row.insert()
				
			else:
				child_table_data = {
					"group_type": application.group_type,
					"group_name": application.group_name,
					"projects": application.projects,
					"amount": application.amount,
					"amount": application.amount,
					"linked_application": application.name
				}
				if application.type == "Community Loans":
					loans_total += float(application.amount)
					ward_child_table = [x for x in parent_ward.loans]
					child_table_field = "loans"
				else:
					grants_total += float(application.amount)
					ward_child_table = [x for x in parent_ward.grants]
					child_table_field = "grants"
		
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_ward.append(child_table_field, child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_ward.append(child_table_field, child_table_data)
					row.insert()
					
		parent_ward.total_number_of_cooperative = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Cooperative'}))
		parent_ward.total_number_of_women_groups = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Women Group'}))
		parent_ward.total_number_of_businesses = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Business'}))
		parent_ward.total_number_of_companies = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Company'}))
		parent_ward.total_number_of_youth_groups = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Youth Group'}))
		parent_ward.total_number_of_community_clubs = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'group_type':'Community Club'}))
		
		parent_ward.total_male_bursaries_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name,'sex':'Male', 'type':'Secondary School Bursaries'}))
		parent_ward.total_female_bursaries_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'sex':'Female', 'type':'Secondary School Bursaries'}))
		parent_ward.total_male_skill_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'sex':'Male', 'type':'Skill Development Bursaries'}))
		parent_ward.total_female_skill_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'sex':'female', 'type':'Skill Development Bursaries'}))
		parent_ward.total_number_of_community_projects = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name, 'type':'Community Project'}))

		parent_ward.total_number_of_project_submitted = float(frappe.db.count('Application', {'ward':self.ward_name,'type':'Community Project'})) + float(frappe.db.count('Application', {'ward':self.ward_name,'type':'Community Grants'})) + float(frappe.db.count('Application', {'ward':self.ward_name,'type':'Community Loans'}))
		parent_ward.total_number_of_projects_approved = float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name,'type':'Community Project'})) + float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name,'type':'Community Loans'})) + float(frappe.db.count('Application', {'docstatus': 1, 'ward':self.ward_name,'type':'Community Grants'})) 
		
		parent_ward.secondary_school_total_amount_disbursed = f"ZMW {secondary_school_total:,}"
		parent_ward.skills_development_total_amount_disbursed = f"ZMW {skills_development_total:,}"
		parent_ward.community_projects_total_amount_disbursed = f"ZMW {communtiy_projects_total:,}"
		parent_ward.loans_total_amount_disbursed = f"ZMW {loans_total:,}"
		parent_ward.grants_total_amount_disbursed = f"ZMW {grants_total:,}"
		parent_ward.total_amount_disbursed = f"ZMW {ward_grand_total:,}"

		parent_ward.save()



	def auto_fill_data(self,level,level_name,doc):
		secondary_school_total = 0
		skills_development_total = 0
		communtiy_projects_total = 0
		loans_total = 0
		grants_total = 0
		level_grand_total = 0
		approved_applications_in_level = frappe.db.get_list("Application", filters = {"docstatus": 1,level: level_name}, fields = ["name","type", "amount", "name_of_beneficiary", "school", "grade", "sex", "age", "training_institution","name_of_project","location","name_of_contractor", "contact_number","group_type","group_name","projects"])
		parent_level = frappe.get_doc(doc, level_name)
		for application in approved_applications_in_level:
			level_grand_total += float(application.amount)
			
			if application.type == "Secondary School Bursaries":
				secondary_school_total += float(application.amount)
				child_table_data = {
					"name_of_the_beneficiary": application.name_of_beneficiary,
					"school": application.school,
					"grade": application.grade,
					"sex": application.sex,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_level.secondary_school]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_level.append("secondary_school", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_level.append("secondary_school", child_table_data)
					row.insert()
					
					
			elif application.type == "Skill Development Bursaries":
				skills_development_total += float(application.amount)
				child_table_data = {
					"name_of_beneficiary": application.name_of_beneficiary,
					"sex": application.sex,
					"age": application.age,
					"contact_number": application.contact_number,
					"training_institution": application.training_institution,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_level.skills_development]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_level.append("skills_development", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_level.append("skills_development", child_table_data)
					row.insert()
			elif application.type == "Community Project":
				communtiy_projects_total += float(application.amount)
				child_table_data = {
					"name_of_the_project": application.name_of_project,
					"location": application.location,
					"name_of_contractor": application.name_of_contractor,
					"contact_number": application.contact_number,
					"amount": application.amount,
					"linked_application": application.name
				}
				ward_child_table = [x for x in parent_level.community_projects]
				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_level.append("community_projects", child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_level.append("community_projects", child_table_data)
					row.insert()
			else:
				child_table_data = {
					"group_type": application.group_type,
					"group_name": application.group_name,
					"projects": application.projects,
					"amount": application.amount,
					"amount": application.amount,
					"linked_application": application.name
				}
				if application.type == "Community Loans":
					loans_total += float(application.amount)
					ward_child_table = [x for x in parent_level.loans]
					child_table_field = "loans"
				
				else:
					grants_total += float(application.amount)
					ward_child_table = [x for x in parent_level.grants]
					child_table_field = "grants"

				og_length = len(ward_child_table)
				loop_count = 0
				found_match = False
				if len(ward_child_table) != 0:
					for entry in ward_child_table:
						if loop_count > og_length:
							# frappe.msgprint("Exceeded list")
							break
						loop_count += 1
						if str(entry.linked_application) == str(application.name):
							found_match = True
							# frappe.msgprint("entry exits")
							break
					if not found_match:
						# frappe.msgprint("entry does not exist")
						row = parent_level.append(child_table_field, child_table_data)
						row.insert()
				else:
					# frappe.msgprint("Child_tb is empty")
					row = parent_level.append(child_table_field, child_table_data)
					row.insert()
					
		parent_level.total_number_of_cooperative = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Cooperative'}))
		parent_level.total_number_of_women_groups = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Women Group'}))
		parent_level.total_number_of_businesses = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Business'}))
		parent_level.total_number_of_companies = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Company'}))
		parent_level.total_number_of_youth_groups = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Youth Group'})) 
		frappe.errprint(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Youth Group'}))
		parent_level.total_number_of_community_clubs = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'group_type':'Community Club'}))
		
		parent_level.total_male_bursaries_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, level: level_name,'sex':'Male', 'type':'Secondary School Bursaries'}))
		parent_level.total_female_bursaries_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'sex':'Female', 'type':'Secondary School Bursaries'}))
		parent_level.total_male_skill_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'sex':'Male', 'type':'Skill Development Bursaries'}))
		parent_level.total_female_skill_benficiaries = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'sex':'female', 'type':'Skill Development Bursaries'}))
		parent_level.total_number_of_community_projects = float(frappe.db.count('Application', {'docstatus': 1, level: level_name, 'type':'Community Project'}))

		parent_level.total_number_of_project_submitted = float(frappe.db.count('Application', {level:level_name,'type':'Community Project'})) + float(frappe.db.count('Application', {level:level_name,'type':'Community Grants'})) + float(frappe.db.count('Application', {level:level_name,'type':'Community Loans'}))
		parent_level.total_number_of_projects_approved = float(frappe.db.count('Application', {'docstatus': 1, level: level_name,'type':'Community Project'})) + float(frappe.db.count('Application', {'docstatus': 1, level:level_name,'type':'Community Loans'})) + float(frappe.db.count('Application', {'docstatus': 1, level:level_name,'type':'Community Grants'})) 
		
		parent_level.secondary_school_total_amount_disbursed = f"ZMW  {secondary_school_total:,}"
		parent_level.skills_development_total_amount_disbursed = f"ZMW  {skills_development_total:,}"
		parent_level.community_projects_total_amount_disbursed = f"ZMW  {communtiy_projects_total:,}"
		parent_level.loans_total_amount_disbursed = f"ZMW  {loans_total:,}"
		parent_level.grants_total_amount_disbursed = f"ZMW  {grants_total:,}"
		parent_level.total_amount_disbursed = f"ZMW  {level_grand_total:,}"

		parent_level.save()

	def calculate_constituency_financial_summary(self):
		constituency = frappe.get_doc('Constituency Entry', self.constituency)
		amount_allocated_to_constituency = frappe.db.get_single_value('Allocation Settings', 'total_amount_allocated_per_constituency').replace('ZMW','')
		# frappe.msgprint(_("Amount Allocated to {0} Constituency is {1}").format(self.constituency,amount_allocated_to_constituency))
		amount_used_in_constituency = constituency.total_amount_disbursed
		# total_amount_unused
		int_clean_allocated_amount = float(amount_allocated_to_constituency.replace(',',''))
		string_amount_used_in_constituency = amount_used_in_constituency.replace('ZMW','')
		clean_amount_used_in_constituency = float(string_amount_used_in_constituency.replace(',',''))
		amount_unsued = int_clean_allocated_amount - clean_amount_used_in_constituency
		constituency.total_amount_allocated_to_constituency = amount_allocated_to_constituency
		constituency.total_amount_unused = f"ZMW {amount_unsued:,}"
		constituency.save()
		
@frappe.whitelist()
def testing_api_calls(doc):             
	return(doc)

	
