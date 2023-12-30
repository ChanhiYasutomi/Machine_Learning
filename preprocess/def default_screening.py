def default_screening(df, threshold=180):
    df['recency'] = df['recency']-df['product_use_days']-threshold
    df['age'] = df['age']-threshold
    if 'pre_recency' in df.columns:
        df['pre_recency'] = df['pre_recency']-threshold
    df = df[df['recency']>=0]
    return df.drop(columns=['date']) if 'date' in df.columns else df

# 提供された関数 default_screening は、データフレーム内の特定の列に対して閾値を適用し、条件を満たさない行を削除するために使用されます。以下では、この関数の主要なステップとその動作について説明します：
# 'recency' と 'age' 列の変更:
# df['recency'] = df['recency'] - df['product_use_days'] - threshold
# df['age'] = df['age'] - threshold
# 'recency' 列と 'age' 列から 'product_use_days' と threshold の値を引きます。これにより、特定の閾値を超えた場合のみ条件を満たすことができるようになります。

# 'pre_recency' 列の変更:
# if 'pre_recency' in df.columns:
#     df['pre_recency'] = df['pre_recency'] - threshold
# もしデータフレーム内に 'pre_recency' 列が存在する場合、同様に 'pre_recency' 列から threshold の値を引きます。

# 条件に基づくフィルタリング:
# df = df[df['recency'] >= 0]
# 'recency' 列がゼロ以上の行だけを残します。これにより、条件を満たさない行が削除されます。

# 'date' 列の削除:
# return df.drop(columns=['date']) if 'date' in df.columns else df
# もしデータフレーム内に 'date' 列が存在する場合、この列を削除します。その後、変更されたデータフレームを返します。

# この関数は、特定の条件（'recency' および 'age' 列が閾値を超えない）を満たす行のみを保持し、不要な 'date' 列を削除することを目的としています。データの前処理とクリーニングに使用されることを想定しています。
