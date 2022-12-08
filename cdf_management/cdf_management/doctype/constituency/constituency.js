// Copyright (c) 2022, Alphazen Technoliginologies and contributors
// For license information, please see license.txt



frappe.ui.form.on('Constituency', {
	// refresh: function(frm) {
		// frappe.call({
		// 	method: "cdf_management.cdf_management.doctype.constituency.constituency.calculate_total", 
		// 	args: {
		// 		doctype: 'constituency',
		// 		name: frm.doc.constituency_name
		// 	},
		// 	callback: function(r) {
		// 		console.log(r.message)
		// 	}
		// });
		// frappe.call({
		// 	method: "cdf_management.cdf_management.doctype.constituency.constituency.calculate_gender_total",
		// 	args: {
		// 		doctype: 'constituency',
		// 		name: frm.doc.constituency_name
		// 	}, 
		// 	callback: function(r) {
		// 		console.log(r.message)
		// 	}
		// });
	// 	const cons_name = frm.doc.constituency_name;
	// 	frappe.db.get_list('Ward', {
	// 		fields: ['ward_name','secondary_school_total_amount_disbursed','skills_development_total_amount_disbursed','grants_total_amount_disbursed','loans_total_amount_disbursed'],
	// 		filters: {
	// 			constituency: cons_name
	// 		}
	// 	}).then(records => {
	// 			const genderCount = {
	// 				male: 0,
	// 				female: 0
	// 			}
	// 		const count = {};
	// 		for(let k of records){
	// 			const w_name = k.ward_name
	// 			frappe.db.get_doc('Ward', w_name)
	// 			.then(doc => {
	// 				const s_table = doc.secondary_school
	// 				for(let g of s_table){
	// 					if (g.sex === "Male"){
	// 						genderCount.male += 1;
	// 					} else {
	// 						genderCount.female += 1;
	// 					}
	// 					if (count[g.sex]) {
	// 						count[g.sex] += 1;
	// 					} else {
	// 						count[g.sex] = 1;
	// 					}
	// 				}
					
	// 			})
	// 		}
	// 		console.log("Obj:",genderCount)
	// 		var childTable = cur_frm.add_child("bursaries_secondary_school_beneficiaries");
	// 		childTable.male = genderCount.male;
	// 		childTable.female = genderCount.female;
	// 		childTable.total = genderCount.male += genderCount.female;
	// 		cur_frm.refresh_fields("bursaries_secondary_school_beneficiaries");

	// 		const total_amount_secondary = []
	// 		for (let i of records){
	// 			if(i.secondary_school_total_amount_disbursed !== null){
	// 				total_amount_secondary.push(i.secondary_school_total_amount_disbursed)
	// 			}
	// 		}
	// 		const clean_secondary_total =[]
	// 		total_amount_secondary.forEach(amt => {
	// 			const clean_amt = amt.match(/\d+/)
	// 			clean_secondary_total.push(parseInt(clean_amt[0]))
	// 		  });
	// 		console.log(clean_secondary_total)
	// 		const initialValue = 0;
	// 		const sum = clean_secondary_total.reduce(
	// 			(previousValue, currentValue) => previousValue + currentValue,
	// 			initialValue
	// 			);
    //   			frm.set_value("secondary_school_total_amount_disbursed",'ZMW ' + sum) 
	// 			console.log(sum)
	//	})
	// 	frappe.db.get_doc('Ward', null, { constituency: cons_name  })
    // .then(doc => {
    //     console.log(doc)
	// 	const arr = doc.secondary_school;
	// 	const new_arr = []
	// 	for(let g of arr){
	// 	new_arr.push(g.sex)
	// 	}

	// 	console.log(doc.secondary_school_total_amount_disbursed)

    // })

	// }
});
