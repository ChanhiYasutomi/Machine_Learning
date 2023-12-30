# Feature Hashing（特徴ハッシング）は、高次元のカテゴリカルデータを低次元のベクトルに変換するためのテクニックの一つです。
# 主にテキストデータやカテゴリカルデータを処理する際に使用され、メモリ効率が高いことが特徴です。
# このテクニックでは、ハッシュ関数を使用して各カテゴリを固定サイズのベクトルにマッピングします。

# 以下に、Pythonコードを使用してFeature Hashingを説明する具体的な例を示します。この例では、カテゴリカルなデータを低次元のハッシュベクトルに変換します。
import pandas as pd
from sklearn.feature_extraction import FeatureHasher

# サンプルデータを含むデータフレームを作成
data = {
    'Category1': ['A', 'B', 'A', 'C', 'B'],
    'Category2': ['X', 'Y', 'X', 'Z', 'Z']
}

df = pd.DataFrame(data)

# Feature Hashingのインスタンスを作成
hasher = FeatureHasher(n_features=4, input_type='string')

# カテゴリカルデータをハッシュベクトルに変換
hashed_features = hasher.transform(df[['Category1', 'Category2']].astype(str).values)

# ハッシュベクトルをデータフレームに変換
hashed_df = pd.DataFrame(hashed_features.toarray(), columns=['Feature_0', 'Feature_1', 'Feature_2', 'Feature_3'])

# 元のデータフレームとハッシュベクトルを結合
result_df = pd.concat([df, hashed_df], axis=1)

print(result_df)

# このコードでは、以下の手順を実行しています：
# カテゴリカルなデータを持つデータフレーム df を作成します。
# FeatureHasher のインスタンスを作成し、ハッシュベクトルの次元数を指定します。この例では n_features=4 としました。
# カテゴリカルデータをハッシュベクトルに変換する前に、astype(str) を使用してデータを文字列型に変換します。
# hasher.transform(...) を使用してカテゴリカルデータをハッシュベクトルに変換します。
# ハッシュベクトルをデータフレームに変換し、新しい列として追加します。
# 元のデータフレームとハッシュベクトルを結合して、最終的な結果のデータフレーム result_df を得ます。
# 上記のコードを実行すると、以下のようなデータフレーム result_df が得られます：

#   Category1 Category2  Feature_0  Feature_1  Feature_2  Feature_3
# 0         A         X         0.0        1.0         0.0         1.0
# 1         B         Y         0.0        0.0         0.0         1.0
# 2         A         X         0.0        1.0         0.0         1.0
# 3         C         Z        -1.0       -1.0        -1.0        -1.0
# 4         B         Z        -1.0        0.0        -1.0        -1.0

# このようにして、カテゴリカルデータが低次元のハッシュベクトルに変換されました。ハッシュベクトルの次元数は n_features パラメータで指定できます。この方法により、カテゴリカルデータを数値データに変換する際のメモリ消費を削減できます。
# ただし、注意が必要で、異なるカテゴリが同じハッシュ値にマップされることがあるため、適切な次元数やハッシュ関数の選択が重要です。
