def get_vector_map(df, column):
    dim = df[column].nunique()
    elem = df[column].unique()

    vector_map = dict()

    for id, e in enumerate(elem):
        init = [0 for _ in range(dim)]
        init[id] = 1
        vector_map[e] = init

    return vector_map, dim  # 関数内にreturn文を配置

# このコードは、DataFrame内の一意のカテゴリカルな要素（列）をベクトルにマッピングする関数 get_vector_map を定義しています。以下に、この関数の具体的な説明と例を示します。

import pandas as pd

# サンプルのDataFrameを作成
data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
}

df = pd.DataFrame(data)

# カテゴリカル列 'Category' をベクトルにマッピングする関数
def get_vector_map(df, column):
    dim = df[column].nunique()  # 列内の一意の要素数を取得
    elem = df[column].unique()  # 列内の一意の要素を取得

    vector_map = dict()

    for id, e in enumerate(elem):
        init = [0 for _ in range(dim)]  # ゼロで初期化されたリストを生成
        init[id] = 1  # インデックスがidの要素を1に設定
        vector_map[e] = init

    return vector_map, dim

# カテゴリカル列 'Category' をベクトルにマッピング
vector_map, dim = get_vector_map(df, 'Category')

# 結果を表示
print("ベクトルマップ:")
for category, vector in vector_map.items():
    print(f"{category}: {vector}")

print(f"次元数: {dim}")

# このコードでは、以下の手順で関数 get_vector_map を実行しています：
# dim 変数には、指定されたカラム（'Category'）内の一意の要素数が格納されます。この場合、'A'、'B'、'C' の3つの一意の要素があるため、dim は3になります。
# elem 変数には、指定されたカラム内の一意の要素（'A'、'B'、'C'）が格納されます。
# vector_map は、要素（'A'、'B'、'C'）を対応するベクトルにマッピングするための空の辞書です。ループを使用して、各要素をベクトルに変換し、vector_map に格納します。
# 各要素は、指定されたカラム内での順序に基づいて、対応するインデックスが1で、他のインデックスが0のリストで表されます。
# vector_map と dim の値が関数から返され、結果が表示されます。
# この関数は、カテゴリカルなデータをベクトル形式に変換する際に便利です。例えば、機械学習モデルにカテゴリカルデータを供給する際に使用できます。



import pandas as pd

data = {
    'Category': ['A', 'B', 'C', 'A', 'B', 'C'],
}

df = pd.DataFrame(data)

# カテゴリカル列 'Category' をベクトルにマッピングする関数
def get_vector_map(df, column):
    dim = df[column].nunique()  # 列内の一意の要素数を取得
    elem = df[column].unique()  # 列内の一意の要素を取得

    vector_map = dict()

    for id, e in enumerate(elem):
        init = [0 for _ in range(dim)]  # ゼロで初期化されたリストを生成
        init[id] = 1  # インデックスがidの要素を1に設定
        vector_map[e] = init

    return vector_map, dim

# カテゴリカル列 'Category' をベクトルにマッピング
vector_map, dim = get_vector_map(df, 'Category')

# ベクトルマップを新しいデータフレームに追加
vector_df = pd.DataFrame.from_dict(vector_map, orient='index', columns=[f'Category_{i+1}' for i in range(dim)])
df = df.join(vector_df, on='Category')

# 結果を表示
display(df)

# 提供されたコードは、カテゴリカル列 'Category' をベクトルにマッピングし、新しいデータフレームに追加するものです。これにより、各カテゴリがベクトルとして表現され、カテゴリごとに対応する列が作成されます。以下はコードの詳細な説明です：
# サンプルのデータフレーム df は、1つのカテゴリカル列 'Category' を持っています。
# get_vector_map 関数は、指定されたカテゴリカル列をベクトルにマッピングするための関数です。この関数は次のステップで実行されます：
# dim 変数は、'Category' 列内の一意の要素数（異なるカテゴリの数）を取得します。
# elem 変数は、'Category' 列内の一意の要素（異なるカテゴリ）を取得します。
# vector_map 辞書は、カテゴリからベクトルへのマッピングを保持するための辞書です。各カテゴリに対して、初期化されたゼロのリストを生成し、該当する位置に1を設定します。これにより、カテゴリがベクトルに変換されます。
# vector_map を使用して、新しいデータフレーム vector_df を作成します。pd.DataFrame.from_dict() を使用して、辞書からデータフレームを生成し、列名を 'Category_1'、'Category_2'、...、'Category_dim' のように命名します。
# 最後に、元のデータフレーム df に vector_df を結合します。これにより、カテゴリカル列がベクトルに変換されたデータフレームが得られます。

# 結果を表示するために display(df) を使用していることがわかります。データフレームの最終的な形式は、各カテゴリがベクトルとして表現され、新しい列として追加されています。
