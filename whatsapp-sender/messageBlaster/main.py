import whatsapp
import excel_reader as excel
import os

attachment_path =  os.path.dirname(__file__) + r'\Sale.mp4'

def main():
    # whatsapp.whatsapp_login()
    (contacts, numbers) = excel.read_file(os.path.dirname(__file__) + r'\Contacts.xlsx')
    whatsapp.sender(numbers, contacts, attachment_path)
main()
    
