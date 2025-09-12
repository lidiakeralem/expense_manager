// Copyright (c) 2025, lidia and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Expense category", {
// 	refresh(frm) {

// 	},
// });


// frappe.ui.form.on('Expense Category', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Add Category'), function () {

//             let d = new frappe.ui.Dialog({
//                 title: 'Add Expense Category',
//                 size: 'small',
//                 fields: [
//                     {
//                         label: 'Category Name',
//                         fieldname: 'category_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
//                     {
//                         label: 'Description',
//                         fieldname: 'description',
//                         fieldtype: 'Small Text'
//                     }
//                 ],
//                 primary_action_label: 'Save',
//                 primary_action(values) {
//                     d.hide();

//                     frappe.show_alert({
//                         message: `Saving category "${values.category_name}"...`,
//                         indicator: 'blue'
//                     }, 3);

//                     frappe.call({
//                         method: 'expense_manager.expense_manager.api.add_expense_category',
//                         args: {
//                             category_name: values.category_name,
//                             description: values.description
//                         },
//                         callback: function (r) {
//                             if (r.message) {
//                                 frappe.msgprint({
//                                     title: __('Success'),
//                                     message: r.message,
//                                     indicator: 'green'
//                                 });
//                                 frm.reload_doc();
//                             } else {
//                                 frappe.msgprint({
//                                     title: __('Error'),
//                                     message: 'Failed to add Expense Category',
//                                     indicator: 'red'
//                                 });
//                             }
//                         }
//                     });
//                 }
//             });

//             d.show();
//         });
//     }
//  without backend
// frappe.ui.form.on('Expense Category', {
//     refresh: function (frm) {
//         frm.add_custom_button(__('Add Category'), function () {
//             let d = new frappe.ui.Dialog({
//                 title: 'Add Expense Category',
//                 fields: [
//                     { label: 'Category Name', fieldname: 'category_name', fieldtype: 'Data', reqd: 1 },
//                     { label: 'Description', fieldname: 'description', fieldtype: 'Small Text' }
//                 ],
//                 primary_action_label: 'Save',
//                 primary_action(values) {
//                     d.hide();

//                     frappe.call({
//                         method: 'expense_manager.expense_manager.api.add_expense_category',
//                         args: {
//                             category_name: values.category_name,
//                             description: values.description
//                         },
//                         callback: function (r) {
//                             frappe.msgprint(r.message || 'Done!');
//                             frm.reload_doc();
//                         }
//                     });
//                 }
//             });

//             d.show();
//         });
//     }
// });




// frappe.ui.form.on('Expense Category', {
//     refresh: function (frm) {
//         // ✅ Custom button for other work
//         frm.add_custom_button(__('Log Category Action'), function () {
//             let d = new frappe.ui.Dialog({
//                 title: 'Log Category Action',
//                 fields: [
//                     { label: 'Action Note', fieldname: 'action_note', fieldtype: 'Small Text', reqd: 1 }
//                 ],
//                 primary_action_label: 'Log',
//                 primary_action(values) {
//                     d.hide();

//                     frappe.call({
//                         method: 'expense_manager.expense_manager.api.log_category_action',
//                         args: {
//                             action_note: values.action_note
//                         },
//                         callback: function (r) {
//                             frappe.msgprint({
//                                 title: __('Success'),
//                                 message: r.message || 'Action logged!',
//                                 indicator: 'green'
//                             });
//                         }
//                     });
//                 }
//             });
//             d.show();
//         });
//     },

//     // ✅ Normal save
//     after_save: function (frm) {
//         frappe.msgprint({
//             title: __('Success'),
//             message: __('Thank you for adding the category "{0}"', [frm.doc.category_name]),
//             indicator: 'green'
//         });
//     }
// });

frappe.ui.form.on('Expense Category', {
    before_save: function (frm) {
        // Prevent infinite loop
        if (frm.confirmation_done) {
            frm.confirmation_done = false;  // reset for next save
            return;
        }

        frappe.validated = false;  // stop save until user confirms

        frappe.confirm(
            'Are you sure you want to save this Expense Category?',
            function () {
                // ✅ Yes → save, then go to list
                frm.confirmation_done = true;
                frappe.validated = true;
                frm.save().then(() => {
                    frappe.msgprint(__('Expense Category saved successfully!'));
                    frappe.set_route('List', 'Expense Category');
                });
            },
            function () {
                // ❌ No → cancel and go to list
                frappe.msgprint(__('Save Cancelled.'));
                frappe.set_route('List', 'Expense Category');
            }
        );
    }
});


////// add dailog button
// frappe.ui.form.on('Expense Category', {
//     refresh: function (frm) {
//         // Add a button on the form
//         frm.add_custom_button(__('Add via Dialog'), function () {

