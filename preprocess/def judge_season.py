# judge_season 関数は、与えられた月情報をもとに、季節を判定するための関数です。具体的な例を挙げて説明します。
def judge_season(month):
    if 3 <= month <=5:
        season = 0
    elif 6 <= month <= 8:
        season = 1
    elif 9 <= month <= 11:
        season = 2
    else:
        season = 3

# 月情報（1月から12月）を含むデータを作成
month_data = [1, 3, 5, 7, 9, 12]

# 'judge_season' 関数を使用して各月の季節を判定し、結果を表示
seasons = [judge_season(month) for month in month_data]

# 判定結果を表示
for month, season in zip(month_data, seasons):
    print(f"Month {month}: Season {season}")
このコードでは、month_data というリストを作成し、それぞれの要素が月を表しています。judge_season 関数を使用して、各月がどの季節に該当するかを判定し、結果を seasons リストに格納しています。

# 出力結果は以下のようになります：

# Month 1: Season 3
# Month 3: Season 0
# Month 5: Season 0
# Month 7: Season 1
# Month 9: Season 2
# Month 12: Season 3

# この結果から、各月がどの季節に該当するかが判定されています。たとえば、1月は冬季（季節コード 3）、3月と5月は春季（季節コード 0）などと判定されています。
