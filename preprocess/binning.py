# binning
x = [1, 7, 5, 4, 6, 3]

# pandasのcut関数でbinningを行う
# binの数を指定する場合
binned = pd.cut(x, 3)
display(binned)

binned_labels_false = pd.cut(x, 3, labels=False)
display(binned_labels_false)
# [0 2 1 1 2 0] - 変換された値は3つのbinのどれに入ったかを表す

# binの範囲を指定する場合（3.0以下、3.0より大きく5.0以下、5.0より大きい）
bin_edges = [-float('inf'), 3.0, 5.0, float('inf')]
binned_2 = pd.cut(x, bin_edges)
display(binned_2)

bin_edges = [-float('inf'), 3.0, 5.0, float('inf')]
binned_labels_false_2 = pd.cut(x, bin_edges, labels=False)
display(binned_labels_false_2)
# [0 2 1 1 2 0] - 変換された値は3つのbinのどれに入ったかを表す

# 提供されたコードは、"binning" または "データのビン分割" を行うために pandas ライブラリの pd.cut 関数を使用する例を示しています。データの離散化を行う際に役立ちます。以下はコードの詳細な説明です：
# データの用意：
# リスト x には、連続値のデータが格納されています。これをビン分割して離散的なカテゴリに変換します。

# ビンの数を指定してビン分割：
# pd.cut(x, 3) のように使用します。第1引数に対象のデータを渡し、第2引数にビンの数を指定します（この場合、3つのビンに分割されます）。
# 結果は、各データポイントがどのビンに属するかを示すカテゴリ（ラベル）が含まれた binned 変数に格納されます。また、display 関数を使用して結果を表示します。

# ビンの範囲を指定してビン分割：
# pd.cut(x, bin_edges) のように使用します。第1引数に対象のデータを渡し、第2引数にビンの範囲を指定します。
# ビンの範囲は bin_edges で定義されており、例では [-∞, 3.0, 5.0, ∞] と指定されています。
# 結果は、各データポイントがどのビンに属するかを示すカテゴリ（ラベル）が含まれた binned_2 変数に格納されます。また、display 関数を使用して結果を表示します。
# labels=False オプションを指定しない場合、pd.cut はビンの範囲に基づいてカテゴリ名（ラベル）を返します。labels=False を指定すると、代わりに各データポイントがどのビンに属するかを示す整数値が返されます。
