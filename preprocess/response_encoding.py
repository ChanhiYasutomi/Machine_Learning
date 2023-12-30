# Response Encoding（応答エンコーディング）は、カテゴリカルデータを数値データに変換する手法で、各カテゴリの平均値（または他の統計的な指標）を、そのカテゴリの新しい数値としてエンコードします。
# 通常、このエンコーディングは目的変数（応答変数）に関連付けて行われ、カテゴリが特定の応答値に対してどの程度影響を持つかを示す指標として使用されます。以下に、Pythonコードを使用してResponse Encodingを実行する具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C'],
    'Target': [10, 20, 15, 25, 30, 10, 10, 25]
}

df = pd.DataFrame(data)

# 'Category' 列をResponse Encodingでエンコード
response_encoding_dict = df.groupby('Category')['Target'].mean().to_dict()
df['Category_Response_Encoded'] = df['Category'].map(response_encoding_dict)

# print(df)
# このコードの具体的なステップは以下の通りです：
# サンプルデータを含むデータフレーム df を作成します。このデータフレームには 'Category' 列と 'Target' 列が含まれています。
# groupby() メソッドを使用して 'Category' 列をグループ化し、各カテゴリ内の 'Target' 列の平均値を計算します。これにより、各カテゴリの平均応答値が得られます。
# to_dict() メソッドを使用して、各カテゴリの平均応答値を辞書に変換します。この辞書は各カテゴリをキーとし、平均応答値を値として保持します。
# map() メソッドを使用して 'Category' 列をResponse Encodingで置き換えます。各カテゴリはその平均応答値で置き換えられます。新しい列 'Category_Response_Encoded' がデータフレームに追加されます。
# 最終的なデータフレームは、'Category' 列がResponse Encodingによって置き換えられ、各カテゴリの平均応答値がその数値としてエンコードされた 'Category_Response_Encoded' 列を含んでいます。
# このエンコードは、カテゴリカルデータと応答変数との関連性を示す指標として使用され、モデルの学習に適した形式に変換します。
