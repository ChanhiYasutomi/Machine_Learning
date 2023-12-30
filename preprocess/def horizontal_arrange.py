def horizontal_arrange(df):
    _df = df.groupby(['user_id'], as_index=False).shift()
    _df.columns = ['pre_'+c for c in _df.columns]
    df = df.join(_df)
    del _df
    df['interval'] = df['pre_recency']-df['recency']
    df = df.drop(columns=['pre_date', 'pre_recency', 'pre_use_days', 'pre_cum'])
    return df[df['cum']>=2]

# 提供された関数 horizontal_arrange は、データフレーム内の行をユーザーごとに並び替えて、特定の列に対して差分や間隔を計算し、条件を満たす行のみを残すために使用されます。
# 以下では、この関数の主要なステップとその動作について説明します：

# データの横方向の並べ替え:
# _df = df.groupby(['user_id'], as_index=False).shift()
# データフレームを 'user_id' でグループ化し、各ユーザーごとに行を横方向に並び替えます。これにより、同じユーザーの前の行のデータがそれぞれの行に追加されます。

# 列名の変更:
# python
# _df.columns = ['pre_'+c for c in _df.columns]
# _df データフレームの各列名の前に 'pre_' を付け加え、新しい列名を設定します。これにより、前の行の各列の名前が変更されます。

# オリジナルデータフレームに結合:
# df = df.join(_df)
# _df データフレームをオリジナルのデータフレーム df に結合します。

# 時間間隔の計算:
# df['interval'] = df['pre_recency'] - df['recency']
# 'pre_recency' 列と 'recency' 列の差を計算し、結果を新しい 'interval' 列として追加します。これにより、前の行との時間間隔が計算されます。

# 不要な列の削除:
# df = df.drop(columns=['pre_date', 'pre_recency', 'pre_product_use_days', 'pre_cum'])
# 不要な列を削除します。これらの列は前の行のデータを含んでおり、もはや必要ないため削除されます。

# 条件に基づくフィルタリング:
# return df[df['cum'] >= 2]
# 'cum' 列が2以上の行だけを残します。この条件に基づいてデータがフィルタリングされ、関数の結果として返されます。

# この関数は、データの前処理と特徴量エンジニアリングの一部として使用されることを想定しており、データフレーム内の行を特定の方法で変換し、条件を満たす行を抽出する役割を果たします。

# 提供された関数 horizontal_arrange を使用して、具体的なPythonコードの例を示します。この例では、関数を使用してデータフレームの行をユーザーごとに並び替え、前の行との時間間隔を計算し、特定の条件を満たす行のみを残します。
import pandas as pd
import numpy as np

# サンプルデータフレームを作成
data = {
    'user_id': [1, 1, 1, 2, 2, 2, 3, 3],
    'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02', '2023-01-03', '2023-01-01', '2023-01-02'],
    'recency': [5, 10, 15, 20, 25, 30, 35, 40],
    'use_days': [90, 120, 180, 60, 150, 210, 90, 120],
    'cum': [1, 2, 3, 1, 2, 3, 1, 2]
}

df = pd.DataFrame(data)

# horizontal_arrange関数を使用してデータの変換を行う
df = horizontal_arrange(df)

# このコードでは、次のステップが実行されます：
# サンプルデータフレーム df を作成し、'user_id'、'date'、'recency'、'product_use_days'、および 'cum' の列が含まれています。
# horizontal_arrange 関数を呼び出し、データフレームに対して変換を実行します。
# 最終的なデータフレーム df を表示します。
# horizontal_arrange 関数によって、データが前の行との時間間隔に関して変換され、特定の条件（'cum' 列が2以上の行のみを残す）が適用されます。最終的なデータフレームは、これらの変更が適用されたものとなります。
