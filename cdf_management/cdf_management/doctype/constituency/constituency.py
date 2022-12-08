# Copyright (c) 2022, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
import re
from frappe.model.document import Document

class Constituency(Document):
	pass
	def validate(self):
		self.calculate_total()
		self.calculate_gender_total()
	@frappe.whitelist()
	def calculate_total(self):
		ward_data = frappe.db.get_list('Ward',
					filters={
						'constituency': self.constituency_name
					},
					fields=['ward_name','secondary_school_total_amount_disbursed','skills_development_total_amount_disbursed','grants_total_amount_disbursed','loans_total_amount_disbursed'],)
		
		sum_total = 0
		sum_totals = {
			'secondary_school_total_amount_disbursed': 0,
			'skills_development_total_amount_disbursed': 0,
			'grants_total_amount_disbursed': 0,
			'loans_total_amount_disbursed': 0,
		}
		for d in ward_data:
			frappe.msgprint(str(d.ward_name))
			# d_dict = d.__dict__
			amounts = {
				'secondary_school_total_amount_disbursed': d.secondary_school_total_amount_disbursed,
				'skills_development_total_amount_disbursed': d.skills_development_total_amount_disbursed,
				'grants_total_amount_disbursed': d.grants_total_amount_disbursed,
				'loans_total_amount_disbursed': d.loans_total_amount_disbursed
			}

			# frappe.msgprint("Dict here")
			# frappe.msgprint(str(d))
			for amount in amounts.items(): #(k,v)
			# amount = d.skills_development_total_amount_disbursed
				# frappe.msgprint(amount[1])
				if amount[1] != None:
					num = amount[1].split(' ')[1]
					sum_totals[amount[0]] = sum_totals[amount[0]] + int(num)	
		total = str(sum_totals)
		frappe.msgprint(total)
		self.secondary_school_total_amount_disbursed = sum_totals['secondary_school_total_amount_disbursed']
		self.skills_development_total_amount_disbursed = sum_totals['skills_development_total_amount_disbursed']
		self.loans_total_amount_disbursed = sum_totals['loans_total_amount_disbursed']
		self.grants_total_amount_disbursed = sum_totals['grants_total_amount_disbursed']
		return total
	@frappe.whitelist()
	def calculate_gender_total(self):
		ward_data = frappe.db.get_list('Ward',
					filters={
						'constituency': self.constituency_name
					},
					fields=['ward_name'],)

		males = 0
		females = 0

		for d in ward_data:
			doc = frappe.get_doc('Ward', d.ward_name)
			#doc_dict = doc.__dict__
			secondary_school_field = doc.secondary_school
			table = doc.secondary_school
			frappe.msgprint(str(table))
			frappe.errprint(str(table))
			
			for t in table:
				frappe.msgprint(t.sex)
				if t.sex != "":
					if t.sex == "Male":
						males += 1

					else:
						females += 1

			frappe.msgprint(f'Males: {males} Females: {females}')
			return table
