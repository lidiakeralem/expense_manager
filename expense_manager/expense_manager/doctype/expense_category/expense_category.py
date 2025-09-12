# Copyright (c) 2025, lidia and contributors
# For license information, please see license.txt

#import frappe
import frappe
from frappe.utils.logger import set_log_level
from frappe.model.document import Document


class ExpenseCategory(Document):
	pass


# set_log_level("DEBUG")
# logger = frappe.logger("expense_category", allow_site=True, file_count=20)

# @frappe.whitelist()
# def log_category(category_name, description=None):
#     """
#     Log creation or update events for Expense Category
#     """
#     user = frappe.session.user
#     logger.info(f"User {user} triggered log_category API with category_name='{category_name}'")

#     try:
#         # Check if category exists
#         existing = frappe.db.exists("Expense Category", {"category_name": category_name})
#         if existing:
#             logger.debug(f"Updating existing category: {category_name}")
#             doc = frappe.get_doc("Expense Category", existing)
#             doc.description = description
#             doc.save()
#             logger.info(f"Updated category '{category_name}' with new description")
#         else:
#             logger.debug(f"Creating new category: {category_name}")
#             doc = frappe.get_doc({
#                 "doctype": "Expense Category",
#                 "category_name": category_name,
#                 "description": description
#             })
#             doc.insert()
#             logger.info(f"Created new category '{category_name}'")

#         frappe.db.commit()
#         return {"status": "success", "name": doc.name}

#     except Exception as e:
#         logger.error(f"Error while handling category '{category_name}': {str(e)}", exc_info=True)
#         frappe.throw(f"Error: {str(e)}")
