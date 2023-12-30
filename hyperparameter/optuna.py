# 全データの予測確率を計算します。
y_pred_prob = best_model_on_LGBM.predict_proba(X)[:,1]
# 念のため、numpy配列に変換する
y_pred_prob = np.array(y_pred_prob)

def objective(trial):
    # 閾値を提案します。
    threshold = trial.suggest_uniform('threshold', 0, 1)

    # 予測確率を基にクラスラベルを決定します。
    y_pred = (y_pred_prob > threshold).astype(int)

    # 評価指標を計算します。
    score = precision_score(y, y_pred)

    return score

# Optunaを使って閾値を最適化します。
study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=100)

print()
print()

# 最適な閾値を出力します。
print("Best threshold: ", study.best_params["threshold"])

# このコードは、Optunaを使用して予測確率の閾値を最適化するための例です。具体的な手順を説明します。
# まず、全データの予測確率を計算します。best_model_on_LGBMを使用して予測確率を取得し、y_pred_probに格納します。
# 次に、Optunaのobjective関数を定義します。この関数は、Optunaが最適な閾値を探索するために呼び出す関数です。関数内で、提案された閾値（trial.suggest_uniformを使用して0から1の範囲で提案）を使用して、予測確率からクラスラベルを生成します。そして、指定した評価指標であるPrecision（適合率）を計算します。この関数の目的は、Precisionを最大化する最適な閾値を見つけることです。
# Optunaのcreate_study関数を使用して新しいOptunaのStudyオブジェクト（最適化のための実行単位）を作成します。directionパラメータは、最適化の方向を指定します。ここでは、Precisionを最大化するために'maximize'を指定しています。
# study.optimizeメソッドを使用して、Objective関数を最適化します。n_trialsパラメータは、試行の回数を指定します。この例では100回の試行を行います。
# 最適な閾値はstudy.best_paramsから取得し、出力されます。

# Optunaは、指定した評価指標を最大化または最小化する最適なハイパーパラメータや閾値を見つけるための強力なツールです。このコードを使用することで、Precisionを最大化する最適な予測確率の閾値を見つけることができます。
