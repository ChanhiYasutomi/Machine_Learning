# 累積購入回数
df['cum_tmp'] = 1

_df = df.groupby(['userid'], as_index=False)[['cum_tmp']].cumsum().rename(columns={'cum_tmp': 'cumsum'})

# インデックスを基準に結合。横に連結する
df = df.join(_df)

del df['cum_tmp']

# このコードは、Pandas DataFrameを使用してユーザーごとの累積購入回数を計算し、元のDataFrameにその結果を結合する操作を行っています。以下に各部分の説明を提供します：
# 最初に、df データフレームに cum_tmp という新しい列を追加し、その値を全て1に設定します。この列は、各購入行が何回目の購入であるかを示すために使用されます。
# df['cum_tmp'] = 1

# 次に、_df という一時的なデータフレームを作成します。このデータフレームは、ユーザーごとに累積購入回数を計算します。
# groupby メソッドを使用して、userid 列をグループ化し、cum_tmp 列を累積合計（cumulative sum）します。そして、cumsum という列名にリネームします。結果は、ユーザーごとの購入回数の累積合計が格納された _df に保存されます。

# _df = df.groupby(['userid'], as_index=False)[['cum_tmp']].cumsum().rename(columns={'cum_tmp': 'cumsum'})

# 最後に、元の df と _df を userid に基づいて結合します。join メソッドを使用し、cum_tmp 列は不要なので削除します。結果として、元のデータフレーム df に cumsum 列が追加され、各ユーザーごとの累積購入回数が格納されます。
# df = df.join(_df)
# del df['cum_tmp']

# このコードを実行することで、ユーザーごとに累積購入回数を計算し、元のデータフレームに追加することができます。



# 条件付き累積購入回数 = 商品が切れる日+180日が経過すると0にリセット(購入が途絶えたらcumsumをリセット)
df["conditional_cumsum"] = df["cumsum"]

#  条件付き累積購入回数の条件を満たす行のインデックスを取得
# 「前回購入から[商品が切れる日+180]経過以内に再購入していない(==0)」を特定
condition = ((pd.Timestamp.now() + pd.Timedelta(hours=9)) > pd.to_datetime(df["out_of_stock_date_plus_180_days"])) & (df["repurchase_within_out_of_stock_date_plus_180_days_flag"] == 0)
reset_indices = df.index[condition]

# 0を付与
df.loc[reset_indices, "conditional_cumsum"] = 0

# 'userid' でグループ化
groups = df.groupby('userid')

# 条件を定義
condition = (df["conditional_cumsum"] == 0)

# 各 'userid' グループに対して処理を実行
# _はindex, group は'userid' グループ
for _, group in groups:
    # 'userid' グループ内で'conditional_cumsum'列の値が0である行のインデックスを取得(cumsumが0であるindex)
    reset_indices = group[condition].index
    
    # 0をリセットして1ずつ増加させる
    # (cumsum変数を初期化して、'conditional_cumsum'列の値をリセットする際に使用)
    cumsum = 1
    
    # 'userid' グループ内の各行に対してループ処理。index は行の(useridの)インデックス、row は行の(useridの)データ
    for index, row in group.iterrows():
        
        # もし行の(useridの)インデックス index が reset_indices 内に存在する場合、'cumsum' を0にリセット(cumsumが0であるindex)
        # cumsumが0であるindex内に、userid各グループ内インデックスがあればcumsumを0にリセット
        if index in reset_indices:
            cumsum = 1
            
        #　現在の行の 'conditional_cumsum' 列に、cumsum の値を設定し、'conditional_cumsum' 列の値が更新
        df.at[index, 'conditional_cumsum'] = cumsum
        # cumsum 変数を1ずつ増加させ、次の行の 'conditional_cumsum' 列の値を設定
        cumsum += 1

# 提供されたコードは、Pandasを使用して、条件付きの累積購入回数を計算し、特定の条件を満たす場合に累積購入回数をリセットする操作を行っています。以下にコードの各部分を詳しく説明します。
# df["conditional_cumsum"] = df["cumsum"]: cumsum 列の値を conditional_cumsum 列にコピーしています。この列には通常の累積購入回数が格納されます。

