# Target Encoding（ターゲットエンコーディング）は、カテゴリカルデータを数値データに変換する手法で、各カテゴリの平均ターゲット値をそのカテゴリの新しい数値としてエンコードします。
# 以下に、Pythonコードを使用してTarget Encodingを実行する具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C'],
    'Target': [10, 20, 15, 25, 30, 10, 10, 25]
}

df = pd.DataFrame(data)

# 'Category' 列をTarget Encodingでエンコード
encoding_map = df.groupby('Category')['Target'].mean().to_dict()
df['Category_Target_Encoded'] = df['Category'].map(encoding_map)

print(df)

# このコードの具体的なステップは以下の通りです：
# サンプルデータを含むデータフレーム df を作成します。このデータフレームには 'Category' 列（カテゴリカルデータ）と 'Target' 列（数値データ、目的変数）が含まれています。
# groupby() メソッドを使用して 'Category' 列をグループ化し、各カテゴリ内の 'Target' 列の平均値を計算します。これにより、各カテゴリの平均ターゲット値が得られます。
# to_dict() メソッドを使用して、平均ターゲット値を辞書に変換します。この辞書は各カテゴリをキーとし、平均ターゲット値を値として保持します。
# map() メソッドを使用して 'Category' 列をTarget Encodingで置き換えます。各カテゴリはその平均ターゲット値で置き換えられます。新しい列 'Category_Target_Encoded' がデータフレームに追加されます。
# 最終的なデータフレームは、'Category' 列がTarget Encodingによって置き換えられ、各カテゴリの平均ターゲット値がその数値としてエンコードされた 'Category_Target_Encoded' 列を含んでいます。
# このエンコードは、カテゴリカルデータと目的変数との関連性を示す指標として使用され、モデルの学習に適した形式に変換します。
