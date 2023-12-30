n_rows        = len(df)
new_user_ids  = list(range(1, n_rows+1))
df['user_id'] = new_user_ids

# 上記のコードは、DataFrame df に新しい 'user_id' カラムを追加し、各行に一意のユーザーIDを割り当てるための方法です。user_id は 1 からデータフレームの行数までの連番の整数で、各行にユニークな値を持ちます。

# このコードの主要な部分は以下です：
# n_rows = len(df) で、DataFrame df の行数を取得します。
# new_user_ids = list(range(1, n_rows+1)) で、1 から行数までの整数のリストを作成します。これは新しい 'user_id' カラムの値として使用されます。
# df['user_id'] = new_user_ids で、新しい 'user_id' カラムを DataFrame に追加します。各行に対して、対応する新しいユーザーIDが割り当てられます。

# これにより、DataFrame の各行にユニークな 'user_id' が付与され、行数に合わせて連番が割り当てられます。
