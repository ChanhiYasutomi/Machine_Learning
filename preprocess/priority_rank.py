# PandasのDataFrameに対して新しい列を追加し、その新しい列に優先順位を割り当てるための関数とコード。
prioritize_values 関数:

def prioritize_values(row):
    values = [
        dataframe['columns_1'], 
        dataframe['columns_2'], 
        dataframe['columns_3'], 
        dataframe['columns_4']
    ]

    priority_order = ['rank_1', 'rank_2']
    
    # priority_order リスト内の順序に従って、各カラムが優先されるかどうかを確認する。
    # if value in values: の条件で、value（優先順位のカラム名）が valuesリスト内に含まれているかをチェックし、もし含まれていれば、そのカラム名を優先順位として返す。
    # 優先順位が見つからない場合、'None' を返す。'rank_1'があれば'rank_2'よりも優先的に返す(つまり'rank_1'が優先される。)

    for value in priority_order:
        if value in values:
            return value
    
    return 'None'

# prioritize_values 関数を各行に適用し、その結果を 'rank_info' という新しい列に追加します。
# 各行には、優先順位が割り当てられた新しい列が作成されます。優先順位がない場合は 'None' が設定されます。
# このコードの目的は、各行の値を比較し、優先順位に従って優先順位情報を提供する。
# たとえば、行ごとに異なるカラム（'columns_1' から 'columns_4'）の値がある場合、その値を優先順位に従って評価し、'rank_info' カラムに最終的な優先順位を割り当てます。このような処理は、データ内の要素の優先順位を特定する際に役立ちます。
dataframe['rank_info'] = dataframe.apply(prioritize_values, axis=1)
