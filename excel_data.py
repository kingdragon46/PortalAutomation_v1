# import xlsxwriter module
import xlsxwriter
from random_name_generator import ran_name

class Test_InvitesPage():
    def test_excel_writing(self):
        # Workbook() takes one, non-optional, argument
        # which is the filename that we want to create.
        workbook = xlsxwriter.Workbook('E:/Testing/Bookings/v0.1.0./hello.xlsx')

        # The workbook object is then used to add new
        # worksheet via the add_worksheet() method.
        worksheet = workbook.add_worksheet()

        for i in range(1, 10):
            person = ran_name()
            fname = person[2]
            lname = person[3]
            cmail = person[1]
            # Use the worksheet object to write
            # data via the write() method.
            worksheet.write(f'A{i}', fname)
            worksheet.write(f'B{i}', lname)
            worksheet.write(f'C{i}', cmail)

        # Finally, close the Excel file
        # via the close() method.
        workbook.close()
