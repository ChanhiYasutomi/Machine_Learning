# Count Encoding（カウントエンコーディング）は、カテゴリカルなデータを数値データに変換する手法で、各カテゴリの出現回数をそのカテゴリの新しい値としてエンコードします。
# 以下に、Pythonコードを使用してCount Encodingを実行する具体的な例を示します：
import pandas as pd

# サンプルデータを含むデータフレームを作成
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'A', 'A', 'C'],
    'Value': [10, 20, 15, 25, 30, 10, 10, 25]
}

df = pd.DataFrame(data)

# Count Encodingを行うための辞書を作成
count_encoding_dict = df['Category'].value_counts().to_dict()

# 'Category' 列をCount Encodingで置き換える
df['Category_Count_Encoded'] = df['Category'].map(count_encoding_dict)

print(df)

# このコードの具体的なステップは次のとおりです：
# サンプルデータを含むデータフレーム df を作成します。
# value_counts() メソッドを使用して 'Category' 列内の各カテゴリの出現回数を計算し、それを辞書に変換します。この辞書は各カテゴリをキーとし、出現回数を値として保持します。
# map() メソッドを使用して 'Category' 列をCount Encodingで置き換えます。この操作により、各カテゴリがその出現回数で置き換えられます。新しい列 'Category_Count_Encoded' がデータフレームに追加されます。
# 最終的なデータフレームを表示します。
# 結果として、'Category' 列がCount Encodingによって置き換えられ、各カテゴリの出現回数がそれに対応する数値としてエンコードされた 'Category_Count_Encoded' 列が作成されます。
# このエンコードは、カテゴリカルデータを数値データに変換するための一般的な手法であり、カテゴリの出現頻度を考慮に入れることができます。
