# Copyright (c) 2025, lidia and contributors
# For license information, please see license.txt

# import frappe
# from frappe import _


# def execute(filters: dict | None = None):
# 	"""Return columns and data for the report.

# 	This is the main entry point for the report. It accepts the filters as a
# 	dictionary and should return columns and data. It is called by the framework
# 	every time the report is refreshed or a filter is updated.
# 	"""
# 	columns = get_columns()
# 	data = get_data()

# 	return columns, data


# def get_columns() -> list[dict]:
# 	"""Return columns for the report.

# 	One field definition per column, just like a DocType field definition.
# 	"""
# 	return [
# 		{
# 			"label": _("Column 1"),
# 			"fieldname": "column_1",
# 			"fieldtype": "Data",
# 		},
# 		{
# 			"label": _("Column 2"),
# 			"fieldname": "column_2",
# 			"fieldtype": "Int",
# 		},
# 	]


# def get_data() -> list[list]:
# 	"""Return data for the report.

# 	The report data is a list of rows, with each row being a list of cell values.
# 	"""
# 	return [
# 		["Row 1", 1],
# 		["Row 2", 2],
# 	]
# import frappe

# def execute(filters=None):
#     if not filters:
#         filters = {}

#     columns = [
#         {"label": "Expense Date", 
#          "fieldname": "expense_date", 
#          "fieldtype": "Date"},
#         {"label": "Employee Name",
#           "fieldname": "employee_name", 
#           "fieldtype": "Data"},
#         {"label": "Payment Method", 
#          "fieldname": "payment_method", 
#          "fieldtype": "Data"},
#         {"label": "Category", 
#          "fieldname": "category", 
#          "fieldtype": "Data"},
#         {"label": "Amount", 
#          "fieldname": "amount", 
#          "fieldtype": "Currency"},
#         {"label": "Description", 
#          "fieldname": "description", 
#          "fieldtype": "Data"},
#     ]

#     conditions = []
#     values = {}

#     if filters.get("from_date"):
#         conditions.append("expense_date >= %(from_date)s")
#         values["from_date"] = filters["from_date"]

#     if filters.get("to_date"):
#         conditions.append("expense_date <= %(to_date)s")
#         values["to_date"] = filters["to_date"]

#     if filters.get("category"):
#         conditions.append("category = %(category)s")
#         values["category"] = filters["category"]

#     condition_sql = " AND ".join(conditions)

#     query = f"""
#         SELECT
#             expense_date,
#             employee_name,
#             payment_method,
#             category,
#             amount,
#             description
#         FROM
#             `tabExpense`
#         WHERE
#             1=1 { " AND " + condition_sql if condition_sql else "" }
#         ORDER BY expense_date ASC
#     """

#     data = frappe.db.sql(query, values, as_dict=True)

#     # calculate total
#     total = sum(d.amount for d in data)

#     # add a row for total
#     data.append({
#         "expense_date": "",
#         "employee_name": "",
#         "payment_method": "",
#         "category": "",
#         "amount": total,
#         "description": "",
#         "Total": "TOTAL",
#     })

#     return columns, data




# import frappe

# def execute(filters=None):
#     if not filters:
#         filters = {}

#     columns = [
#         {"label": "Expense Date", "fieldname": "expense_date", "fieldtype": "Date", "width": 120},
#         {"label": "Employee Name", "fieldname": "employee_name", "fieldtype": "Data", "width": 150},
#         {"label": "Payment Method", "fieldname": "payment_method", "fieldtype": "Select", "width": 120},
#         {"label": "Category", "fieldname": "category", "fieldtype": "Link", "options": "Expense Category", "width": 120},
#         {"label": "Amount", "fieldname": "amount", "fieldtype": "Currency", "width": 120},
#         {"label": "Description", "fieldname": "description", "fieldtype": "Data", "width": 200},
#     ]

#     filters_dict = {}
#     if filters.get("from_date"):
#         filters_dict["expense_date"] = [">=", filters["from_date"]]
#     if filters.get("to_date"):
#         filters_dict["expense_date"] = ["<=", filters["to_date"]]
#     if filters.get("category"):
#         filters_dict["category"] = filters["category"]

