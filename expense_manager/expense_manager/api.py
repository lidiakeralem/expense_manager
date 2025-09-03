# import frappe
# from frappe.model.document import Document

# api.py
# api.py
import frappe
@frappe.whitelist(allow_guest=True)
def get_test_data():
    # your code here
    return "test"
# @frappe.whitelist(allow_guest=False)
# def get_expenses():
#     return frappe.get_all(
#         "Expense",
#         fields=["expense_date", "employee_name", "amount", "category", "payment_method"]
#     )

# @frappe.whitelist(allow_guest=False)
# def add_expense(employee_name, expense_date, category, amount, payment_method, description=None, attach_receipt=None):
#     doc = frappe.get_doc({
#         "doctype": "Expense",
#         "employee_name": employee_name,
#         "expense_date": expense_date,
#         "category": category,
#         "amount": amount,
#         "payment_method": payment_method,
#         "description": description or "No description provided",
#         "attach_receipt": attach_receipt
#     })
#     doc.insert(ignore_permissions=True)
#     return {"message": f"Expense {doc.name} added successfully."}
