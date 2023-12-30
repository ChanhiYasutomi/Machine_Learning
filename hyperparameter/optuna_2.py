import optuna
import lightgbm as lgb
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from optuna.integration import OptunaSearchCV

# データをロードして分割する
breast_cancer = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    breast_cancer.data, breast_cancer.target, random_state=0)

# モデルを定義する
model = lgb.LGBMClassifier()

# ハイパーパラメータの範囲を定義する
param_distributions = {
    'num_leaves': optuna.distributions.IntDistribution(10, 1000),
    'learning_rate': optuna.distributions.FloatDistribution(1e-3, 1e-1),
    'colsample_bytree': optuna.distributions.FloatDistribution(0.1, 0.9),
    'subsample': optuna.distributions.FloatDistribution(0.1, 0.9),
    'min_child_samples': optuna.distributions.IntDistribution(10, 100),
    'early_stopping_rounds': optuna.distributions.IntDistribution(100, 300),
    'max_depth': optuna.distributions.IntDistribution(3, 30),
    'n_estimators': optuna.distributions.IntDistribution(50, 200)
}

# OptunaSearchCVを用いてグリッドサーチを実行する
optuna_search = OptunaSearchCV(
    model,
    param_distributions,
    n_trials=100,
    random_state=6481,
    scoring='roc_auc',
    cv=5,
    verbose=2,
    n_jobs=-1
)

# グリッドサーチを実行する
optuna_search.fit(X_train, y_train)

# テストデータで予測を評価する
y_pred = optuna_search.predict(X_test)
score = roc_auc_score(y_test, y_pred)
print(f'Test AUC: {score:.3f}')

# 上記のコードは、Optunaを使用してLightGBMモデルのハイパーパラメータチューニングを行う例です。以下はこのコードの詳細な説明です。

# データのロードと分割：
# load_breast_cancer() 関数を使用して、乳がんのデータセットをロードします。
# train_test_split() 関数を使用して、データをトレーニングセット（X_trainとy_train）とテストセット（X_testとy_test）に分割します。

# モデルの定義：
# LightGBMの分類モデル LGBMClassifier を model として定義します。

# ハイパーパラメータの範囲の定義：
# param_distributions 辞書内で、ハイパーパラメータの探索範囲を指定します。例えば、'num_leaves' の値の範囲は10から1000までの整数です。

# OptunaSearchCVの設定：
# OptunaSearchCV クラスを使用して、Optunaを統合したグリッドサーチを設定します。
# model：モデル
# param_distributions：ハイパーパラメータの探索範囲
# n_trials：Optunaの試行回数
# random_state：ランダムシード
# scoring：評価指標（ROC AUCスコア）
# cv：交差検証の分割数
# verbose：詳細なログ表示
# n_jobs：並列処理に使用するコア数（-1はすべての利用可能なコアを使用）

# グリッドサーチの実行：
# optuna_search.fit() を使用して、Optunaを統合したグリッドサーチを実行します。

# テストデータでの評価：
# 最適なモデルでテストデータに対する予測を行い、ROC AUCスコアを計算します。
# 結果を表示します。

# このコードは、Optunaを使用してハイパーパラメータを調整し、最適なモデルを見つける典型的なハイパーパラメータチューニングの例です。 Optunaは、指定された試行回数内で最適なハイパーパラメータセットを探索するのに役立ちます。
