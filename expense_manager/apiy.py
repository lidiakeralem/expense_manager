import frappe
from frappe.utils.logger import set_log_level
######scanner api######
# @frappe.whitelist(allow_guest=True)
# def log_scanned_barcode(barcode=None):
#     """
#     Logs scanned barcode to expense_category.log
#     """
#     if not barcode:
#         barcode = "No data"

#     logger.info({
#         "event": "Barcode Scanned",
#         "data": {"barcode": barcode},
#         "site": frappe.local.site,
#         "user": frappe.session.user
#     })

#     return "Logged successfully!"

# @frappe.whitelist( allow_guest = True)
# def add_expense_category(category_name, description=None):
#     """
#     Create a new Expense Category document
#     """
#     if not category_name:
#         frappe.throw("Category Name is required")
    
#     doc = frappe.get_doc({
#         "doctype": "Expense Category",
#         "category_name": category_name,
#         "description": description
#     })
#     doc.insert()
#     frappe.db.commit()
    
#     return {"message": "Expense Category added successfully!"}


@frappe.whitelist()
def add_expense_category(category_name, description=None):
    """Add a new Expense Category"""
    if not category_name:
        frappe.throw("Category Name is required")

    # Check if category already exists
    if frappe.get_all("Expense Category", filters={"category_name": category_name}):
        return f'Category "{category_name}" already exists'

    # Create new category
    doc = frappe.get_doc({
        "doctype": "Expense Category",
        "category_name": category_name,
        "description": description
    })
    doc.insert()
    frappe.db.commit()

    return f'Category "{category_name}" added successfully'
