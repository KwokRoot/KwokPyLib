import xlrd
import xlwt

## 读

rb = xlrd.open_workbook(r"/opt/test_excel.xlsx")
sh1 = rb.sheet_by_index(0)

row_count = sh1.nrows
col_count = sh1.ncols

print(row_count)
print(col_count)

for row in sh1.get_rows():
    for col in range(col_count):
        print(row[col].value, end=", ", )
    print()


# ## 写

# xl = xlwt.Workbook(encoding='utf-8')
# sh = xl.add_sheet('单元格宽度', cell_overwrite_ok=True)
# sh.write(0, 0, '第一个行第一列内容')
# sh.col(0).width = 5000
#
# xl.save(r'/opt/test_excel.xlsx')


