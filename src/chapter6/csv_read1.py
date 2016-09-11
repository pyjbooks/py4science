import csv # 標準モジュールcsvを読み込んで使用可能にする


# CSVファイルの読み出し
with open('data1.csv', 'r', encoding='utf8') as f:
    dat = [k for k in csv.reader(f)] # リスト内包表記を使う

# CSVファイルの書き込み
with open('out.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(dat)
