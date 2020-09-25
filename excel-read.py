import xlrd
import datetime
import pandas as pd

path = "Free/Python_Exercises/business_report.xlsx"
excel_workbook = xlrd.open_workbook(path)
excel_worksheet = excel_workbook.sheet_by_index(0)

print("Your excel sheet has " + str(excel_worksheet.ncols) + " columns")
print("Your excel sheet has " + str(excel_worksheet.nrows) + " rows")

for row in range(excel_worksheet.nrows):
    for col in range(excel_worksheet.ncols):
        if col == 0 and row != 0:
            # format date
            raw_value = excel_worksheet.cell_value(row, col)
            converted_date = xlrd.xldate_as_tuple(raw_value, excel_workbook.datemode)
            to_print_date = datetime.datetime(*converted_date).strftime("%m/%d/%y")
            print (to_print_date, end='')
            # *converted_date = converted_date[0],converted_date[1],converted_date[2]
        else:
            print(excel_worksheet.cell_value(row, col), end='')
        print("\t\t", end='')
    print()
