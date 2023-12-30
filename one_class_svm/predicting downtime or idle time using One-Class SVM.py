# 医師のすきま時間の予測にOne-Class SVMを使用するための具体的なPythonコードを示します。
# この例では、医師の患者診察のすきま時間を予測します。One-Class SVMは、通常のパターンから外れる異常な時間スロットを特定するのに役立ちます。

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 次に、擬似的なデータを生成します。医師の診察時間のデータとして、正規の診察時間とそれから外れる異常な時間を生成します。
# 正規の診察時間データ（平均: 10分、標準偏差: 2分）
normal_times = np.random.normal(10, 2, 100)

# 異常な時間データ（外れ値：30分と40分）
anomalous_times = np.array([30, 40])

# 正規データと異常データを結合
data = np.concatenate((normal_times, anomalous_times), axis=0)

# データを可視化
plt.hist(data, bins=20)
plt.xlabel('consultation hours（minutes）')
plt.ylabel('frequency')
plt.title('data of consultation hours')
plt.show()

# データを可視化した後、One-Class SVMを使用して異常検出を行います。以下はそのコードです：
# One-Class SVMモデルを初期化
clf = OneClassSVM(kernel='rbf', nu=0.05)  # nuは異常値の割合を指定

# データをモデルに適合
clf.fit(data.reshape(-1, 1))

# データポイントの異常スコアを計算
anomaly_scores = clf.decision_function(data.reshape(-1, 1))

# 異常スコアをプロット
plt.plot(data, anomaly_scores, 'bo')
plt.xlabel('consultation hours（minutes）')
plt.ylabel('abnormal score')
plt.title('abnormal detection by One-Class SVM')
plt.show()

# このコードでは、One-Class SVMモデルを使用して異常スコアを計算し、異常スコアをプロットしています。異常スコアが高いデータポイントは異常な時間スロットを示し、異常スコアが低いデータポイントは正規の時間スロットを示します。
# 異常スコアが閾値を超えるデータポイントを検出することで、医師のすきま時間を予測することができます。閾値は具体的なアプリケーションや要件に応じて調整する必要があります。
