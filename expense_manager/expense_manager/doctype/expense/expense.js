// Copyright (c) 2025, lidia and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Expense", {
//  	//refresh(frm) {
// 	//},
//     onload: function(frm){
//         frm.set_df_property("expense_date","max_date",frappe.datetime.get_today());
//     }
// });
frappe.ui.form.on("Expense", {
    refresh: function (frm) {
        frappe.realtime.on("expense_added", (data) => {
            console.log("New expense added:", data);
            frappe.show_alert({
                message: `Expense ${data.expense_id} added with amount ${data.amount}`,
                indicator: 'green'
            });
        });
    }
});

