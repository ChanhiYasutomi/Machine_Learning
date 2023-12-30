# 'columns'カラムが非null（欠損値でない）行のインデックスを取得し、それを変数 i に格納
i = dataframe[dataframe['columns'].notnull()].index

# iで選択された行の 'columns' カラムのデータ型を整数型（int）に変換
dataframe.loc[i,'columns'] = dataframe.loc[i,'columns'].astype(int)

# DataFrame内の重複した行を削除し、新しいインデックスが設定
dataframe = dataframe.drop_duplicates().reset_index(drop=True)

# 'columns' カラムが欠損値（NaN）を持つ行を削除。
dataframe = dataframe.dropna(subset =['columns'])
