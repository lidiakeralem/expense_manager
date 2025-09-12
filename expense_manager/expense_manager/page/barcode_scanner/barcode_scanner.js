frappe.pages['barcode-scanner'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'barcode scanner',
		single_column: true
	});
}