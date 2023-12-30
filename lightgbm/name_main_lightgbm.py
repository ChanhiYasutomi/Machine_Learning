if __name__=='__main__':
    model = LightGBM()
    start_time = time.time()                                               # 開始時間を取得する
    model.train()
    end_time = time.time()                                                 # 終了時間を取得する
    elapsed_time = end_time - start_time                                   # 経過時間を計算する
    minutes, seconds = divmod(elapsed_time, 60)
    fpr, tpr, auc = model.test(_acc=False)
    model.get_best_params()
    model.get_importance()
    data_name = dataset_filepath.replace("./data/", "")
    data_name = data_name.replace(".csv", "")
    filename = './data/' + f'{data_name}_model_on_optuna_' + time.strftime('%Y%m%d') + '.pkl'          # modelを保存する
    with open(filename, mode='wb') as f:
        pickle.dump(model.res.best_estimator_, f)
    print(f"Elapsed time: {int(minutes)} minutes {int(seconds)} seconds")   # 経過時間を表示する
    gc.collect()

# このコードは、LightGBM クラスを使用してモデルのトレーニング、評価、および最適化を実行するためのスクリプトです。以下は、スクリプトの主要な部分と役割の説明です：

# if __name__=='__main__': ブロック:
# if __name__=='__main__':
# このブロックは、スクリプトが直接実行された場合に実行されます。
# LightGBM クラスのインスタンスを作成し、モデルのトレーニング、評価、最適化を実行します。

# モデルのインスタンス化:
# model = LightGBM()
# LightGBM クラスのインスタンスを作成します。

# トレーニング時間の計測:
# start_time = time.time()  # 開始時間を取得する
# モデルのトレーニング開始時刻を記録します。

# モデルのトレーニング:
# model.train()
# LightGBM クラス内で定義された train メソッドを呼び出し、モデルのトレーニングを行います。

# 評価と結果の保存:
# fpr, tpr, auc = model.test(_acc=False)
# LightGBM クラス内で定義された test メソッドを呼び出し、モデルの評価を行います。_acc=False はAccuracyの表示を無効にします。
# モデルの最適なハイパーパラメータ、特徴量の重要度を表示します。

# モデルの保存:
# filename = './data/' + f'{data_name}_model_on_optuna_' + time.strftime('%Y%m%d') + '.pkl'
# モデルを保存するファイル名を生成します。
# pickle を使用して最適なモデルをファイルに保存します。

# 経過時間の表示:
# print(f"Elapsed time: {int(minutes)} minutes {int(seconds)} seconds")
# モデルのトレーニングと評価にかかった経過時間を表示します。

# メモリの解放:
# gc.collect()
# メモリの解放を行います。不要なメモリを解放してリソースを効率的に使用します。

# このスクリプトは、LightGBMモデルをトレーニングし、評価し、最適なハイパーパラメータを見つけてモデルを保存するための一連の手順を実行します。
