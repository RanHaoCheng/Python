import openpyxl
import sys
import pprint

def createBOMlist(NameOfBOM , NewFileName):

    # 'RDPIO301XX1421-ELE-V1.0_20180202.xlsx'
    wb = openpyxl.load_workbook(NameOfBOM)
    sheetList = wb.get_sheet_names()
    ws = wb.get_sheet_by_name(sheetList[0])

    #
    #   billOfMaterialData = {}

    bomAry = []

    for row_cnt in range(7,ws.max_row+1):

        componentNumber = ws['A'+str(row_cnt)].value
        componentName = ws['B'+str(row_cnt)].value
        componentSpec = ws['C'+str(row_cnt)].value
        isReplacement = ws['D'+str(row_cnt)].value
        placeMent = ws['E'+str(row_cnt)].value
        componentUsage = ws['F'+str(row_cnt)].value

        # leave loop when BOM actually ends
        if type(componentNumber) == type(None):
            break

        # Placement and usage may be combined to one cell
        # So it is possible be read as None
        while type(placeMent) == type(None):
            placeMent = ws['E'+str(row_cnt-1)].value

       #  print(type(componentUsage))
        while type(componentUsage) == type(None):
            componentUsage = ws['F'+str(row_cnt-1)].value
        #print(componentName)

        # Create a new dict in each loop
        # Otherwise the dict you put into list will be just the same reference
        # No matter how you changes its value
        # Finally the list will full of the same value
        billOfMaterialData = {
            "NUMBER":componentNumber,
            "NAME":componentName,
            "SPEC":componentSpec,
            "REPLACEMENT":isReplacement,
            "PLACEMENT": placeMent,
            "USAGE":int(componentUsage)
                }

        # billOfMaterialData.setdefault('NUMBER' , '')
        # billOfMaterialData.setdefault('NAME' , '')
        # billOfMaterialData.setdefault('SPEC' , '')
        # billOfMaterialData.setdefault('REPLACEMENT' , '')
        # billOfMaterialData.setdefault('PLACEMENT','')
        # billOfMaterialData.setdefault('USAGE' , 0)


        # billOfMaterialData['NUMBER'] = componentNumber
        # billOfMaterialData['NAME'] = componentName
        # billOfMaterialData['SPEC'] = componentSpec
        # billOfMaterialData['REPLACEMENT'] = isReplacement
        # billOfMaterialData['PLACEMENT'] = placeMent
        # billOfMaterialData['USAGE'] = int(componentUsage)

        # print(billOfMaterialData)
        bomAry.append(billOfMaterialData)

    #print(bomAry)

    print('Writing results...')
    # 'OriginBOM.py'
    resultFile = open(NewFileName+'.py', 'w')
    resultFile.write(NewFileName + ' = ' + pprint.pformat(bomAry))
    resultFile.close()

def main():
    if len(sys.argv) < 3 :
        print('Usage : ' + sys.argv[0] + ' <Original BOM><R-BOM> ')
        sys.exit(1)

    originalBOM = sys.argv[1]
    newBOM = sys.argv[2]
    print('Original : ' + originalBOM + ' ; new BOM : ' + newBOM)

    createBOMlist(originalBOM, 'Original')
    createBOMlist(newBOM, 'New')


if __name__ == "__main__":
    main()
