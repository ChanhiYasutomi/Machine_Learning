# モデルの読み込み
best_model_on_LGBM = pickle.load(open("./data/F2_dataset_add_features_model_on_optuna_20230824.pkl", 'rb'))

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import seaborn as sns

color_black = (76/255, 73/255, 72/255)
color0 = (18/255, 179/255, 199/255)
color1 = (62/255, 150/255, 210/255)
color2 = (20/255, 167/255, 157/255)
color3 = (173/255, 211/255, 97/255)
color4 = (232/255, 173/255, 95/255)
color5 = (215/255, 76/255, 119/255)
color6 = (139/255, 124/255, 186/255)

# データの読み込み
filepath = 'xxx.csv'
df = pd.read_csv(filepath)

# 特徴量の読み込み
filepath = "xxx.txt"

with open(filepath, 'r') as f:
    feature_names = [line.strip() for line in f.readlines()]
    
# 予測
X = df[feature_names].values
y = df["target"].values

pred = best_model_on_LGBM.predict(X)
df["予測結果"] = pred
pred_proba = best_model_on_LGBM.predict_proba(X)[:,1]
df["予測確率"] = pred_proba

auc = roc_auc_score(y, pred_proba)
cm = confusion_matrix(y, pred)

print()
print('AUC:%.3f' % auc)
print('confusion matrix:\n', cm)
print()

# ヒートマップで混同行列を表示する
sns.set(font_scale=1.4)  # フォントサイズを指定する
sns.heatmap(cm, annot=True, cmap="Blues", fmt='d', cbar=True)  # ヒートマップを描画する
plt.title('Confusion Matrix')  # タイトルを設定する
plt.xlabel('Predicted Labels')  # x軸のラベルを設定する
plt.ylabel('True Labels')  # y軸のラベルを設定する
plt.show()  # ヒートマップを表示する

# y: 目的変数
# pred: 予測値(0,1 の反転なし)

# 正解率 (Accuracy)
accuracy = accuracy_score(y, pred)
print("Accuracy:", accuracy*100)

# 再現率 (Recall)
recall = recall_score(y, pred)
print("Recall:", recall*100)

# 適合率 (Precision)
precision = precision_score(y, pred)
print("Precision:", precision*100)

# F1値 (F1)
f1 = f1_score(y, pred)
print("F1:", f1*100)

# このPythonコードは、保存されたLightGBMモデルを読み込み、新しいデータに対して予測を行い、混同行列（Confusion Matrix）とROC曲線のAUCスコアを計算して可視化する方法を示しています。以下は、コードの詳細な説明です。
# best_model_on_LGBM = pickle.load(open("./data/F2_dataset_add_features_model_on_optuna_20230824.pkl", 'rb'))：保存されたLightGBMモデルをバイナリ読み込みモードで開き、best_model_on_LGBM変数に読み込みます。このモデルは前のステップでトレーニングされたものです。

# データと特徴量の読み込み：
# filepath変数にデータファイル（xxx.csv）のパスを指定して、pd.read_csv()を使用してデータを読み込みます。
# 特徴量のリストをテキストファイルから読み込み、feature_names変数に格納します。

# 予測：
# X = df[feature_names].valuesで特徴量データを取得します。
# y = df["target"].valuesで目標変数データを取得します。
# best_model_on_LGBM.predict(X)で特徴量データから予測を行い、pred変数に格納します。
# best_model_on_LGBM.predict_proba(X)[:,1]で各データのクラス1の予測確率を取得し、pred_proba変数に格納します。

# AUCスコアと混同行列の計算と表示：
# roc_auc_score(y, pred_proba)でROC曲線のAUCスコアを計算し、auc変数に格納します。
# confusion_matrix(y, pred)で混同行列を計算し、cm変数に格納します。
# AUCスコアと混同行列をコンソールに表示します。

# 混同行列の可視化：
# sns.set(font_scale=1.4)でヒートマップのフォントサイズを設定します。
# sns.heatmap(cm, annot=True, cmap="Blues", fmt='d', cbar=True)で混同行列のヒートマップを描画します。
# プロットのタイトルやラベルを設定し、ヒートマップを表示します。

# このコードを実行すると、モデルの予測結果に関する詳細な評価が表示され、混同行列がヒートマップとして可視化されます。これにより、モデルのパフォーマンスが評価され、クラス分類の品質が視覚化されます。
