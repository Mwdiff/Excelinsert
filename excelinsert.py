from DBcm import UseDatabase
from openpyxl import load_workbook
from init import dbconfig


# open file
file = input('Podaj nazwę pliku: ')

wb = load_workbook(f'./{file}.xlsx')
ws = wb[wb.sheetnames[0]]
last_column = ws.max_column
# last_row = ws.max_row
# print(ws['A2:A'+str(ws.max_row)])
# for cell in ws.iter_rows(min_row=2, max_row=ws.max_row, max_col=1, values_only=1):
#     print(cell[0])

def AppendSelectColumns(sheet: 'worksheet', columns: str) -> None:
    max_column = sheet.max_column
    for (col, i) in zip(columns.split(', '), range(max_column+1, 100)):
        sheet.cell(1, i).value = col
    with UseDatabase(dbconfig) as cursor:
        for cell in sheet.iter_rows(min_row=2, max_row=sheet.max_row, max_col=1):
            _SQL = """select %s from towary where symbol=%s"""
            cursor.execute(_SQL, (columns, cell[0].value,))
            data = cursor.fetchall()[0]
            for index in range(len(data)):
                sheet.cell(cell[0].row, max_column+1+index).value = data[index]

AppendSelectColumns(ws, '*')
wb.save(f'./edit_{file}.xlsx')
# get args

# read-select-write
#   >connect to DB

#save and quit