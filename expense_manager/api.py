import frappe

# ---------------- EXPENSE ----------------

@frappe.whitelist(allow_guest=True)
def create_expense(expense_date, employee_name, amount, payment_method, category, description=None):
    doc = frappe.get_doc({
        "doctype": "Expense",
        "expense_date": expense_date,
        "employee_name": employee_name,
        "amount": amount,
        "payment_method": payment_method,
        "category": category,
        "description": description or ""
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist(allow_guest=True)
def get_expenses():
    return frappe.get_all(
        "Expense",
        fields=["name", "expense_date", "employee_name", "amount", "payment_method", "category", "description"],
        order_by="expense_date desc"
    )


@frappe.whitelist(allow_guest=True)
def update_expense(name, expense_date=None, employee_name=None, amount=None, payment_method=None, category=None, description=None):
    doc = frappe.get_doc("Expense", name)
    if expense_date: doc.expense_date = expense_date
    if employee_name: doc.employee_name = employee_name
    if amount: doc.amount = amount
    if payment_method: doc.payment_method = payment_method
    if category: doc.category = category
    if description is not None: doc.description = description
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist(allow_guest=True)
def delete_expense(name):
    frappe.delete_doc("Expense", name, ignore_permissions=True)
    frappe.db.commit()
    return {"message": f"Expense {name} deleted successfully"}


# ---------------- EXPENSE CATEGORY ----------------

@frappe.whitelist(allow_guest=True)
def create_expenseCategory(category_name, description=None):
    doc = frappe.get_doc({
        "doctype": "Expense Category",
        "category_name": category_name,
        "description": description or ""
    })
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist(allow_guest=True)
def get_expenseCategories():
    return frappe.get_all(
        "Expense Category",
        fields=["name", "category_name", "description"],
        order_by="name desc"
    )


@frappe.whitelist(allow_guest=True)
def update_expenseCategory(name, category_name=None, description=None):
    doc = frappe.get_doc("Expense Category", name)
    if category_name: doc.category_name = category_name
    if description is not None: doc.description = description
    doc.save(ignore_permissions=True)
    frappe.db.commit()
    return doc.as_dict()


@frappe.whitelist(allow_guest=True)
def delete_expenseCategory(name):
    frappe.delete_doc("Expense Category", name, ignore_permissions=True)
    frappe.db.commit()
    return {"message": f"Expense Category {name} deleted successfully"}






















# import frappe
# from frappe import _ 
# from frappe.utils import cint
# from pydantic import BaseModel, Field, validator
# from typing import Optional


# # class ExpenseInput(BaseModel):
# #   expense_date: str
# #   employee_name: str
# #   amount: float
# #   payment_method: str
# #   category: str
# #   description: Optional[str]
# #   #validation for amount
# #   @validator("amount")
# #   def validate_amount(cls, a):
# #     if a <= 0:
# #         raise ValueError("amount must be greater than zero")
# #     if a > 10000:
# #         raise ValueError("amount must be less than 10000")
# #     return a
# #       # validator: check date format
# #   @validator("expense_date")
# #   def validate_date(cls, v):
# #         if not v or len(v.split("-")) != 3:
# #             raise ValueError("Invalid date format, expected YYYY-MM-DD")
# #         return v
  

# # ### add function
# # @frappe.whitelist(allow_guest=False)
# # def add_expense():
# #     try:
# #         # Get request JSON
# #         data = frappe.local.form_dict

# #         # Validate with Pydantic
# #         payload = ExpenseInput(**data)

# #         # Create new Expense doc
# #         expense = frappe.get_doc({
# #             "doctype": "Expense",
# #             "expense_date": payload.expense_date,
# #             "employee_name": payload.employee_name or frappe.session.user,
# #             "amount": payload.amount,
# #             "payment_method": payload.payment_method,
# #             "category": payload.category,
# #             "description": payload.description,
# #         })
# #         expense.insert(ignore_permissions=False)
# #         frappe.db.commit()

# #         return {
# #             "status": "success",
# #             "message": "Expense added successfully",
# #             "expense_id": expense.name,
# #         }

# #     except Exception as e:
# #         frappe.log_error(frappe.get_traceback(), "Add Expense API Error")
# #         return {
# #             "status": "error",
# #             "message": str(e),
# #         }




# # -----------------------
# # Pydantic model
# # -----------------------
# class ExpenseInput(BaseModel):
#     expense_date: str
#     employee_name: str
#     amount: float
#     payment_method: str
#     category: str
#     description: Optional[str]

#     # Validate date format
#     @validator("expense_date")
#     def validate_date(cls, v):
#         if not v or len(v.split("-")) != 3:
#             raise ValueError("Invalid date format, expected YYYY-MM-DD")
#         return v

#     # Validate amount
#     @validator("amount")
#     def validate_amount(cls, a):
#         if a <= 0:
#             raise ValueError("Amount must be greater than zero")
#         if a > 10000:
#             raise ValueError("Amount must be less then or equal to 10,000")
#         return a

# # -----------------------
# # Add expense function
# # -----------------------
# @frappe.whitelist(allow_guest=False)
# def add_expense(*args, **kwargs):
#     try:
#         # Merge args into kwargs if needed
#         data = kwargs

#         # Validate with Pydantic
#         payload = ExpenseInput(**data)

#         # Create new Expense doc using validated data
#         expense = frappe.get_doc({
#             "doctype": "Expense",
#             "expense_date": payload.expense_date,
#             "employee_name": payload.employee_name,
#             "amount": payload.amount,
#             "payment_method": payload.payment_method,
#             "category": payload.category,
#             "description": payload.description,
#         })
#         expense.insert(ignore_permissions=False)
#         frappe.db.commit()

#         return {
#             "status": "success",
#             "message": "Expense added successfully",
#             "expense_id": expense.name,
#         }

#     except Exception as e:
#         frappe.log_error(frappe.get_traceback(), "Add Expense API Error")
#         return {
#             "status": "error",
#             "message": str(e),
#         }




# #### get function
# # @frappe.whitelist(allow_guest=True)
# # def get_expense(page: int = 1, limit: int = 10, payment_method: Optional[str] = None, employee_name: Optional[str] = None):
# #     """Fetch expenses with pagination & optional filters"""
# #     try:
# #         page = cint(page)
# #         limit = cint(limit)
# #         start = (page - 1) * limit

# #         filters = {}
# #         if payment_method:
# #             filters["payment_method"] = payment_method
# #         if employee_name:
# #             filters["employee_name"] = employee_name

# #         expenses = frappe.get_all(
# #             "Expense",
# #             fields=[
# #                 "name",
# #                 "expense_date",
# #                 "employee_name",
# #                 "amount",
# #                 "payment_method",
# #                 "category",
# #                 "description",
# #             ],
# #             filters=filters,
# #             start=start,
# #             page_length=limit,
# #             order_by="expense_date desc",
# #         )

# #         return {
# #             "status": "success",
# #             "page": page,
# #             "limit": limit,
# #             "data": expenses,
# #         }

# #     except Exception as e:
# #         frappe.log_error(frappe.get_traceback(), "Get Expenses API Error")
# #         return {
# #             "status": "error",
# #             "message": str(e),
# #         }



# @frappe.whitelist(allow_guest=False)
# def get_expense(
#     page: int = 1,
#     limit: int = 5,
#     start_date: Optional[str] = None,
#     end_date: Optional[str] = None,
#     category: Optional[str] = None,
# ):
#     try:
#         # Convert page and limit to integer
#         page = cint(page)
#         limit = cint(limit)

#         # Calculate start index for pagination
#         start = (page - 1) * limit

#         # Build filters dictionary
#         filters = {}
#         if start_date and end_date:
#             filters["expense_date"] = ["between", [start_date, end_date]]
#         elif start_date:
#             filters["expense_date"] = [">=", start_date]
#         elif end_date:
#             filters["expense_date"] = ["<=", end_date]

#         if category:
#             filters["category"] = category

#         # Fetch expenses using filters & pagination
#         expenses = frappe.get_all(
#             "Expense",
#             fields=[
#                 "expense_date",
#                 "employee_name",  # Added employee_name
#                 "category",
#                 "amount",
#                 "description",
#                 "payment_method",
#             ],
#             filters=filters,
#             start=start,
#             page_length=limit,
#             order_by="expense_date desc",
#         )

#         return {
#             "status": "success",
#             "page": page,
#             "limit": limit,
#             "data": expenses,
#         }

#     except Exception as e:
#         # Log errors in Frappe error logs
#         frappe.log_error(frappe.get_traceback(), "Get Expenses API Error")
#         return {
#             "status": "error",
#             "message": str(e),
#         }




# def after_insert_expense(doc, method):
#     frappe.logger().info(f"New Expense Added: {doc.name}, Amount: {doc.amount}")

# def on_update_expense(doc, method):
#     frappe.logger().info(f"Expense Updated: {doc.name}")


# # -----------------------------
# # Hooks: Scheduled Job
# # -----------------------------
# def log_expense_summary():
#     total_expenses = frappe.db.count("Expense")
#     frappe.logger().info(f"Total Expenses so far: {total_expenses}")




#/////////////////////

