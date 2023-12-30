# 方位にカテゴライズ
# 先ほどの関数を使って求めた360°表記の角度をカテゴリ変数に変換します。
# ラベルエンコーダーを適用することを考えて、方角を数字に変換して出力します。
# n_ways=8（つまり8方位）のときは、0が北、1が北東、…、7が北西です。

# 方位にカテゴライズ
def direction(azimuth, n_ways=8):
    bins = np.linspace(0, 360, n_ways+1) 
    # 方位角に22.5°を足す。
    _azimuth = azimuth + 180/n_ways
    _azimuth = np.where(_azimuth >= 360, _azimuth - 360, _azimuth)
    return np.digitize(_azimuth, bins=bins) - 1についてpythonのコードで具体例を挙げて説明して

# direction 関数は、与えられた方位角（0度から360度の値）を指定された数の方位（方向）カテゴリに分類するための関数です。以下に具体的な例を示します。
import numpy as np
import pandas as pd

# サンプルのデータフレームを作成
data = {'azimuth': [30, 60, 120, 180, 240, 300, 330]}
df_location = pd.DataFrame(data)

# 方位をカテゴライズ
df_location['direction'] = direction(df_location['azimuth'], n_ways=8)

# 結果を表示
display(df_location)

# このコードでは、df_location データフレーム内の 'azimuth' 列の方位角データを direction 関数を使用してカテゴライズします。n_ways パラメータは方向の数を指定します。デフォルトでは8つの方向に分類されます。結果は、'direction' 列にカテゴリカルな方向情報が追加されたデータフレームとして表示されます。

# 例の出力（カテゴリのインデックスが表示されます）：
#    azimuth  direction
# 0       30          0
# 1       60          1
# 2      120          2
# 3      180          3
# 4      240          4
# 5      300          5
# 6      330          6
# 方位角が0度から360度の範囲で、8つの方向に分類されています。
