def unique_to_binary(column):
    unique_values = column.unique()
    if len(unique_values) == 2 and set(unique_values) == {0, 1}:
        return 1
    else:
        return 0

# def unique_to_binary(column) 関数は、与えられた列（Pandas Series）内のユニークな値が0または1であるかどうかを確認し、その結果に応じて0または1を返す関数です。具体的な例を挙げて説明しましょう。
# 以下の例を考えます。仮想的なデータセットで、 'Gender' 列があり、この列には性別を表す値が含まれています。この列が0（男性）または1（女性）の値しか含まないかどうかを確認したいとします。
import pandas as pd

data = {'Gender': [0, 1, 0, 1, 0, 1]}
df = pd.DataFrame(data)

# unique_to_binary 関数を適用して 'Gender' 列を評価
result = unique_to_binary(df['Gender'])
display(result)

# このコードでは、 unique_to_binary 関数が 'Gender' 列に適用されます。 'Gender' 列には0と1の2つのユニークな値しかないため、この関数は1を返します。
# 結果として、次のように出力されます：
# 1
# この場合、関数が1を返したことから、'Gender' 列は0または1の値しか含まず、フラグが立てられます。データの品質評価やデータの前処理時に、このようなカラムを特定するのに役立ちます。
