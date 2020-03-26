import xlwt
# myWorkbook = xlrd.open_workbook('excelFile.xls')
f = xlwt.Workbook() 
sheet1 = f.add_sheet(u'sheet2',cell_overwrite_ok=True) 
l_=[1,2,3,4,5]
for i in range(len(l_)):
    sheet1.write(0,i,i)
f.save(r'C:\Users\winner\Desktop\text.xls')#保存文件


import xlrd, xlwt
from xlutils.copy import copy as xl_copy
 
# open existing workbook
rb = xlrd.open_workbook(r'C:\Users\winner\Desktop\text.xls', formatting_info=True)
# make a copy of it
wb = xl_copy(rb)
# add sheet to workbook with existing sheets
Sheet1 = wb.add_sheet('ddsfsw')
a=[1,2,3,4,5]
for i in range(len(a)):
    Sheet1.write(i,0,a[i])
wb.save(r'C:\Users\winner\Desktop\text.xls')
