# 基礎集計ではアンダーサンプリングはしなくてもいい。理由は学習データの特徴を掴む必要があるから。
# アンダーサンプリングしてしまうと、目的変数の割合が 1:1 に近づくので基礎集計には使えなくなる。
# アンダーサンプリングしたことで、目的変数のバランスが崩れ、基礎集計の結果と変わる可能性がある

# データの読み込み
filepath = 'xxx.csv' 
df = pd.read_csv(filepath)

# 特徴量の読み込み
filepath = "xxx_add_feature.txt"

with open(filepath, 'r') as f:
    feature_names = [line.strip() for line in f.readlines()]
    
# モデルの読み込み
best_model_on_LGBM = pickle.load(open("./data/F1_dataset_add_features_model_on_optuna_20230719.pkl", 'rb'))

# このPythonコードは、データの読み込み、特徴量の読み込み、およびトレーニング済みのLightGBMモデルの読み込みの手順を示しています。以下は、各手順の詳細な説明です：

# データの読み込み：
# filepathに指定されたCSVファイルからデータを読み込みます。CSVファイルのパスは'xxx.csv'に設定されています。
# pd.read_csv(filepath)を使用してCSVファイルをPandasのデータフレームに読み込みます。読み込んだデータフレームはdfに格納されます。

# 特徴量の読み込み：
# filepathには特徴量のリストが格納されたテキストファイル（通常は.txt）のパスが指定されています。特徴量のファイルパスは'xxx_add_feature.txt'に設定されています。
# with open(filepath, 'r') as fを使用してテキストファイルを読み込みモードで開きます。
# for line in f.readlines()を使用してファイル内の各行を反復処理し、各行を特徴量名としてfeature_namesリストに追加します。各行の改行文字は.strip()を使用して削除されます。

# モデルの読み込み：
# トレーニング済みのLightGBMモデルを読み込みます。モデルファイルのパスは"./data/F1_dataset_add_features_model_on_optuna_20230719.pkl"に設定されています。
# pickle.load(open(model_filepath, 'rb'))を使用してモデルを読み込み、best_model_on_LGBMに格納します。'rb'はバイナリ読み込みモードを示します。

# これらの手順を実行することで、データフレームへのデータの読み込み、特徴量の読み込み、トレーニング済みのモデルの読み込みが行われ、これらのデータとモデルを後続の解析や予測に使用できるようになります。
