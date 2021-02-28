import openpyxl
from pathlib import Path

def readFile():
	xlsx_file = Path('P:\Mini-Python\excel-reader', 'Contacts.xlsx')
	wb_obj = openpyxl.load_workbook(xlsx_file) 

	# Read the active sheet:
	sheet = wb_obj.active
	# A and C from 2 to count
	# print(sheet["A3"].value)
	noOfEntries = sheet.max_row
	contacts = [noOfEntries]
	numbers = [noOfEntries]

	for i in range(noOfEntries):
		print(str(sheet["A"+str(i+1)].value) + "- " + str(sheet["C"+str(i+1)].value))
		contacts.append(sheet["A"+str(i+1)].value)
		numbers.append(sheet["C"+str(i+1)].value)

	return (contacts, numbers)

# print(readFile())
(contacts, numbers) = readFile()
print(numbers)