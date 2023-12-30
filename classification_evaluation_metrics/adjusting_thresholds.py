# 目的変数1 の割合が多すぎるので、閾値を調整
# 仮説：0 になるのが難しいため、確率が低すぎる場合のみ 0 として予測すると良いかもしれない

import pandas as pd
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score, roc_auc_score

# ターゲットと予測確率
y_true = df["target"]
y_scores = best_model_on_LGBM.predict_proba(X)[:,1]

# 結果を保存するためのデータフレーム
results_df = pd.DataFrame(columns=['Threshold', 'Accuracy', 'Recall', 'Precision', 'F1_Score', 'AUC'])

# 閾値を0.05ずつ動かしてメトリックを計算
for threshold in range(0, 105, 5):
    threshold /= 100
    y_pred = (y_scores > threshold).astype(int)
    accuracy = accuracy_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)
    auc = roc_auc_score(y_true, y_scores)
    results_df.loc[len(results_df)] = [threshold, accuracy, recall, precision, f1, auc]

# Accuracy, Recall, Precision, F1_Scoreの最大値を持つ行を見つける
max_accuracy_row = results_df['Accuracy'].idxmax()
max_recall_row = results_df['Recall'].idxmax()
max_precision_row = results_df['Precision'].idxmax()
max_f1_row = results_df['F1_Score'].idxmax()

# 新しいカラムに◯を追加
results_df['Max_Accuracy'] = ['◯' if i == max_accuracy_row else '' for i in range(len(results_df))]
results_df['Max_Recall'] = ['◯' if i == max_recall_row else '' for i in range(len(results_df))]
results_df['Max_Precision'] = ['◯' if i == max_precision_row else '' for i in range(len(results_df))]
results_df['Max_F1'] = ['◯' if i == max_f1_row else '' for i in range(len(results_df))]

print()

# データフレームの表示
results_df

# このPythonコードは、異なる確率閾値を使用して二項分類モデルの評価メトリクスを計算し、結果をデータフレームに格納し、表示する方法を示しています。以下は、コードの詳細な説明です：
# y_trueとy_scores：y_trueには実際のターゲット（正解ラベル）が格納され、y_scoresにはモデルの予測確率（クラス1の確率）が格納されています。
# 結果を保存するための空のデータフレームresults_dfを作成します。このデータフレームには、異なる確率閾値で計算されたメトリクス（Accuracy、Recall、Precision、F1スコア、AUC）が保存されます。

# 確率閾値を0から1まで0.05刻みで変化させながら、以下のメトリクスを計算し、results_dfに行を追加します：
# y_pred：確率が閾値を超えるかどうかを示す予測ラベル。
# accuracy：Accuracyスコアの計算。
# recall：Recallスコアの計算。
# precision：Precisionスコアの計算。
# f1：F1スコアの計算。
# auc：AUC（ROC曲線の下の面積）スコアの計算。
# 最大のAccuracy、Recall、Precision、F1スコアを持つ行を特定し、それぞれの行に"◯"を追加します。これにより、各メトリクスの最大値が視覚的に強調表示されます。
# 最終的に、results_dfを表示します。このデータフレームには、各確率閾値における異なるメトリクスの評価が含まれており、最適な閾値を見つけるのに役立ちます。

# このコードを実行すると、異なる確率閾値でのモデルのパフォーマンスが表示され、最適な閾値に基づいて最大のメトリクスが強調表示されます。
