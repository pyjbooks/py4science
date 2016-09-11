import xlwt  # Excelファイル書き込み用
import xlrd  # Excelファイル読み出し用

# --- Excelファイルの書き込み
# Work bookを準備
wb = xlwt.Workbook()
# シートを追加
ws = wb.add_sheet('シート1')
# シートの特定のセルに値を入れる
ws.write(0, 0, 'Upper Left')
ws.write(1, 0, 1)
ws.write(1, 1, 2)
ws.write(1, 2, xlwt.Formula("A3+B3"))
# Work bookに名前を付けて保存
wb.save('xlwt.xls')

# --- Excelファイルの読み出し
# 読み出すWork bookを指定して開く
wb = xlrd.open_workbook('xlwt.xls')
# シートを名前で指定する
st = wb.sheet_by_name('シート1')
# 指定したシートの特定のセルの値を読み出して表示
print(st.cell(0, 0).value)
