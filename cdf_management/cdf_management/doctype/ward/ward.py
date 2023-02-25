# Copyright (c) 2022, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

import frappe
import datetime
import re
from frappe.model.document import Document

class Ward(Document):

	#Todo convert data in ward.js to python
	# def add_total(self, child_table, total):
	# 	table = child_table
	# 	if table:
	# 		arr = []
	# 		for k in table:
	# 			if str(k.response) == "Accepted":
	# 				arr.append(k.amount)
	# 		initial_value = 0
	# 		_sum = 0
	# 		_sum = sum(arr, initial_value)
			
			# self.set_value(total, 'ZMW ' + _sum)

			# set_value('Ward', self.name, total, 'ZMW ' + str(_sum))
			# frappe.msgprint(str())
			# self.set_value(total, 'ZMW ' + str(_sum))
	# 		setattr(self, total, 'ZMW ' + str(_sum))

	
	# def add_group_type(self, group_type, field_name):
	# 	table1 = self.grants
	# 	table2 = self.loans
	# 	if table1 and table2:
	# 		child_table = table1 + table2
	# 		arr = []
	# 		arr1 = []
	# 		for k in child_table:
	# 			arr.append(k.group_type)
	# 			arr1.append(k.response)

	# 		total_number_projects = len(arr)
	# 		self.total_number_of_project_submitted = total_number_projects
	# 		# self.set_value("total_number_of_project_submitted", total_number_projects)
	# 		count0 = arr1.count("Accepted")
	# 		self.total_number_of_projects_approved = count0
	# 		# self.set_value("total_number_of_projects_approved", count0)
	# 		count = arr.count(group_type)
	# 		# match field_name:
	# 		# 	case "total_number_of_cooperative":
	# 		setattr(self, field_name, count)
	# 		# self.set_value(field_name, count)
	
	# def validate(self):
		
	# 	frappe.msgprint("Valitaded")
	# 	self.add_total(self.secondary_school, 'secondary_school_total_amount_disbursed')
	# 	self.add_total(self.skills_development, 'skills_development_total_amount_disbursed')
	# 	self.add_total(self.community_projects, 'community_projects_total_amount_disbursed')
	# 	self.add_total(self.grants, 'grants_total_amount_disbursed')
	# 	self.add_total(self.loans, 'loans_total_amount_disbursed')

	# 	self.add_group_type("Cooperative","total_number_of_cooperative")
	# 	self.add_group_type("Youth Group","total_number_of_youth_groups")
	# 	self.add_group_type("Women Group","total_number_of_women_groups")
	# 	self.add_group_type("Community Club","total_number_of_community_clubs")
	# 	self.add_group_type("Community Club","total_number_of_community_projects")
	# 	self.add_group_type("Company","total_number_of_companies")
	# 	self.add_group_type("Business","total_number_of_businesses")

	# 	total_amount_disbursed = [
	# 		self.secondary_school_total_amount_disbursed,
	# 		self.skills_development_total_amount_disbursed,
	# 		self.community_projects_total_amount_disbursed,
	# 		self.grants_total_amount_disbursed,
	# 		self.loans_total_amount_disbursed
	# 	]
		# print(total_amount_disbursed)
		# if None not in total_amount_disbursed:
		# 	sum_total = []
		# 	for amt in total_amount_disbursed:
		# 		clean_amt = re.search(r"\d+", amt)
		# 		sum_total.append(int(clean_amt.group()))
			# frappe.msgprint(str(sum_total))
			# initial_value = 0
			# _sum = 0
			# _sum = sum(sum_total)
			# self.total_amount_disbursed = 'ZMW ' + str(_sum)
			# frappe.db.set_value('Ward', self.name,"total_amount_disbursed", 'ZMW ' + str(_sum))



	def on_update(self):
		pass
		#self.calculate_total()

	def calculate_total(self):
		self.wards_in_constituency_total_secondary_school_amount_disbursed()
		self.wards_in_constituency_skills_development_beneficiaries_totals()
		self.wards_in_constituency_community_projects_total()
		self.wards_in_constituency_grants_totals()
		self.wards_in_constituency_loans_totals()
		self.wards_in_district_total_secondary_school_amount_disbursed()
		self.wards_in_district_skills_development_beneficiaries_totals()
		self.wards_in_district_community_projects_total()
		self.wards_in_district_grants_totals()
		self.wards_in_district_loans_totals()
		self.wards_in_province_total_secondary_school_amount_disbursed()
		self.wards_in_province_skills_development_beneficiaries_totals()
		self.wards_in_province_community_projects_total()
		self.wards_in_province_grants_totals()
		self.wards_in_province_loans_totals()
		self.wards_in_country_grants_totals()
		self.wards_in_country_loans_total()
		





	def wards_in_constituency_grants_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0
		
		total_amount = 0.00

		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		
		for constituency_ward in constituency_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Youth Group", "parentfield": "grants",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Women Group", "parentfield": "grants",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Community Club", "parentfield": "grants",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Cooperative", "parentfield": "grants",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Company", "parentfield": "grants",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Business", "parentfield": "grants",'response': "Accepted"})

			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "grants_total_amount_disbursed").replace("ZMW", ""))
		
		frappe.db.set_value("Constituency", self.constituency, "grants_youth_groups", youth_groups)
		frappe.db.set_value("Constituency", self.constituency, "grants_women_groups", women_groups)
		frappe.db.set_value("Constituency", self.constituency, "grants_community_clubs", community_clubs)
		frappe.db.set_value("Constituency", self.constituency, "grants_cooperatives", cooperatives)
		frappe.db.set_value("Constituency", self.constituency, "grants_businesses", businesses)
		frappe.db.set_value("Constituency", self.constituency, "grants_companies", companies)

		frappe.db.set_value("Constituency", self.constituency, "grants_total_amount_disbursed", f"ZMW {total_amount:,}")
	
	def wards_in_constituency_loans_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		
		for constituency_ward in constituency_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Youth Group", "parentfield": "loans",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Women Group", "parentfield": "loans",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Community Club", "parentfield": "loans",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Cooperative", "parentfield": "loans",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Company", "parentfield": "loans",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': constituency_ward.name, 'group_type': "Business", "parentfield": "loans",'response': "Accepted"})

			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "loans_total_amount_disbursed").replace("ZMW", ""))


		frappe.db.set_value("Constituency", self.constituency, "loans_youth_groups", youth_groups)
		frappe.db.set_value("Constituency", self.constituency, "loans_women_groups", women_groups)
		frappe.db.set_value("Constituency", self.constituency, "loans_community_clubs", community_clubs)
		frappe.db.set_value("Constituency", self.constituency, "loans_cooperatives", cooperatives)
		frappe.db.set_value("Constituency", self.constituency, "loans_businesses", businesses)
		frappe.db.set_value("Constituency", self.constituency, "loans_companies", companies)

		frappe.db.set_value("Constituency", self.constituency, "loans_total_amount_disbursed", f"ZMW {total_amount:,}")


	def wards_in_district_grants_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		district_wards = frappe.get_all("Ward", {"district": self.district})
		
		for district_ward in district_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Youth Group", "parentfield": "grants",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Women Group", "parentfield": "grants",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Community Club", "parentfield": "grants",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Cooperative", "parentfield": "grants",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Company", "parentfield": "grants",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Business", "parentfield": "grants",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", district_ward, "grants_total_amount_disbursed").replace("ZMW", ""))


		frappe.db.set_value("District", self.district, "grants_youth_groups", youth_groups)
		frappe.db.set_value("District", self.district, "grants_women_groups", women_groups)
		frappe.db.set_value("District", self.district, "grants_community_clubs", community_clubs)
		frappe.db.set_value("District", self.district, "grants_cooperatives", cooperatives)
		frappe.db.set_value("District", self.district, "grants_businesses", businesses)
		frappe.db.set_value("District", self.district, "grants_companies", companies)

		frappe.db.set_value("District", self.district, "grants_total_amount_disbursed", f"ZMW {total_amount:,}")


	def wards_in_district_loans_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		district_wards = frappe.get_all("Ward", {"district": self.district})
		
		for district_ward in district_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Youth Group", "parentfield": "loans",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Women Group", "parentfield": "loans",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Community Club", "parentfield": "loans",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Cooperative", "parentfield": "loans",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Company", "parentfield": "loans",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': district_ward.name, 'group_type': "Business", "parentfield": "loans",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", district_ward, "loans_total_amount_disbursed").replace("ZMW", ""))


		frappe.db.set_value("District", self.district, "loans_youth_groups", youth_groups)
		frappe.db.set_value("District", self.district, "loans_women_groups", women_groups)
		frappe.db.set_value("District", self.district, "loans_community_clubs", community_clubs)
		frappe.db.set_value("District", self.district, "loans_cooperatives", cooperatives)
		frappe.db.set_value("District", self.district, "loans_businesses", businesses)
		frappe.db.set_value("District", self.district, "loans_companies", companies)

		frappe.db.set_value("District", self.district, "loans_total_amount_disbursed", f"ZMW {total_amount:,}")

	def wards_in_province_grants_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		province_wards = frappe.get_all("Ward", {"province": self.province})
		
		for province_ward in province_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Youth Group", "parentfield": "grants",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Women Group", "parentfield": "grants",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Community Club", "parentfield": "grants",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Cooperative", "parentfield": "grants",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Company", "parentfield": "grants",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Business", "parentfield": "grants",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", province_ward, "grants_total_amount_disbursed").replace("ZMW", ""))


		frappe.db.set_value("Province", self.province, "grants_youth_groups", youth_groups)
		frappe.db.set_value("Province", self.province, "grants_women_groups", women_groups)
		frappe.db.set_value("Province", self.province, "grants_community_clubs", community_clubs)
		frappe.db.set_value("Province", self.province, "grants_cooperatives", cooperatives)
		frappe.db.set_value("Province", self.province, "grants_businesses", businesses)
		frappe.db.set_value("Province", self.province, "grants_companies", companies)

		frappe.db.set_value("Province", self.province, "grants_total_amount_disbursed", f"ZMW {total_amount:,}")


	def wards_in_province_loans_totals(self):
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		province_wards = frappe.get_all("Ward", {"province": self.province})
		
		for province_ward in province_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Youth Group", "parentfield": "loans",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Women Group", "parentfield": "loans",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Community Club", "parentfield": "loans",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Cooperative", "parentfield": "loans",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Company", "parentfield": "loans",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': province_ward.name, 'group_type': "Business", "parentfield": "loans",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", province_ward, "loans_total_amount_disbursed").replace("ZMW", ""))


		frappe.db.set_value("Province", self.province, "loans_women_groups", women_groups)
		frappe.db.set_value("Province", self.province, "loans_community_clubs", community_clubs)
		frappe.db.set_value("Province", self.province, "loans_youth_groups", youth_groups)
		frappe.db.set_value("Province", self.province, "loans_cooperatives", cooperatives)
		frappe.db.set_value("Province", self.province, "loans_businesses", businesses)
		frappe.db.set_value("Province", self.province, "loans_companies", companies)

		frappe.db.set_value("Province", self.province, "loans_total_amount_disbursed", f"ZMW {total_amount:,}")
	# @staticmethod
	def wards_in_country_loans_total(self):
		#loans
		today = datetime.date.today()
		current_year = today.year
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		country_wards = frappe.get_all("Ward", {"year": current_year })
		
		for country_ward in country_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Youth Group", "parentfield": "loans",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Women Group", "parentfield": "loans",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Community Club", "parentfield": "loans",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Cooperative", "parentfield": "loans",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Company", "parentfield": "loans",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Business", "parentfield": "loans",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", country_ward, "loans_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_women_groups", women_groups)
		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_community_clubs", community_clubs)
		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_youth_groups", youth_groups)
		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_cooperatives", cooperatives)
		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_businesses", businesses)
		frappe.db.set_value("Country Summary", "2023 Community Development Fund Summary", "loans_companies", companies)

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "loans_total_amount_disbursed", f"ZMW {total_amount:,}")
		self.wards_in_country_skills_development_beneficiaries_totals(current_year,country_wards)
		self.wards_in_country_total_secondary_school(current_year, country_wards)
		self.wards_in_country_community_projects_total(current_year, country_wards)
		self.grand_total_per_summary(current_year,country_wards)
	def wards_in_country_grants_totals(self):
		today = datetime.date.today()
		current_year = today.year
		youth_groups = 0
		women_groups = 0
		community_clubs = 0
		cooperatives = 0
		businesses = 0
		companies = 0

		total_amount = 0.00

		country_wards = frappe.get_all("Ward", {"year": current_year })
		
		for country_ward in country_wards:
			youth_groups += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Youth Group", "parentfield": "grants",'response': "Accepted"})
			women_groups += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Women Group", "parentfield": "grants",'response': "Accepted"})
			community_clubs += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Community Club", "parentfield": "grants",'response': "Accepted"})
			cooperatives += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Cooperative", "parentfield": "grants",'response': "Accepted"})
			businesses += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Company", "parentfield": "grants",'response': "Accepted"})
			companies += frappe.db.count("Community EmpowermentTB", {'parent': country_ward.name, 'group_type': "Business", "parentfield": "grants",'response': "Accepted"})
		
			total_amount += float(frappe.db.get_value("Ward", country_ward, "grants_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_women_groups", women_groups)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_community_clubs", community_clubs)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_youth_groups", youth_groups)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_cooperatives", cooperatives)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_businesses", businesses)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_companies", companies)

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grants_total_amount_disbursed", f"ZMW {total_amount:,}")




	def wards_in_constituency_skills_development_beneficiaries_totals(self):
		#Calculate total amount disbursed for wards in constituency
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		total_amount = 0.00

		for constituency_ward in constituency_wards:
			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "skills_development_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Constituency", self.constituency, "skills_development_total_amount_disbursed", f"ZMW {total_amount:,}")

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
	
	def wards_in_district_skills_development_beneficiaries_totals(self):
		#Calculate total amount disbursed for wards in district
		district_wards = frappe.get_all("Ward", {"district": self.district})
		total_amount = 0.00

		for district_ward in district_wards:
			total_amount += float(frappe.db.get_value("Ward", district_ward, "skills_development_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("District", self.district, "skills_development_total_amount_disbursed", f"ZMW {total_amount:,}")

		#Calculate total male and female for wards in district
		total_male_in_district = 0
		total_female_in_district = 0

		for district_ward in district_wards:
			total_male_in_district += frappe.db.count("Skills DevelopmentTB", {'parent': district_ward.name, 'sex': 'Male'})
		
		for district_ward in district_wards:
			total_female_in_district += frappe.db.count("Skills DevelopmentTB", {'parent': district_ward.name, 'sex': 'Female'})
		


		
		frappe.db.set_value("District", self.district, "skills_development_beneficiaries_male", total_male_in_district)
		frappe.db.set_value("District", self.district, "skills_development_beneficiaries_female", total_female_in_district)
		frappe.db.set_value("District", self.district, "skills_development_beneficiaries_total", total_male_in_district + total_female_in_district)
	
	def wards_in_province_skills_development_beneficiaries_totals(self):
		#Calculate total amount disbursed for wards in district
		province_wards = frappe.get_all("Ward", {"province": self.province})
		total_amount = 0.00

		for province_ward in province_wards:
			total_amount += float(frappe.db.get_value("Ward", province_ward, "skills_development_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Province", self.province, "skills_development_total_amount_disbursed", f"ZMW {total_amount:,}")

		#Calculate total male and female for wards in district
		total_male_in_province = 0
		total_female_in_province = 0

		for province_ward in province_wards:
			total_male_in_province += frappe.db.count("Skills DevelopmentTB", {'parent': province_ward.name, 'sex': 'Male'})
		
		for province_ward in province_wards:
			total_female_in_province += frappe.db.count("Skills DevelopmentTB", {'parent': province_ward.name, 'sex': 'Female'})
		


		
		frappe.db.set_value("Province", self.province, "skills_development_beneficiaries_male", total_male_in_province)
		frappe.db.set_value("Province", self.province, "skills_development_beneficiaries_female", total_female_in_province)
		frappe.db.set_value("Province", self.province, "skills_development_beneficiaries_total", total_male_in_province + total_female_in_province)
	
	def wards_in_country_skills_development_beneficiaries_totals(self,current_year,country_wards):
		#Calculate total amount disbursed for wards in district
		total_amount = 0.00

		for country_ward in country_wards:
			total_amount += float(frappe.db.get_value("Ward", country_ward, "skills_development_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "skills_development_total_amount_disbursed", f"ZMW {total_amount:,}")

		#Calculate total male and female for wards in district
		total_male_in_province = 0
		total_female_in_province = 0

		for country_ward in country_wards:
			total_male_in_province += frappe.db.count("Skills DevelopmentTB", {'parent': country_ward.name, 'sex': 'Male'})
		
		for country_ward in country_wards:
			total_female_in_province += frappe.db.count("Skills DevelopmentTB", {'parent': country_ward.name, 'sex': 'Female'})
		


		
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "skills_development_beneficiaries_male", total_male_in_province)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "skills_development_beneficiaries_female", total_female_in_province)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "skills_development_beneficiaries_total", total_male_in_province + total_female_in_province)
	

	def wards_in_constituency_total_secondary_school_amount_disbursed(self):
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		total_amount = 0.00
		for constituency_ward in constituency_wards:
			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "secondary_school_total_amount_disbursed").replace("ZMW", ""))

		constituency = frappe.get_doc("Constituency", self.constituency)
		constituency.secondary_school_total_amount_disbursed = f"ZMW {total_amount:,}"
		constituency.save()

		self.wards_in_constituency_total_secondary_school_male(constituency_wards)

	def wards_in_district_total_secondary_school_amount_disbursed(self):
		district_wards = frappe.get_all("Ward", {"district": self.district})
		total_amount = 0.00
		for district_ward in district_wards:
			total_amount += float(frappe.db.get_value("Ward", district_ward, "secondary_school_total_amount_disbursed").replace("ZMW", ""))

		district = frappe.get_doc("District", self.district)
		district.secondary_school_total_amount_disbursed = f"ZMW {total_amount:,}"
		district.save()

		self.wards_in_district_total_secondary_school_male(district_wards)

	def wards_in_province_total_secondary_school_amount_disbursed(self):
		province_wards = frappe.get_all("Ward", {"province": self.province})
		total_amount = 0.00
		for province_ward in province_wards:
			total_amount += float(frappe.db.get_value("Ward", province_ward, "secondary_school_total_amount_disbursed").replace("ZMW", ""))

		province = frappe.get_doc("Province", self.province)
		province.secondary_school_total_amount_disbursed = f"ZMW {total_amount:,}"
		province.save()

		self.wards_in_province_total_secondary_school_male(province_wards)

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

	def wards_in_district_total_secondary_school_male(self, district_wards):
		total_male_in_district = 0
		total_female_in_district = 0

		for district_ward in district_wards:
			total_male_in_district += frappe.db.count("Secondary SchoolTB", {'parent': district_ward.name, 'sex': 'Male'})

		for district_ward in district_wards:
			total_female_in_district += frappe.db.count("Secondary SchoolTB", {'parent': district_ward.name, 'sex': 'Female'})
		
		frappe.db.set_value("District", self.district, "secondary_beneficiaries_male", total_male_in_district)
		frappe.db.set_value("District", self.district, "secondary_beneficiaries_female", total_female_in_district)
		frappe.db.set_value("District", self.district, "secondary_beneficiaries_total", total_male_in_district + total_female_in_district)


	def wards_in_province_total_secondary_school_male(self, province_wards):
		total_male_in_province = 0
		total_female_in_province = 0

		for province_ward in province_wards:
			total_male_in_province += frappe.db.count("Secondary SchoolTB", {'parent': province_ward.name, 'sex': 'Male'})

		for province_ward in province_wards:
			total_female_in_province += frappe.db.count("Secondary SchoolTB", {'parent': province_ward.name, 'sex': 'Female'})
		
		frappe.db.set_value("Province", self.province, "secondary_beneficiaries_male", total_male_in_province)
		frappe.db.set_value("Province", self.province, "secondary_beneficiaries_female", total_female_in_province)
		frappe.db.set_value("Province", self.province, "secondary_beneficiaries_total", total_male_in_province + total_female_in_province)

	def wards_in_country_total_secondary_school(self, current_year,country_wards):
		total_male_in_country = 0
		total_female_in_country = 0
		total_amount = 0

		for country_ward in country_wards:
			total_amount += float(frappe.db.get_value("Ward", country_ward, "secondary_school_total_amount_disbursed").replace("ZMW", ""))
			total_male_in_country += frappe.db.count("Secondary SchoolTB", {'parent': country_ward.name, 'sex': 'Male'})
			total_female_in_country += frappe.db.count("Secondary SchoolTB", {'parent': country_ward.name, 'sex': 'Female'})
		
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "secondary_beneficiaries_male", total_male_in_country)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "secondary_beneficiaries_female", total_female_in_country)
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "secondary_beneficiaries_total", total_male_in_country + total_female_in_country)

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "secondary_school_total_amount_disbursed", F"ZMW {total_amount:,}")

	def wards_in_country_community_projects_total(self, current_year, country_wards):
		total = 0
		total_amount = 0.00
		for country_ward in country_wards:
			total += frappe.db.count("Community ProjectsTB", {'parent': country_ward.name, "parentfield": "community_projects",'response': "Accepted"})
			total_amount += float(frappe.db.get_value("Ward", country_ward, "community_projects_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "community_development_total_amount_disbursed", f"ZMW {total_amount:,}")
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "community_development_total", total)

	def wards_in_province_community_projects_total(self):
		province_wards = frappe.get_all("Ward", {"province": self.province})
		total = 0
		total_amount = 0.00
		for province_ward in province_wards:
			total += frappe.db.count("Community ProjectsTB", {'parent': province_ward.name, "parentfield": "community_projects",'response': "Accepted"})
			total_amount += float(frappe.db.get_value("Ward", province_ward, "community_projects_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Province", self.province, "community_development_total_amount_disbursed", f"ZMW {total_amount:,}")
		frappe.db.set_value("Province", self.province, "community_development_total", total)

	def wards_in_district_community_projects_total(self):
		district_wards = frappe.get_all("Ward", {"district": self.district})
		total = 0
		total_amount = 0.00
		for district_ward in district_wards:
			total += frappe.db.count("Community ProjectsTB", {'parent': district_ward.name, "parentfield": "community_projects",'response': "Accepted"})
			total_amount += float(frappe.db.get_value("Ward", district_ward, "community_projects_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("District", self.district, "community_development_total_amount_disbursed", f"ZMW {total_amount:,}")
		frappe.db.set_value("District", self.district, "community_development_total", total)

	def wards_in_constituency_community_projects_total(self):
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		total = 0
		total_amount = 0.00
		for constituency_ward in constituency_wards:
			total += frappe.db.count("Community ProjectsTB", {'parent': constituency_ward.name, "parentfield": "community_projects",'response': "Accepted"})
			total_amount += float(frappe.db.get_value("Ward", constituency_ward, "community_projects_total_amount_disbursed").replace("ZMW", ""))

		frappe.db.set_value("Constituency", self.constituency, "community_development_total_amount_disbursed", f"ZMW {total_amount:,}")
		frappe.db.set_value("Constituency", self.constituency, "community_development_total", total)

	def grand_total_per_summary(self, current_year,country_wards):
		constituency_grand_total = 0.00
		district_grand_total = 0.00
		province_grand_total = 0.00
		country_grand_total = 0.00
		amount_allocated_per_constituency = frappe.db.get_single_value('Allocation Settings', 'total_amount_allocated_per_constituency')
		amount_allocated_per_constituency = "ZMW0,0" if amount_allocated_per_constituency == None else amount_allocated_per_constituency
		constituency_wards = frappe.get_all("Ward", {"constituency": self.constituency})
		district_wards = frappe.get_all("Ward", {"district": self.district})
		province_wards = frappe.get_all("Ward", {"province": self.province})

		for constituency_ward in constituency_wards:
			constituency_grand_total += float(frappe.db.get_value("Ward", constituency_ward, "secondary_school_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", constituency_ward, "skills_development_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", constituency_ward, "community_projects_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", constituency_ward, "grants_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", constituency_ward, "loans_total_amount_disbursed").replace("ZMW", ""))
		for district_ward in district_wards:
			district_grand_total += float(frappe.db.get_value("Ward", district_ward, "secondary_school_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", district_ward, "skills_development_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", district_ward, "community_projects_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", district_ward, "grants_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", district_ward, "loans_total_amount_disbursed").replace("ZMW", ""))
		for province_ward in province_wards:
			province_grand_total += float(frappe.db.get_value("Ward", province_ward, "secondary_school_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", province_ward, "skills_development_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", province_ward, "community_projects_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", province_ward, "grants_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", province_ward, "loans_total_amount_disbursed").replace("ZMW", ""))
		for country_ward in country_wards:
			country_grand_total += float(frappe.db.get_value("Ward", country_ward, "secondary_school_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", country_ward, "skills_development_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", country_ward, "community_projects_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", country_ward, "grants_total_amount_disbursed").replace("ZMW", "")) + float(frappe.db.get_value("Ward", country_ward, "loans_total_amount_disbursed").replace("ZMW", ""))
  		
		constituency_grand_total = constituency_grand_total + float(frappe.db.get_value("Constituency", self.constituency, "clean_total"))
		district_grand_total = district_grand_total + float(frappe.db.get_value("Constituency", self.constituency, "clean_total"))
		province_grand_total = province_grand_total + float(frappe.db.get_value("Constituency", self.constituency, "clean_total"))
		country_grand_total = country_grand_total + float(frappe.db.get_value("Constituency", self.constituency, "clean_total"))
		string_amount = amount_allocated_per_constituency.replace("ZMW", "")
		amount_unused_per_constituecy = float(string_amount.replace(",", "")) - float(constituency_grand_total)
		frappe.db.set_value("Constituency", self.constituency, "grand_total", f" ZMW {constituency_grand_total:,}")
		frappe.db.set_value("Constituency", self.constituency, "constituency_total_amount_allocated", amount_allocated_per_constituency)
		frappe.db.set_value("Constituency", self.constituency, "constituency_total_amount_unused", f"ZMW {amount_unused_per_constituecy:,}")
		frappe.db.set_value("District", self.district, "grand_total", f" ZMW {district_grand_total:,}")
		frappe.db.set_value("Province", self.province, "grand_total", f" ZMW {province_grand_total:,}")
		frappe.db.set_value("Country Summary", F"{current_year} Community Development Fund Summary", "grand_total", F"ZMW {country_grand_total:,}")
