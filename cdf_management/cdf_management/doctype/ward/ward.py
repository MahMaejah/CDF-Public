# Copyright (c) 2022, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Ward(Document):
	def on_update(self):
		self.calculate_total()

	def calculate_total(self):
		self.wards_in_constituency_total_secondary_school_amount_disbursed()
		self.wards_in_constituency_skills_development_beneficiaries_totals()

	def wards_in_constituency_skills_development_beneficiaries_totals(self):
		#Calculate total amount disbursed for wards in constituency
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		total_amount = 0.00

		for constituency_ward in constituency_wards:
			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "skills_development_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Constituency", self.constituency, "skills_development_total_amount_disbursed", f"ZMW {total_amount}")

		#Calculate total male and female for wards in constituency
		total_male_in_constituency = 0
		total_female_in_constituency = 0

		for constituency_ward in constituency_wards:
			total_male_in_constituency += frappe.db.count("Skills DevelopmentTB", {'parent': constituency_ward.name, 'sex': 'Male'})
		
		for constituency_ward in constituency_wards:
			total_female_in_constituency += frappe.db.count("Skills DevelopmentTB", {'parent': constituency_ward.name, 'sex': 'Female'})
		
		frappe.db.set_value("Constituency", self.constituency, "skills_development_beneficiaries_male", total_male_in_constituency)
		frappe.db.set_value("Constituency", self.constituency, "skills_development_beneficiaries_female", total_female_in_constituency)
		frappe.db.set_value("Constituency", self.constituency, "skills_development_beneficiaries_total", total_male_in_constituency + total_female_in_constituency)
	
	def wards_in_constituency_total_secondary_school_amount_disbursed(self):
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		total_amount = 0.00
		for constituency_ward in constituency_wards:
			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "secondary_school_total_amount_disbursed").replace("ZMW", ""))

		constituency = frappe.get_doc("Constituency", self.constituency)
		constituency.secondary_school_total_amount_disbursed = f"ZMW {total_amount}"
		constituency.save()

		self.wards_in_constituency_total_secondary_school_male(constituency_wards)

	def wards_in_constituency_total_secondary_school_male(self, constituency_wards):
		total_male_in_constituency = 0
		total_female_in_constituency = 0

		for constituency_ward in constituency_wards:
			total_male_in_constituency += frappe.db.count("Secondary SchoolTB", {'parent': constituency_ward.name, 'sex': 'Male'})

		for constituency_ward in constituency_wards:
			total_female_in_constituency += frappe.db.count("Secondary SchoolTB", {'parent': constituency_ward.name, 'sex': 'Female'})
		
		frappe.db.set_value("Constituency", self.constituency, "secondary_beneficiaries_male", total_male_in_constituency)
		frappe.db.set_value("Constituency", self.constituency, "secondary_beneficiaries_female", total_female_in_constituency)
		frappe.db.set_value("Constituency", self.constituency, "secondary_beneficiaries_total", total_male_in_constituency + total_female_in_constituency)
