# Copyright (c) 2023, Alphazen Technoliginologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class SummaryReport(Document):
	
	def before_save(self):
  
		# fields_map = {
		# 	'Secondary School Bursaries':{'secondary_beneficiaries_male','secondary_beneficiaries_female'},
		# 	'Skill Development Bursaries': {'skills_development_beneficiaries_male', 'skills_development_beneficiaries_female'},
		# 	'Community Project': {'community_development_total'},
		# 	'Community Loans': {'loans_youth_groups','loans_women_groups',
        #      'loans_community_clubs','loans_cooperatives','loans_businesses','loans_companies',
        #      'loans_total_amount_disbursed'},
		# 	'Community Grants': {'grants_youth_groups','grants_women_groups','grants_community_clubs',
        #       'grants_cooperatives','grants_businesses','grants_companies','grants_total_amount_disbursed'},
		# }
  
		action_map = {
			'Secondary School Bursaries': self.evaluate_seconary_school,
			'Skill Development Bursaries': self.evaluate_skills,
			'Community Project': self.evaluate_com_project,
			'Community Loans': self.evaluate_loans,
			'Community Grants': self.evaluate_grants,
		}

		fields = ['secondary_beneficiaries_male','secondary_beneficiaries_female','skills_development_beneficiaries_male', 'skills_development_beneficiaries_female'
            ,'community_development_total','loans_youth_groups','loans_women_groups',
              'loans_community_clubs','loans_cooperatives','loans_businesses','loans_companies',
              'loans_total_amount_disbursed','grants_youth_groups','grants_women_groups','grants_community_clubs',
              'grants_cooperatives','grants_businesses','grants_companies','grants_total_amount_disbursed','skills_development_beneficiaries_total','secondary_beneficiaries_total'
              ,'skills_development_total_amount_disbursed', "community_development_total_amount_disbursed",'secondary_school_total_amount_disbursed']
  
		# Reset values
		for f in fields:
			setattr(self,f,0)
		level = str(self.level)
		if level == "Country":
			fields_to_copy = [	
					"grants_youth_groups",
					"grants_cooperatives",
					"grants_women_groups",
					"grants_community_clubs",
					"grants_businesses",
					"grants_companies",
					'grants_total_amount_disbursed',
					"loans_youth_groups",
					"loans_cooperatives", 
					"loans_women_groups", 
					"loans_community_clubs",
					"loans_businesses",
					"loans_companies",
					'loans_total_amount_disbursed',
					'secondary_beneficiaries_male',
					"secondary_beneficiaries_female",
					"secondary_beneficiaries_total",
					'secondary_school_total_amount_disbursed',
					'skills_development_beneficiaries_male',
					"skills_development_beneficiaries_female",
					"skills_development_beneficiaries_total",
					'skills_development_total_amount_disbursed',
					"community_development_total",
					"community_development_total_amount_disbursed"
     		]
			sums = frappe.db.get_list("Summary Report", filters={"level":"Province"})
			actual_summaries = [frappe.get_doc("Summary Report",x.name) for x in sums]
			
			for summary in actual_summaries:
				for f in fields_to_copy:
					setattr(self,f,getattr(summary,f))
		else:
			document_type = level.lower()
			retrieved_doc = getattr(self,document_type)
			applications_names = []
			applications_names = frappe.db.get_list('Application', filters={document_type : retrieved_doc}) 
			applications = [frappe.get_doc('Application',x.name) for x in applications_names]
			temp = {}
			for application in applications:
				if application.docstatus == 1:
					res = action_map[application.type](application)
					# frappe.msgprint(str(res))
					# frappe.msgprint("*"*10)
					for key in res.keys():

						if key in temp.keys():
							temp[key] += res[key]
							# setattr(self,key,getattr(self,key)+res[key])
						else:
							temp[key] = res[key]
			for key in temp.keys():
				frappe.msgprint(temp[key])
				setattr(self,key,temp[key])
	
	def evaluate_grants(self,application):
		group_types= {'Youth Group': "grants_youth_groups", 
                'Cooperative': "grants_cooperatives", 
                'Women Group': "grants_women_groups", 
                'Community Club': "grants_community_clubs"
                ,'Business': "grants_businesses", 
                'Company': "grants_companies"
                    }
		output = {
      	 'grants_total_amount_disbursed':application.amount,
		group_types[application.group_type]:1
       	}
		return output

	def evaluate_loans(self,application):
		group_types= {'Youth Group': "loans_youth_groups", 
                'Cooperative': "loans_cooperatives", 
                'Women Group': "loans_women_groups", 
                'Community Club': "loans_community_clubs"
                ,'Business': "loans_businesses", 
                'Company': "loans_companies"
                    }
		output = {
      	'loans_total_amount_disbursed':application.amount,
		group_types[application.group_type]:1
       	}
		return output
	
	def evaluate_seconary_school(self,application):
		sec_map = {"Male":'secondary_beneficiaries_male',
             		"Female": "secondary_beneficiaries_female"}
		
		out = {"secondary_beneficiaries_total":1, sec_map[application.sex]:1,'secondary_school_total_amount_disbursed':application.amount}
		return out
	def evaluate_skills(self,application):
		sec_map = {"Male":'skills_development_beneficiaries_male',
         		"Female": "skills_development_beneficiaries_female"}
	
		out = {"skills_development_beneficiaries_total":1, sec_map[application.sex]:1, 'skills_development_total_amount_disbursed':application.amount}
		return out

	def evaluate_com_project(self,application):
		return {"community_development_total":1,
          "community_development_total_amount_disbursed": application.amount
          }
	

	
	