%%time
# 予測
X = df[feature_names].values
y = df["target"].values

pred = best_model_on_LGBM.predict(X)
df["予測結果"] = pred

fpr, tpr, thresholds = roc_curve(y, pred, pos_label=1)
cm = confusion_matrix(y, pred)

print()
print("trainデータも含まれているので AUC が高めに出る")
print('AUC:%.3f' % auc(fpr, tpr))
print('confusion matrix:\n', cm)
print()

# ヒートマップで混同行列を表示する
sns.set(font_scale=1.4)  # フォントサイズを指定する
sns.heatmap(cm, annot=True, cmap="Blues", fmt='d', cbar=True)  # ヒートマップを描画する
plt.title('Confusion Matrix')  # タイトルを設定する
plt.xlabel('Predicted Labels')  # x軸のラベルを設定する
plt.ylabel('True Labels')  # y軸のラベルを設定する
plt.show()  # ヒートマップを表示する

# このコードは、モデルを使用してデータを予測し、予測結果を評価するためのものです。具体的には、以下のステップが含まれています。

# データの準備:
# 特徴量（feature_namesで指定されたカラム）とターゲット（targetカラム）を抽出し、NumPy配列としてXとyに格納します。

# 予測:
# LightGBMモデル（best_model_on_LGBM）を使用して、特徴量Xから予測を行い、その結果をpredに格納します。

# AUCの計算:
# roc_curve関数を使用して、予測結果と真のターゲットyに基づいてROC曲線のデータを計算します。
# AUC（ROC曲線の下の面積）を計算し、その結果を表示します。

# 混同行列の表示:
# 混同行列（confusion matrix）は、真陽性（True Positives）、偽陽性（False Positives）、真陰性（True Negatives）、偽陰性（False Negatives）のカウントを示す行列です。
# confusion_matrix関数を使用して、予測結果と真のターゲットに基づいて混同行列を計算します。
# 混同行列をヒートマップとして表示し、分類モデルの性能を視覚化します。

# このコードを実行することで、モデルの性能を評価できます。特にAUCや混同行列は、分類モデルの性能を評価するための重要な指標です。ヒートマップを通じて、モデルがどのクラスをどの程度正確に予測できているかを可視化することができます。
