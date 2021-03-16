# excel file reader
import openpyxl
# imports the path stuff
from pathlib import Path

def read_file(contacts_path):
    """
    reads the excel file
    """
    xlsx_file = Path(contacts_path)
    wb_obj = openpyxl.load_workbook(xlsx_file) 

    sheet = wb_obj.active
    entries_count = sheet.max_row
    contacts = [entries_count]
    numbers = [entries_count]
    for i in range(entries_count):
        contacts.append(sheet["A" + str(i+1)].value)
        numbers.append(sheet["C" + str(i+1)].value)
    return (contacts, numbers)