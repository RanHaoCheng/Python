import openpyxl

wb = openpyxl.load_workbook('RDPIO301XX1421-ELE-V1.0_20180202.xlsx')
ws = wb.get_sheet_by_name('Sheet1')


print(ws['E8'].value)

billOfMaterialData = {}

bomAry = []

for row_cnt in range(7,ws.max_row+1):

    billOfMaterialData.setdefault('NUMBER' , '')
    billOfMaterialData.setdefault('NAME' , '')
    billOfMaterialData.setdefault('SPEC' , '')
    billOfMaterialData.setdefault('REPLACEMENT' , '')
    billOfMaterialData.setdefault('PLACEMENT','')
    billOfMaterialData.setdefault('USAGE' , 0)

    componentNumber = ws['A'+str(row_cnt)].value
    componentName = ws['B'+str(row_cnt)].value
    componentSpec = ws['C'+str(row_cnt)].value
    isReplacement = ws['D'+str(row_cnt)].value
    placeMent = ws['E'+str(row_cnt)].value
    componentUsage = ws['F'+str(row_cnt)].value
    print(type(componentUsage))
    if type(componentUsage) == type(None):
        componentUsage = ws['F'+str(row_cnt-1)].value
    print(componentName)

    billOfMaterialData['NUMBER'] = componentNumber
    billOfMaterialData['NAME'] = componentName
    billOfMaterialData['SPEC'] = componentSpec
    billOfMaterialData['REPLACEMENT'] = isReplacement
    billOfMaterialData['PLACEMENT'] = placeMent
    billOfMaterialData['USAGE'] = int(componentUsage)

    bomAry.append(billOfMaterialData)

print(bomAry)

