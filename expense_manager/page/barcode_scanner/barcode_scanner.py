# Purpose: This file defines the Frappe page context.
# Frappe requires a Python file in page/<page_name>/ folder even if it does nothing complex.

# import frappe

# def get_context(context):
#     context.title = "Barcode Scanner"


# /home/lid/Expense_manager/apps/expense_manager/expense_manager/page/barcode_scanner/barcode_scanner.py

import frappe

def get_context(context):
    """
    This function is called automatically when the page is loaded.
    You can pass variables to the Jinja context if needed.
    """
    context.title = "Barcode-Scanner"
    context.intro_message = "This is the Barcode Scanner test page."
    return context
