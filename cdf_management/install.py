import json
import os
import frappe
from frappe.utils import cint
import datetime

@frappe.whitelist()
def create_entry_template():
    temp = {
        
    }
    
    # TODO make stuff happen here
    wards = frappe.db.get_all("Ward",fields=['name','district','ward_number','ward_name','name_of_ward_councilor','province','constituency'])
    constituenies = frappe.db.get_all("Constituency",fields=['name','constituency_name','constituency_number','name_of_member_of_parliament','province','district'])
    district = frappe.db.get_all("District",fields=['name','district_name','mayorcouncil_chairperson','province'])
    provinces = frappe.db.get_all("Province",fields=['name','provincial_minister','name_of_province'])
    temp['Province'] = provinces
    temp['Constituency'] = constituenies
    temp['District'] = district
    temp['Ward'] = wards
    f = open("cdf_data_template.json",'x')
    json.dump(temp,f)
    f.close()
        
    return str(wards[:5])
    # TODO save json here
    


def create_from_template(key):
    f = open("cdf_data_template.json",'r')
    data = json.load(f)
    f.close()
    current_year = datetime.datetime.now().year
    doc_data = data[key]
    for d_data in doc_data:
        temp = {"doctype":key}
        for k in list(d_data.keys()):
            #setattr(new_doc,k,d_data[k])
            temp[k] = d_data[k]
        if frappe.db.exists(temp):
            continue
        new_doc = frappe.get_doc(temp)
        new_doc.name += " - " + str(current_year)
        new_doc.flags.ignore_validate = True
        new_doc.insert()
        frappe.msgprint(str(new_doc.__dict__))
        frappe.msgprint(f"Created {new_doc.name} under {key}s")
    frappe.db.commit()

@frappe.whitelist()
def create_provinces():
    create_from_template("Province")
    

@frappe.whitelist()
def create_constituencies():
    create_from_template("Constituency")

    

@frappe.whitelist()
def create_districts():
    create_from_template("District")

    

@frappe.whitelist()
def create_wards():
    f = open("cdf_data_template.json",'r')
    data = json.load(f)
    f.close()
    current_year = datetime.datetime.now().year
    doc_data = data["Ward"]
    
    count = 0
    commit_rate = 10
    # return str(frappe.db.sql("SHOW TABLES;",as_dict=0))
    for d_data in doc_data:
        # temp = {"doctype":"Ward"}
        temp = {}
        for k in list(d_data.keys()):
            #setattr(new_doc,k,d_data[k])
            temp[k] = d_data[k]
        # if frappe.db.exists(temp):
        #     continue
        values = {"values": tuple(temp.values())}
        frappe.db.sql(
            f'''INSERT INTO tabWard (name,district, ward_number, ward_name,name_of_ward_councilor, province, constituency) VALUES %(values)s;''',values=values
        )
        # new_doc = frappe.get_doc(temp)
        # new_doc.name += " - " + str(current_year)
        
        # new_doc.flags.ignore_validate = True
        # new_doc.flags.ignote_on_update = True
        # new_doc.insert()
        # frappe.msgprint(str(new_doc.__dict__))
        # frappe.msgprint(f"Created {new_doc.name} under "Wards")
        
        frappe.db.commit()

@frappe.whitelist()
def after_install():
    print("Done with installation")
    create_provinces()
    create_districts()
    create_districts()
    create_wards()
    # print("use the following commands in the browser")
    # print("site/api/method/cdf_management.api.create_provinces")
    # print("site/api/method/cdf_management.api.create_constituencies")
    # print("site/api/method/cdf_management.api.create_districts")
    # print("site/api/method/cdf_management.api.create_wards")