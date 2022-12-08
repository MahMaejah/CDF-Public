// Copyright (c) 2022, Alphazen Technoliginologies and contributors
// For license information, please see license.txt

frappe.ui.form.on('Ward', {
	before_save: function(frm){
	    function add_total(child_table,total){
	            let table = child_table;
	            if(table){
	                var arr = [];
                    for (let K of table){
                        console.log(K.amount)
                         arr.push(K.amount)  
                    }
                    const initialValue = 0;
                    const sum = arr.reduce(
                        (previousValue, currentValue) => previousValue + currentValue,
                        initialValue
                      );
                    frm.set_value(total,'ZMW ' + sum)  
    	       }
                
	    }
	    add_total(frm.doc.secondary_school,'secondary_school_total_amount_disbursed');
	    add_total(frm.doc.skills_development,'skills_development_total_amount_disbursed')
	    add_total(frm.doc.community_projects,'community_projects_total_amount_disbursed')
	    add_total(frm.doc.grants,'grants_total_amount_disbursed')
	    add_total(frm.doc.loans,'loans_total_amount_disbursed')

      function add_group_type(group_type,field_name){
        const table1 = frm.doc.grants;
        const table2 = frm.doc.loans;
        if(table1 && table2){
          const child_table = table1.concat(table2)
	                var arr = [];
                  var arr1 = [];
                    for (let K of child_table){
                         arr.push(K.group_type)
                         arr1.push(K.response) 
                    }
        const total_number_projects = arr.length;
        frm.set_value("total_number_of_project_submitted",total_number_projects)
        const count0 = arr1.reduce((count0,type) => type === "Accepted" ? count0 +1: count0, 0)
        frm.set_value("total_number_of_projects_approved",count0)
        const count = arr.reduce((count,type) => type === group_type ? count +1: count, 0)
        frm.set_value(field_name,count)

      }
    }
    add_group_type("Cooperative","total_number_of_cooperative")
    add_group_type("Youth Group","total_number_of_youth_groups")
    add_group_type("Women Group","total_number_of_women_groups")
    add_group_type("Community Club","total_number_of_community_clubs")
    add_group_type("Community Club","total_number_of_community_projects")
    add_group_type("Company","total_number_of_companies")
    add_group_type("Business","total_number_of_businesses")
	    
	   const total_amount_disbursed = [frm.doc.secondary_school_total_amount_disbursed,frm.doc.skills_development_total_amount_disbursed,frm.doc.community_projects_total_amount_disbursed,frm.doc.grants_total_amount_disbursed,frm.doc.loans_total_amount_disbursed]
     console.log(total_amount_disbursed)
     if (!total_amount_disbursed.includes(undefined)){
     const sum_total = []
     total_amount_disbursed.forEach(amt => {
      const clean_amt = amt.match(/\d+/)
      sum_total.push(parseInt(clean_amt[0]))
    });
    console.log(sum_total)
	    const initialValue = 0;
      const sum = sum_total.reduce(
          (previousValue, currentValue) => previousValue + currentValue,
          initialValue
        );
      frm.set_value("total_amount_disbursed",'ZMW ' + sum) 
     }
   }
});
