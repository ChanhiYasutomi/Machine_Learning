# 次の日が休日であるかを判定
# 分析する問題によっては、当日が休日であるよりも、次の日が休日であるかが重要な場合もあります。

def judge_next_day_is_holiday(dayofweek):
    return np.where((dayofweek == 4) | (dayofweek == 5), 1, 0)

# judge_next_day_is_holiday 関数は、与えられた曜日情報をもとに、翌日が週末（金曜日または土曜日）かどうかを判定するための関数です。具体的な例を挙げて説明します。
import numpy as np

# 曜日情報（0: 月曜日, 1: 火曜日, 2: 水曜日, 3: 木曜日, 4: 金曜日, 5: 土曜日, 6: 日曜日）を含むデータを作成
dayofweek_data = np.array([0, 1, 2, 3, 4, 5, 6])

# 'judge_next_day_is_holiday' 関数を使用して翌日が週末かどうかを判定し、結果を表示
is_next_day_holiday = judge_next_day_is_holiday(dayofweek_data)

# 判定結果を表示
display(is_next_day_holiday)

# このコードでは、dayofweek_data という配列を作成し、それぞれの要素が曜日を表しています。judge_next_day_is_holiday 関数を使用して、各曜日の翌日が週末（金曜日または土曜日）かどうかを判定し、結果を is_next_day_holiday 配列に格納しています。

# 出力結果は以下のようになります：
# [0 0 0 0 1 1 0]
# 結果の配列では、金曜日と土曜日の前日が1で、それ以外の曜日の前日は0で表されています。このように、judge_next_day_is_holiday 関数を使用することで、曜日データから翌日が週末かどうかを判定できます。
