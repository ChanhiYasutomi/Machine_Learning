# 土曜、日曜のみを休日とする簡易的な休日判定です。
# judge_holiday 関数は、与えられた曜日情報をもとに、その日が週末（土曜日または日曜日）であるかどうかを判定するための関数です。具体的な例を挙げて説明します。
def judge_holiday(dayofweek):
    return np.where((dayofweek == 5) | (dayofweek == 6), 1, 0)
    
# 曜日情報（0: 月曜日, 1: 火曜日, 2: 水曜日, 3: 木曜日, 4: 金曜日, 5: 土曜日, 6: 日曜日）を含むデータを作成
import numpy as np
dayofweek_data = np.array([0, 1, 2, 3, 4, 5, 6])

# 'judge_holiday' 関数を使用して週末かどうかを判定し、結果を表示
is_holiday = judge_holiday(dayofweek_data)

# 判定結果を表示
display(is_holiday)

# このコードでは、dayofweek_data という配列を作成し、それぞれの要素が曜日を表しています。judge_holiday 関数を使用して、各曜日が週末（土曜日または日曜日）かどうかを判定し、結果を is_holiday 配列に格納しています。
# 出力結果は以下のようになります：

# [0 0 0 0 0 1 1]
# 結果の配列では、土曜日と日曜日が1で、それ以外の曜日は0で表されています。このように、judge_holiday 関数を使用することで、曜日データから週末を判定できます。
