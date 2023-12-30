# カテゴリ分割
dataframe = dataframe['category'].str.split(';', expand=True) # expand=Trueは分割された単語の数の分のカラムを新しく作成する
dataframe.columns = ['word_1','word_2','word_3','word_4','word_5']

# カテゴリと置換表(df_map_dep)を結合
df_marge = pd.merge(dataframe, df_map_dep, how="left", left_on="word_1", right_on="before")
df_marge = pd.merge(df_marge, df_map_dep, how="left", left_on="word_2", right_on="before")
df_marge = pd.merge(df_marge, df_map_dep, how="left", left_on="word_3", right_on="before")
df_marge = pd.merge(df_marge, df_map_dep, how="left", left_on="word_4", right_on="before")
df_marge = pd.merge(df_marge, df_map_dep, how="left", left_on="word_5", right_on="before")
