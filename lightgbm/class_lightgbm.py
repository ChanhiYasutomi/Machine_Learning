class LightGBM:
    
    def __init__(self):
        self.param_grid = {
            'num_leaves': optuna.distributions.IntDistribution(10, 1000),
            'learning_rate': optuna.distributions.FloatDistribution(1e-3, 1e-1),
            'colsample_bytree': optuna.distributions.FloatDistribution(0.1, 0.9),
            'subsample': optuna.distributions.FloatDistribution(0.1, 0.9),
            'min_child_samples': optuna.distributions.IntDistribution(10, 100),
            'early_stopping_rounds': optuna.distributions.IntDistribution(100, 300),
            'max_depth': optuna.distributions.IntDistribution(3, 30),
            'n_estimators': optuna.distributions.IntDistribution(50, 200)
        }
        self.estimator = lgb.LGBMClassifier(objective='binary')
        self.setup()
    
    def setup(self, ratio=0.1):
        print('setup...')
        dataset = MyDataset()
        self.columns = dataset.columns
        print('save features...')
        # txtファイルに特徴量を保存する
        if dataset_filepath == 'xxx.csv':
            filename = 'xxx.txt'
        elif dataset_filepath == 'yyy.csv':
            filename = 'yyy.txt'
        with open(filename, 'w') as f:
          for name in self.columns:
            f.write(name + '\n')
        length = len(dataset)
        test_length = int(length*ratio)
        # 8:1:1 に分割
        self.train_dataset, self.val_dataset, self.test_dataset = random_split(dataset, [length-2*test_length, test_length, test_length])
        del dataset
    
    def get_best_params(self):
        print(self.res.best_params_)
        
    def get_importance(self):
        """
        特徴量重要度を追加
        """
        best_model = self.res.best_estimator_
        df = pd.Series(best_model.feature_importances_, index=self.columns).to_frame()
        df.columns = ['value']
        df.sort_values('value', inplace=True, ascending=False)
        print(df.head(10))
        lgb.plot_importance(best_model)
        
    def train(self):
        print('training...')
        # self.res = GridSearchCV(
        #   estimator=self.estimator, 
        #    param_grid=self.param_grid,
        #    cv=5,
        #    verbose=2,
        #    n_jobs=-1, 
        #    scoring='roc_auc')
        
        # OptunaSearchCVを用いる
        self.res = OptunaSearchCV(
            self.estimator,
            self.param_grid,
            n_trials=100,
            random_state=6481,
            cv=5,
            verbose=2,
            n_jobs=-1,
            scoring='roc_auc')
        
        X, y = self.train_dataset[:]
        val_X, val_y = self.val_dataset[:]
        self.res.fit(X, y, eval_set=[(val_X, val_y)])
        del X, y
    
    def test(self, _acc=True, _auc=True, _cm=True):
        best_model = self.res.best_estimator_
        X, y = self.test_dataset[:]
        pred       = best_model.predict(X)
        pred_proba = best_model.predict_proba(X)[:,1]
        
        ### display Accuracy
        print('accuracy:%.3f' % accuracy_score(y, pred)) if _acc else 0
        
        ### display AUC
        if _auc:
            print('#total:',len(y))
            fpr, tpr, thresholds = roc_curve(y, pred, pos_label=1)
            auc = roc_auc_score(y, pred_proba)
            print('AUC:%.3f' % auc)
            # print('fpr: ', fpr)
            # print('tpr: ', tpr)
        
        ### display confusion matrix
        print('confusion matrix:\n', confusion_matrix(y, pred)) if _cm else 0
        del X, y
        
        return fpr, tpr, auc

# このコードは、LightGBMを使用したバイナリ分類のモデルをトレーニング、評価、およびチューニングするためのクラス LightGBM を定義しています。以下は、このクラスの主要な部分と役割の説明です：

# __init__ メソッド:
# def __init__(self):
# このメソッドは、LightGBMモデルとそのハイパーパラメータ探索用のグリッドを初期化します。
# param_grid メンバ変数は、Optunaを使用してチューニングするハイパーパラメータの範囲を指定します。
# estimator メンバ変数は、LightGBMの分類器を初期化します。
# setup メソッドを呼び出し、データのセットアップと特徴量の保存を行います。

# setup メソッド:
# def setup(self, ratio=0.1):
# このメソッドは、データセットのセットアップと特徴量の保存を行います。
# データセットを MyDataset クラスを使用して読み込み、特徴量のリストを取得します。
# 特徴量のリストをテキストファイルに保存します。
# データセットをトレーニング、検証、テストセットに分割します。

# get_best_params メソッド:
# def get_best_params(self):
# ハイパーパラメータチューニングの結果、最適なハイパーパラメータを表示します。

# get_importance メソッド:
# def get_importance(self):
# トレーニングされたモデルの特徴量の重要度を表示します。
# feature_importances_ を使用して特徴量の重要度を取得し、表示します。

# train メソッド:
# def train(self):
# モデルのトレーニングを行います。
# Optunaを使用して最適なハイパーパラメータを見つけ、指定されたデータセットでモデルをトレーニングします。

# test メソッド:
# def test(self, _acc=True, _auc=True, _cm=True):
# テストデータでモデルの評価を行います。
# Accuracy、AUC、混同行列を表示します。
# _acc、_auc、_cm パラメータを使用して表示するメトリクスを制御します。

# このクラスは、LightGBMモデルのトレーニングと評価の一連のステップを効率的に実行し、ハイパーパラメータの最適化を自動化するために使用できます。
