# Leave-One-Out Encoding（LOOエンコーディング）は、カテゴリカルデータをエンコードする手法で、各カテゴリの平均値をそのカテゴリの新しい数値としてエンコードします。
# LOOエンコーディングは、各カテゴリの平均値を計算する際に、エンコード対象のサンプルを除外して計算する点が通常のResponse Encodingと異なります。
# 以下に、Pythonコードを使用してLOOエンコーディングを実行する具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C'],
    'Target': [10, 20, 15, 25, 30, 10, 10, 25]
}

df = pd.DataFrame(data)

# 'Category' 列をLOO Encodingでエンコード
df['Category_LOO_Encoded'] = 0  # 新しい列を初期化

for category in df['Category'].unique():
    # カテゴリを1つずつ取り出して平均値を計算
    mean_target_except_current = df[df['Category'] != category]['Target'].mean()
    
    # 各行のカテゴリがエンコード対象のカテゴリと一致する場合、平均値を代入
    df.loc[df['Category'] == category, 'Category_LOO_Encoded'] = mean_target_except_current

print(df)

# このコードの具体的なステップは以下の通りです：
# サンプルデータを含むデータフレーム df を作成します。
# 新しい列 'Category_LOO_Encoded' を初期化します。この列にLOOエンコーディングの結果を格納します。
# 各カテゴリについてループを実行し、エンコード対象のカテゴリを除外して平均値を計算します。これにより、各カテゴリに対する平均値が計算されます。
# loc を使用して、各行の 'Category' がエンコード対象のカテゴリと一致する場合、平均値を 'Category_LOO_Encoded' 列に代入します。
# 最終的なデータフレームは、'Category' 列がLOOエンコーディングによって置き換えられ、各カテゴリのLOOエンコーディング結果が 'Category_LOO_Encoded' 列に格納されています。
# このエンコーディングは、カテゴリカルデータと目的変数との関連性を示す指標として使用され、モデルの学習に適した形式に変換します。
