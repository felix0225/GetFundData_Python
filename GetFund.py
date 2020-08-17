import pandas as pd


def GetStockq():
    # 取得鋒裕匯理基金淨值的資料表格
    # 網址可以換成想要查找的基金網址
    df = pd.read_html('http://stockq.org/funds/pioneer.php')[11]

    # 刪除有NaN的行跟列
    df = df.dropna(axis=0, how='all').dropna(axis=1, how='all')

    # 指定要過濾的基金名稱
    # 可以換成表格內其他的基金名稱
    dfFilter = df[1].isin(['基金名稱','鋒裕匯理基金(II)-新興市場債券基金-A2'])

    # 取得過濾後的資料，並重新index
    df = df[dfFilter].reset_index(drop=True)
    print(df)

    # 可以另外檔案
    # fileName = '鋒裕匯理基金(II)-新興市場債券基金-A2.html'
    # df.to_html(fileName, encoding='utf-8-sig', index=False, header=False)

    # 重新組合訊息文字
    msg = df.at[1, 11] + ' ' + df.at[1, 1].replace('匯理基金(II)-', '')
    for index, row in df.iterrows():
        if index > 0:
            msg += '\n' + row[3] + ' 淨值(' + row[5] + \
                ') 漲跌(' + row[7] + ') 比例(' + row[9] + ')'
    print(msg)


if __name__ == '__main__':
    # 取投資項目的淨值
    GetStockq()
