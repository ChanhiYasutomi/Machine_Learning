%%time
# 計算時間はかかる
import shap

# 文字化けしている場合は英語に変える
X_en = X.columns

# Explain predictions
print("step1...")
explainer = shap.TreeExplainer(best_model_on_LGBM)
print("step2...")
shap_values = explainer.shap_values(X_en)          # shap_values はリスト形式

# SHAP Summary Plot
print("step3...")
display(shap.summary_plot(shap_values, X_en))      # bar style
display(shap.summary_plot(shap_values[0], X_en))   # dot style

# このPythonコードは、SHAP（SHapley Additive exPlanations）を使用してモデルの予測を説明するプロセスを示しています。SHAPは、機械学習モデルの予測を個々の特徴量への寄与に分解し、予測を説明するのに役立ちます。以下は、このコードの詳細な説明です：

# shap.TreeExplainer オブジェクトの作成：
# shap.TreeExplainer クラスは、木ベースのモデル（ここではLightGBMモデル）に対するSHAP値を計算するためのオブジェクトです。best_model_on_LGBM は、解釈対象のLightGBMモデルです。このモデルに対して TreeExplainer オブジェクトを作成します。

# SHAP値の計算：
# explainer.shap_values(X_en) は、SHAP値を計算するための関数です。X_en は、解釈したいデータセットです。計算されたSHAP値は、特徴量ごとに各サンプルの寄与を表現するリストです。このコードでは、shap_values に計算されたSHAP値が格納されます。

# SHAP Summary Plotの作成：
# shap.summary_plot(shap_values, X_en) と shap.summary_plot(shap_values[0], X_en) は、SHAP Summary Plot（特徴量の重要度を可視化したグラフ）を作成します。
# shap.summary_plot 関数は、SHAP値を使用して各特徴量の重要性を可視化し、モデルの予測をどのように説明しているかを理解するのに役立ちます。この関数は、棒グラフまたはドットプロットのスタイルで特徴量の重要性を表示できます。

# このコードの主要な目的は、モデルが予測を行う際の各特徴量の寄与を視覚化し、モデルの予測を説明するためのインサイトを提供することです。また、SHAPを使用することで、モデルがなぜ特定の予測を行ったのかを理解するのに役立ちます。