# 条件を定義し、条件を満たす行のインデックスを取得しています。条件は次の通りです：
# (pd.Timestamp.now() + pd.Timedelta(hours=9)) > pd.to_datetime(df["out_of_stock_date_plus_180_days"])：現在の日時に9時間を加えた日時が 'out_of_stock_date_plus_180_days' 列の値よりも未来にある場合、つまり商品が切れる日から180日以内に再購入していない場合。
# df["repurchase_within_out_of_stock_date_plus_180_days_flag"] == 0：'repurchase_within_out_of_stock_date_plus_180_days_flag' 列の値が0である場合。
# これらの条件を満たす行のインデックスが reset_indices に格納されます。
# df.loc[reset_indices, "conditional_cumsum"] = 0: 条件を満たす行の conditional_cumsum 列の値を0にリセットします。
# 'userid' 列でグループ化しています。これにより、同じ 'userid' を持つ行が同じグループに含まれます。

# 各 'userid' グループに対して、次の処理を実行します：
# reset_indices は、'conditional_cumsum' 列が0にリセットされる行のインデックスを含むインデックスのリストです。
# cumsum は、累積購入回数をリセットしたり、1ずつ増加させたりするための変数です。
# 各 'userid' グループ内で、行ごとにループ処理を行います。

# もし行のインデックスが reset_indices 内に存在する場合（つまり、累積購入回数が0にリセットされる場合）、cumsum を1にリセットします。
# 'conditional_cumsum' 列に cumsum の値を設定し、この列の値を更新します。
# cumsum を1ずつ増加させ、次の行の 'conditional_cumsum' 列の値を設定するために使用します。
# このようにして、条件付きの累積購入回数を計算し、条件を満たす場合にリセットすることができます。計算結果は 'conditional_cumsum' 列に格納されます。



# 具体例を挙げて説明して
# 具体的な例を示して、提供されたコードの動作を詳しく説明します。
# 以下のようなデータを持つDataFrameを考えましょう：
import pandas as pd

data = {'userid': [1, 1, 1, 2, 2, 2, 3, 3, 3],
        'cumsum': [1, 2, 3, 1, 2, 3, 1, 2, 3],
        'out_of_stock_date_plus_180_days': ['2023-01-01', '2023-03-01', '2023-05-01',
                                            '2023-02-15', '2023-04-15', '2023-06-15',
                                            '2023-01-10', '2023-03-10', '2023-05-10'],
        'repurchase_within_out_of_stock_date_plus_180_days_flag': [0, 1, 0, 1, 1, 0, 0, 0, 1]}

df = pd.DataFrame(data)
df['out_of_stock_date_plus_180_days'] = pd.to_datetime(df['out_of_stock_date_plus_180_days'])
# このDataFrameには、ユーザーごとの cumsum 列（通常の累積購入回数）、out_of_stock_date_plus_180_days 列（商品が切れる日から180日後の日付）、および repurchase_within_out_of_stock_date_plus_180_days_flag 列（再購入が商品が切れる日から180日以内にあるかどうかを示すフラグ）が含まれています。
# 提供されたコードを実行して、条件付きの累積購入回数を計算しましょう：

# 累積購入回数をコピー
df["conditional_cumsum"] = df["cumsum"]

# 条件を満たす行のインデックスを取得
condition = ((pd.Timestamp.now() + pd.Timedelta(hours=9)) > df["out_of_stock_date_plus_180_days"]) & (df["repurchase_within_out_of_stock_date_plus_180_days_flag"] == 0)
reset_indices = df.index[condition]

# 条件を満たす行の 'conditional_cumsum' 列を0にリセット
df.loc[reset_indices, "conditional_cumsum"] = 0

# 'userid' でグループ化
groups = df.groupby('userid')

# 各 'userid' グループに対して処理を実行
for _, group in groups:
    condition = (group["conditional_cumsum"] == 0)
    reset_indices = group[condition].index
    cumsum = 1
    for index, row in group.iterrows():
        if index in reset_indices:
            cumsum = 1
        df.at[index, 'conditional_cumsum'] = cumsum
        cumsum += 1

# このコードは次のように動作します：
# cumsum 列を conditional_cumsum 列にコピーします。これにより、通常の累積購入回数を conditional_cumsum にコピーします。
# 条件を満たす行を特定し、その行のインデックスを reset_indices に格納します。条件は、商品が切れる日から180日以内に再購入しておらず、現在の日時がその日付よりも未来である場合です。
# 条件を満たす行の conditional_cumsum 列を0にリセットします。
# userid でグループ化し、各 userid グループに対してループ処理を行います。
# 各 userid グループ内で、条件を満たす行のインデックスを特定し、その行の conditional_cumsum 列をリセットし、累積購入回数を計算します。リセットは条件を満たす行に対して行われ、累積購入回数が0から再び1に増加します。
# 最終的に、conditional_cumsum 列には条件付きの累積購入回数が格納され、リセットが必要な場合に正しくリセットされています。
