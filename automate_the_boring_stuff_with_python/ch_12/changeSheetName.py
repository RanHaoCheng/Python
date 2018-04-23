import openpyxl

wb = openpyxl.load_workbook('RDPIO301XX1421-ELE-V1.0_20180202.xlsx')
print(wb.get_sheet_names())
