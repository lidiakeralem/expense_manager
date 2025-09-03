# Copyright (c) 2025, lidia and contributors
# For license information, please see license.txt

from pydoc import doc
from xmlrpc.client import _datetime
from expense_manager.expense_manager.doctype import expense, expense_category
import frappe
from frappe.model.document import Document
from frappe.utils import now_datetime, getdate, add_days
from datetime import datetime


class Expense(Document):
    def validate(self):
        if self.expense_date:
            expense_date = getdate(self.expense_date)  # convert string → date
            if expense_date > now_datetime().date():  # compare date with date
                frappe.throw("Expense Date cannot be in the future. Please enter a valid date.")


     
  


	# set description field before insert
def set_description(doc, method):
		if not doc.description:
			doc.description = f"No description provided"
#log creation after insert
# def log_expense_creation(doc):
# 	frappe.msgprint(f"Expense created: {doc.name}")
	
def log_expense_creation(doc, method):
    # Log a message in Frappe Console
    #frappe.logger().info(f"New Expense created: {doc.name}, Employee: {doc.employee_name}, Amount: {doc.amount}")

    if frappe.db.exists("DocType", "Expense Log"):
        frappe.get_doc({
            "doctype": "Expense Log",
            "expense": doc.name,
            "amount": doc.amount,
            "remark": f"This expense {doc.name} created for the employee {doc.employee_name}, and the expense amount in birr:  {doc.amount}",
            "created_date": datetime.now().strftime("%Y-%m-%d"),
            "created_by": frappe.session.user
        }).insert(ignore_permissions=True)


## Validate the amount 

def validate_expense_amount(doc, method):
    """
    Validate that expense amount > 0 and <= 10,000
    """
    company_limit = 10000

    if doc.amount <= 0:
        frappe.throw("Expense amount must be greater than zero.")

    if doc.amount > company_limit:
        frappe.throw(f"Expense amount cannot exceed {company_limit}.")

# scheduler for send email with daily summery of total expenses
def send_daily_expense_summary():
    """
    Send daily expense summary for last 24 hours
    """
    # Get date range
    today = now_datetime()
    yesterday = add_days(today, -1)

    # Fetch expenses in last 24 hours
    expenses = frappe.get_all(
        "Expense",
        filters={
            "creation": [">=", yesterday]
        },
        fields=["name", "owner", "amount", "category", "payment_method", "creation"]
    )

    if not expenses:
        print("No expenses in the last 24 hours.")
        return  

    # Calculate total
    total_amount = sum(exp["amount"] for exp in expenses)

    # Build email content
    message = f"<h3>Daily Expense Summary</h3>"
    message += f"<p>Total Expenses: {len(expenses)}</p>"
    message += f"<p>Total Amount: {total_amount}</p>"
    message += "<ul>"
    for exp in expenses:
        message += f"<li>{exp['creation']} - {exp['owner']} - {exp['amount']} ({exp['category']}, {exp['payment_method']})</li>"
    message += "</ul>"

    # Send email
    frappe.sendmail(
        recipients=["lidu6438@gmail.com"],  
        subject="Daily Expense Summary",
        message=message
    )
    print("Daily expense summary email sent successfully.")
    
	#test
    # print(message)
    # print("Daily expense summary calculation completed.")




	# def validate(self):
	# 	frappe.msgprint(f"Fields available: {self.as_dict()}")

# def add_data(category_name, description):
# 		if not category_name:
# 			frappe.throw("Category Name is a required field.")

# 		expense_category = frappe.get_doc({
# 			"doctype": "Expense_category",
# 			"category_name": category_name,
# 			"description": description
# 		})
# 		expense_category.insert()
# 		return {"message": f'expense_category: {expense_category.name} "Expense category added successfully."}

# def get_data(category_name):
# 		data = frappe.get_all("Expense_category", fields=["category_name", "description"])
# 		return data
		