//             // Create the dialog
//             let d = new frappe.ui.Dialog({
//                 title: 'Add Expense Category',
//                 size: 'small',
//                 fields: [
//                     {
//                         label: 'Category Name',
//                         fieldname: 'category_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
//                     {
//                         label: 'Description',
//                         fieldname: 'description',
//                         fieldtype: 'Small Text'
//                     }
//                 ],
//                 primary_action_label: 'Save',
//                 primary_action(values) {
//                     // Ask for confirmation
//                     frappe.confirm(
//                         `Are you sure you want to save category "${values.category_name}"?`,
//                         function () {
//                             // On Yes: save the category
//                             frappe.call({
//                                 method: 'frappe.client.insert',
//                                 args: {
//                                     doc: {
//                                         doctype: 'Expense Category',
//                                         category_name: values.category_name,
//                                         description: values.description
//                                     }
//                                 },
//                                 callback: function (r) {
//                                     if (r.message) {
//                                         frappe.msgprint({
//                                             title: __('Success'),
//                                             message: `Category "${values.category_name}" saved!`,
//                                             indicator: 'green'
//                                         });
//                                         d.hide();  // Close dialog
//                                         frm.reload_doc(); // Refresh form
//                                     }
//                                 },
//                                 error: function (err) {
//                                     frappe.msgprint({
//                                         title: __('Error'),
//                                         message: 'Failed to save category',
//                                         indicator: 'red'
//                                     });
//                                     console.error(err);
//                                 }
//                             });
//                         },
//                         function () {
//                             // On Cancel
//                             frappe.msgprint(__('Category not saved.'));
//                         }
//                     );
//                 }
//             });

//             d.show();  // Show the dialog
//         });
//     }
// });


// /////////// show task without save
// frappe.ui.form.on('Expense Category', {
//     refresh: function (frm) {
//         // Add a custom button
//         frm.add_custom_button(__('Other Task'), function () {

//             // Create the dialog
//             let d = new frappe.ui.Dialog({
//                 title: 'Perform Other Task',
//                 size: 'small', // small, large, extra-large
//                 fields: [
//                     {
//                         label: 'Task Name',
//                         fieldname: 'task_name',
//                         fieldtype: 'Data',
//                         reqd: 1
//                     },
//                     {
//                         label: 'Notes',
//                         fieldname: 'notes',
//                         fieldtype: 'Small Text'
//                     }
//                 ],
//                 primary_action_label: 'Execute',
//                 primary_action(values) {
//                     // Close the dialog
//                     d.hide();

//                     // Show alert to user
//                     frappe.show_alert({
//                         message: `Task "${values.task_name}" executed!`,
//                         indicator: 'blue'
//                     }, 5);

//                     // Log values in console (for debugging / other tasks)
//                     console.log('Dialog input values:', values);

//                     // Example: You can also call a server method if needed
//                     // frappe.call({
//                     //     method: 'expense_manager.expense_manager.api.do_something',
//                     //     args: values,
//                     //     callback: function(r) {
//                     //         frappe.msgprint({ title: 'Success', message: r.message, indicator: 'green' });
//                     //     }
//                     // });
//                 }
//             });

//             // Show the dialog
//             d.show();
//         });
//     }
// });


///////submit after current task submitted
// frappe.ui.form.on('Expense Category', {
//     after_save: function (frm) {
//         frappe.confirm(
//             __('Do you want to add tasks for this category?'),
//             () => { // Yes
//                 let d = new frappe.ui.Dialog({
//                     title: 'Add Expense Task',
//                     fields: [
//                         {
//                             label: 'Task Name',
//                             fieldname: 'task_name',
//                             fieldtype: 'Data',
//                             reqd: 1
//                         },
//                         {
//                             label: 'Notes',
//                             fieldname: 'notes',
//                             fieldtype: 'Small Text'
//                         }
//                     ],
//                     primary_action_label: 'Save Task',
//                     primary_action: function (values) {
//                         frappe.call({
//                             method: 'frappe.client.insert',
//                             args: {
//                                 doc: {
//                                     doctype: 'Expense Task',
//                                     task_name: values.task_name,
//                                     notes: values.notes,
//                                     category: frm.doc.name  // Link to Expense Category
//                                 }
//                             },
//                             callback: function (r) {
//                                 if (r.message) {
//                                     frappe.msgprint({
//                                         title: __('Success'),
//                                         message: `Task "${values.task_name}" saved!`,
//                                         indicator: 'green'
//                                     });
//                                     d.hide(); // Close dialog
//                                 }
//                             },
//                             error: function (err) {
//                                 frappe.msgprint({
//                                     title: __('Error'),
//                                     message: 'Failed to save task',
//                                     indicator: 'red'
//                                 });
//                                 console.error(err);
//                             }
//                         });
//                     }
//                 });
//                 d.show();
//             },
//             () => { /* No */ }
//         );
//     }
// });


// ///redorecting other form
// frappe.ui.form.on('Expense Category', {
//     after_save: function (frm) {
//         // Show success alert for 3 seconds
//         frappe.show_alert({
//             message: __('Expense Category saved successfully!'),
//             indicator: 'green'
//         }, 3);

//         // Ask user if they want to add tasks
//         frappe.confirm(
//             __('Do you want to add tasks for this category?'),
//             () => {
//                 // Yes: Redirect to Expense Task list filtered by this category
//                 frappe.set_route('List', 'Expense Task', { category: frm.doc.name });
//             },
//             () => {
//                 // No: Do nothing
//             }
//         );
//     }
// });



frappe.ui.form.on('Expense Category', {
    after_save: function (frm) {
        // Show success alert
        frappe.show_alert({
            message: __('Expense Category saved successfully!'),
            indicator: 'green'
        }, 3);

        // Ask if user wants to add tasks
        frappe.confirm(
            __('Do you want to add tasks for this category?'),
            () => { // Yes
                // Redirect to Expense Task list filtered by category
                frappe.set_route('List', 'Expense Task', { category: frm.doc.name });

                // Listen for the list page to load
                frappe.once('route-change', function () {
                    // The list page might not be fully rendered yet, so wait a bit
                    setTimeout(() => {
                        const add_btn = document.querySelector('.page-head .add-btn');
                        if (add_btn) add_btn.click();
                    }, 300); // 0.3s delay
                });

            },
            () => { /* No */ }
        );
    }
});