#     # Fetch data using Frappe ORM
#     data = frappe.get_all(
#         "Expense",
#         filters=filters_dict,
#         fields=[
#             "expense_date",
#             "employee_name",
#             "payment_method",
#             "category",
#             "amount",
#             "description"
#         ],
#         order_by="expense_date asc"
#     )

#     # Calculate total
#     total = sum(d.amount for d in data if d.amount)

#     # Append total row at the end
#     data.append({
#         "expense_date": "TOTAL",   # ✅ TOTAL label in first column
#         "employee_name": "",
#         "payment_method": "",
#         "category": "",
#         "amount": total,
#         "description": ""
#     })

#     return columns, data




# import frappe
# from frappe.utils import flt

# def execute(filters=None):
#     if not filters:
#         filters = {}

#     # Build conditions based on filters
#     conditions = []
#     if filters.get("from_date"):
#         conditions.append(f"expense_date >= '{filters['from_date']}'")
#     if filters.get("to_date"):
#         conditions.append(f"expense_date <= '{filters['to_date']}'")
#     if filters.get("category"):
#         conditions.append(f"category = '{filters['category']}'")

#     where_clause = " AND ".join(conditions) if conditions else "1=1"

#     # Fetch expense data
#     data = frappe.db.sql(f"""
#         SELECT
#             name as ID,
#             employee_name as Employee,
#             expense_date as Date,
#             category as Category,
#             payment_method as Payment,
#             amount as Amount
#         FROM `tabExpense`
#         WHERE {where_clause}
#         ORDER BY expense_date
#     """, as_dict=True)

#     # Calculate total amount
#     total_amount = sum([flt(d.get("Amount") or 0) for d in data])

#     # Append total row
#     data.append({
#         "ID": "",
#         "Employee": "Total",
#         "Date": "",
#         "Category": "",
#         "Payment": "",
#         "Amount": total_amount
#     })

#     # Define columns for report
#     columns = [
#         {"label": "ID", "fieldname": "ID", "fieldtype": "Data", "width": 150},
#         {"label": "Employee", "fieldname": "Employee", "fieldtype": "Data", "width": 150},
#         {"label": "Date", "fieldname": "Date", "fieldtype": "Date", "width": 120},
#         {"label": "Category", "fieldname": "Category", "fieldtype": "Link", "options": "Category", "width": 150},
#         {"label": "Payment Method", "fieldname": "Payment", "fieldtype": "Select",
#          "options": "Cash\nBank\nCheque\nMobile Transfer", "width": 120},
#         {"label": "Amount", "fieldname": "Amount", "fieldtype": "Currency", "width": 120},
#     ]

#     return columns, data

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    conditions = []

    if filters.get("category"):
        conditions.append(f"category = '{filters['category']}'")

    if filters.get("from_date"):
        conditions.append(f"expense_date >= '{filters['from_date']}'")
    if filters.get("to_date"):
        conditions.append(f"expense_date <= '{filters['to_date']}'")

    where_clause = " AND ".join(conditions) if conditions else "1=1"

    expenses = frappe.db.sql(f"""
        SELECT 
            employee_name,
            expense_date,
            category,
            amount,
            payment_method,
            description
        FROM `tabExpense`
        WHERE {where_clause}
        ORDER BY expense_date ASC
    """, as_dict=True)

    # Calculate total
    total_amount = sum([exp.amount for exp in expenses]) if expenses else 0

    # Add total row
    if expenses:
        expenses.append({
            "employee_name": _("Total"),
            "expense_date": "",
            "category": "",
            "amount": total_amount,
            "payment_method": "",
            "description": ""
        })

    columns = [
        {"label": _("Employee"), "fieldname": "employee_name", "fieldtype": "Data", "width": 150},
        {"label": _("Expense Date"), "fieldname": "expense_date", "fieldtype": "Date", "width": 120},
        {"label": _("Category"), "fieldname": "category", "fieldtype": "Link", "options": "Expense Category", "width": 150},
        {"label": _("Amount"), "fieldname": "amount", "fieldtype": "Currency", "width": 120},
        {"label": _("Payment Method"), "fieldname": "payment_method", "fieldtype": "Select", "width": 120},
        {"label": _("Description"), "fieldname": "description", "fieldtype": "Small Text", "width": 300},
    ]

    return columns, expenses
