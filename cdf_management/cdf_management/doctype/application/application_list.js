frappe.listview_settings['Application'] = {
    /*add_fields: ["sex"],
    filters: [
        ['sex', '=', 'Male']
    ]*/
}

// // Get the list view wrapper element
// var wrapper = $('.list-wrapper');
// var assignments = []
// // Get the list view instance
// var list_view = wrapper.list_view;

// // Define the filter criteria
// var filters = [
    
// ];

// frappe.db.get_list('Assignment', {
//     //fields: ['subject', 'description'],
//     filters: {
//         'user':frappe.session.user
//     }
// }).then(records => {
//     var outS = ''
//     records.forEach(element => {
//         outS += element.name + ','
//     });

//     console.log(outS)
//     filters.push(['Assignment', 'in', outS])
// })
// // Make the API call to get the filtered data
// frappe.listview_settings['Application'] = {
 
// 	filters: filters,
// };
// frappe.msgprint("123");