# MinMaxScaler を使用して各列のデータを最小-最大スケーリング（0から1の範囲に変換）することも可能です。以下に、MinMaxScaler を使った具体的な例を示します。
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

# サンプルのDataFrameを作成
data = {'feature1': [10, 20, 30, 40],
        'feature2': [0.1, 0.2, 0.3, 0.4]}

df = pd.DataFrame(data)

# 各列のデータを最小-最大スケーリング
for col in df.columns:
    scaler = MinMaxScaler()  # MinMaxScalerのインスタンスを作成
    df[col] = scaler.fit_transform(np.array(df[col].values).reshape(-1, 1))  # 列データを最小-最大スケーリング

display(df)

# このコードの詳細：
# from sklearn.preprocessing import MinMaxScaler：Scikit-Learnライブラリから MinMaxScaler クラスをインポートします。
# サンプルのDataFrame df を作成し、いくつかのサンプルデータを含む2つの列（'feature1' と 'feature2'）を持たせます。
# for col in df.columns: ループを使用して、DataFrame内の各列に対して以下の操作を実行します：
# scaler = MinMaxScaler()：MinMaxScaler のインスタンスを作成します。
# np.array(df[col].values).reshape(-1, 1) を使用して、列データをNumPy配列に変換し、1列のデータに再形成します。
# scaler.fit_transform メソッドを使用して、データを最小-最大スケーリングします。これにより、各列のデータが0から1の範囲に変換されます。スケーリング後のデータは元のDataFrameに代入されます。
# 最終的に、最小-最大スケーリングされたDataFrame df の内容が表示されます。

# このコードを実行すると、各列のデータが0から1の範囲に変換されたDataFrameが得られます。このようなスケーリングは、異なる尺度を持つ特徴量を同じ尺度に揃え、機械学習モデルの訓練や解析に役立ちます。
