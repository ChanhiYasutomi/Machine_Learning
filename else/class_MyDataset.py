class MyDataset(torch.utils.data.Dataset):
    
    def __init__(self, filepath=dataset_filepath, target='target'):
        self.df = pd.read_csv(filepath)
        
        # リークになりそうなカラムと余計なカラムを削除する
        if filepath == 'xxx.csv':
            # 2回目購入予測モデル のデータ
            self.df = self.df.drop(["colunms"], axis=1)
        elif filepath == 'xxx.csv':
            # 3回目「以上」購入予測モデル のデータ
            self.df = self.df.drop(["colunms"], axis=1)
        else:
            raise("どちらのデータセットでもない")
        
        self.target = target
        self.columns = list(self.df.columns.copy())
        self.columns.remove(target)
        self.setup()
    
    def __len__(self):
        return len(self.label)

    def __getitem__(self, idx):
        return self.df[idx], self.label[idx]

    def setup(self, undersampling=True, coef=1):
        """
        不均衡データなので target が 1:1 になるように調整している
        """
        self.label = self.df[self.target].to_numpy()
        cc = Counter(self.label)
        print('balance before undersampling:', cc)
        ratio = cc[1]/cc[0]
        if undersampling and (ratio > coef or ratio < 1/coef):
            minority_class = 0 if ratio > coef else 1
            minority_indices = [i for i, l in enumerate(self.label) if l == minority_class]
            majority_indices = [i for i, l in enumerate(self.label) if l != minority_class]
            majority_indices = resample(majority_indices, n_samples=coef*cc[minority_class])
            undersampled_indices = minority_indices + majority_indices
            self.label = self.label[undersampled_indices]
            self.df = self.df.iloc[undersampled_indices]
        self.df = self.df.drop(self.target, axis=1).to_numpy()

# このコードは、機械学習モデルのトレーニングと評価のためにデータを準備するカスタムデータセットクラス MyDataset の実装です。以下に、コード内の主要な構造と各部分の詳細を説明します。

# MyDataset クラスの定義:
# class MyDataset(torch.utils.data.Dataset):
# このクラスは、PyTorchのデータセットクラスを継承しています。

# __init__ メソッド:
# def __init__(self, filepath=dataset_filepath, target='target'):
# データセットの初期化を行います。
# filepath パラメータは、データが格納されたCSVファイルのファイルパスを指定します。
# target パラメータは、予測対象の目的変数のカラム名を指定します。

# データの読み込みと前処理:
# self.df = pd.read_csv(filepath)
# CSVファイルからデータを読み込み、self.df にデータフレームとして格納します。
# リークを防ぐため、不要なカラムを削除します。これはデータをクリーニングし、モデルのトレーニングに不要な情報を取り除く重要なステップです。

# __len__ メソッド:
# def __len__(self):
# データセット内のサンプル数を返します。

# __getitem__ メソッド:
# def __getitem__(self, idx):
# 指定されたインデックス idx のデータと対応するラベルを返します。これは、データセット内の各サンプルへのアクセス方法を提供します。

# setup メソッド:
# def setup(self, undersampling=True, coef=1):
# データセットのセットアップを行います。不均衡なクラス分布を持つデータセットの場合、バランスを調整するための処理が行われます。
# アンダーサンプリングを有効にする場合、少数クラス（0または1など）のサンプル数が多数クラスに合わせて調整されます。
# coef パラメータを使用して、アンダーサンプリングの程度を調整できます。均衡したデータセットを作成することが目的です。
# このカスタムデータセットクラス MyDataset は、不均衡なデータセットでクラスバランスを調整し、機械学習モデルのトレーニングに使用するためのデータを効果的に準備するために使用されます。
