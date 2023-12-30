# このコードは、RFM（Recency, Frequency, Monetary）スコアを計算するための関数です。
# RFMスコアは顧客セグメンテーションに広く使用され、以下の3つの要素で構成されます：

# Recency (最終購入日からの経過日数):各顧客ごとに最終購入日から現在までの経過日数を計算します。
# Frequency (購入回数):同じ顧客IDが何回購入したかを計算します。
# Monetary (合計購入金額):各顧客ごとに購入金額の合計を計算します。
# そして、これらの要素を元に各顧客にRFMスコアを付与します。

# 以下は具体的な例です：
def calculate_rfm(df):
    # 最終購入日を取得
    max_purchase_date = df['PurchaseDate'].max()
    
    # RFMスコアを計算
    rfm_df = df.groupby('CustomerID').agg({
        'PurchaseDate': lambda x: (max_purchase_date - x.max()).days, # 最終購入日から何日経っているか計算
        'CustomerID': 'count',  # 同じ顧客IDが何個あるかの計算によって購入回数を求める
        'PurchaseAmount': 'sum' # 合計購入金額の計算
    })

    # カラムの名称を変更
    rfm_df.rename(columns={
        'PurchaseDate': 'Recency',
        'CustomerID': 'Frequency',
        'PurchaseAmount': 'Monetary'
    }, inplace=True)

    return rfm_df

import pandas as pd
import datetime

# サンプルデータの作成
data = {
    'CustomerID': [1, 1, 2, 2, 3],
    'PurchaseDate': ['2023-01-01', '2023-01-05', '2023-01-02', '2023-01-04', '2023-01-03'],
    'PurchaseAmount': [100, 150, 200, 50, 300]
}

df = pd.DataFrame(data)
df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])

# calculate_rfm 関数の実行
rfm_result = calculate_rfm(df)

# 結果の表示
display(rfm_result)

# この例では、5つの購買取引が3人の異なる顧客によって行われました。
# calculate_rfm関数はそれぞれの顧客に対してRecency、Frequency、Monetaryの値を計算し、それを表形式で返します。
この例では、5つの購買取引が3人の異なる顧客によって行われました。calculate_rfm関数はそれぞれの顧客に対してRecency、Frequency、Monetaryの値を計算し、それを表形式で返します。
