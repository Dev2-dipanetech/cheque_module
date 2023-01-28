# Copyright (c) 2023, DT Team and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class ChequeBook(Document):
	
	def before_save(self):
		self.no_of_leaves = int(self.cheque_number_to ) - int(self.cheque_number_from)
	