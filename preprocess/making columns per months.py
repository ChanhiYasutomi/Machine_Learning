# setting span（from '2023-01' to '2023-12'）
# start_monthとend_monthの設定:
# start_monthは範囲の開始月を、end_monthは範囲の終了月を表しています。この例では、範囲が1月から12月までの全ての月であるため、start_monthは1、end_monthは12に設定されています。
start_month = 1
end_month = 12

# making columns per months
for month in range(start_month, end_month + 1):
    # 月ごとのカラムの作成:
    # ループを使用して、指定された範囲（1月から12月）の各月に対して以下の操作が行われます。
    # month_str変数には、フォーマットされた月の文字列が格納されます。例えば、1月は'2023-01'、2月は'2023-02'となります。
    month_str = f'2023-{month:02d}'
    
    # dataframe['columns_timestamp'].dt.strftime('%Y-%m')を使用して、元のDataFrameの 'columns_timestamp' カラムから年と月を 'YYYY-MM' 形式の文字列に変換します。
    # str.contains(month_str)を使用して、変換された文字列が month_str と一致するかどうかを確認します。一致する場合、Trueが、一致しない場合、Falseが生成されます。
    # astype(int)を使用して、Trueを1、Falseを0に変換し、月ごとのフラグのカラムが生成されます。
    # このコードは、元のDataFrameに対して、各月に関するフラグのカラムを追加します。これにより、DataFrame内の特定の日付が各月に該当するかどうかを簡単に判断できます。例えば、特定の日付が3月に該当する場合、3月のカラムには1が表示され、該当しない場合は0が表示されます。
    dataframe[month_str] = dataframe['columns_timestamp'].dt.strftime('%Y-%m').str.contains(month_str).astype(int)
