// frappe.pages['barcode-scanner'] = frappe.pages['barcode-scanner'] || {};
// frappe.pages['barcode-scanner'].on_page_load = function (wrapper) {
//     let page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Barcode Scanner',
//         single_column: true
//     });

//     let scan_button = $('<button class="btn btn-primary">Start Scanner</button>')
//         .appendTo(page.body)
//         .click(() => {
//             start_scanner();
//         });

//     function start_scanner() {
//         const scanner = new frappe.ui.Scanner({
//             dialog: true,      // open camera in dialog
//             multiple: true,    // continuous scanning
//             on_scan(data) {
//                 handle_scanned_barcode(data.decodedText, scanner);
//             }
//         });
//     }

//     function handle_scanned_barcode(value, scanner) {
//         frappe.msgprint("Scanned: " + value);
//         console.log("Scanned:", value);

//         // Stop scanning if a special code is detected
//         if (value === "STOP123") {
//             scanner.stop_scan();
//             frappe.msgprint("Scanner stopped because STOP123 was scanned!");
//         }

//         // Send scanned data to backend API
//         frappe.call({
//             method: "expense_manager.expense_manager.api.log_scanned_barcode",
//             args: { barcode: value },
//             callback: function (r) {
//                 console.log("Logged to server:", r.message);
//             }
//         });
//     }
// };



// frappe.pages['barcode-scanner'].on_page_load = function (wrapper) {
//     let page = frappe.ui.make_app_page({
//         parent: wrapper,
//         title: 'Barcode Scanner',
//         single_column: true
//     });

//     $('<button class="btn btn-primary">Start Scanner</button>')
//         .appendTo(page.body)
//         .click(() => {
//             const scanner = new frappe.ui.Scanner({
//                 dialog: true,
//                 multiple: true,
//                 on_scan(data) {
//                     frappe.msgprint("Scanned: " + data.decodedText);
//                     frappe.call({
//                         method: "expense_manager.expense_manager.api.log_scanned_barcode",
//                         args: { barcode: data.decodedText },
//                         callback: function (r) { console.log(r.message); }
//                     });
//                 }
//             });
//         });
// };





// Purpose: This JS creates the UI for the barcode scanner page
// and handles barcode scanning using Html5Qrcode.

// /home/lid/Expense_manager/apps/expense_manager/expense_manager/page/barcode_scanner/barcode_scanner.js

frappe.pages['barcode-scanner'].on_page_load = function (wrapper) {
    console.log("✅ barcode_scanner.js loaded!");   // Debugging

    // // Create the app page
    // let page = frappe.ui.make_app_page({
    //     parent: wrapper,
    //     title: 'Barcode Scanner',
    //     single_column: true
    // });

    // // Add introduction text
    // $("<p>Welcome to the Barcode Scanner test page. Click the button below.</p>")
    //     .appendTo(page.main);

    // // Add a test button
    // $("<button class='btn btn-primary'>Click Me</button>")
    //     .appendTo(page.main)
    //     .on("click", () => {
    //         frappe.msgprint("✅ Button was clicked!");
    //         console.log("✅ Button was clicked!");
    //     });
};

