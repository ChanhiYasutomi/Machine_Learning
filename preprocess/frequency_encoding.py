# requency Encoding（頻度エンコーディング）は、カテゴリカルデータを数値データに変換する手法で、
# 各カテゴリの出現頻度（割合）をそのカテゴリの新しい数値としてエンコードします。以下に、Pythonコードを使用してFrequency Encodingを実行する具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 10, 10, 25]
}

df = pd.DataFrame(data)

# 'Category' 列をFrequency Encodingでエンコード
frequency_encoding_dict = (df['Category'].value_counts(normalize=True)).to_dict()
df['Category_Frequency_Encoded'] = df['Category'].map(frequency_encoding_dict)

print(df)

# このコードの具体的なステップは以下の通りです：
# サンプルデータを含むデータフレーム df を作成します。
# value_counts(normalize=True) メソッドを使用して 'Category' 列内の各カテゴリの出現頻度を計算し、それを正規化（合計が1になるように）します。これにより、各カテゴリの出現頻度が割合として得られます。
# to_dict() メソッドを使用して、出現頻度を辞書に変換します。この辞書は各カテゴリをキーとし、出現頻度の割合を値として保持します。
# map() メソッドを使用して 'Category' 列をFrequency Encodingで置き換えます。各カテゴリはその出現頻度の割合で置き換えられます。新しい列 'Category_Frequency_Encoded' がデータフレームに追加されます。

# 最終的なデータフレームは、'Category' 列がFrequency Encodingによって置き換えられ、各カテゴリの出現頻度の割合がその数値としてエンコードされた 'Category_Frequency_Encoded' 列を含んでいます。
# このエンコードは、カテゴリカルデータの頻度情報を数値データに変換するために使用され、モデルの学習に適した形式にするのに役立ちます。
