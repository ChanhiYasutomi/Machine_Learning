def setup(df, undersampling=True, coef=1):
    """
    不均衡データなので target が 1:1 になるように調整している
    """
    target = "target"
    label = df[target].to_numpy()
    cc = Counter(label)
    print('balance before undersampling:', cc)
    ratio = cc[1]/cc[0]
    if undersampling and (ratio > coef or ratio < 1/coef):
        minority_class = 0 if ratio > coef else 1
        minority_indices = [i for i, l in enumerate(label) if l == minority_class]
        majority_indices = [i for i, l in enumerate(label) if l != minority_class]
        majority_indices = resample(majority_indices, n_samples=coef*cc[minority_class])
        undersampled_indices = minority_indices + majority_indices
        # label = label[undersampled_indices]
        # df = df.iloc[undersampled_indices]
    # df = df.drop(target, axis=1).to_numpy()
    
    # undersampled_indices を返すように変更
    return undersampled_indices
    
    
idx = setup(df)
idx[:10]

# このPythonコードは、不均衡データのターゲット（target）のクラスバランスを調整するための関数 setup() を示しています。この関数は、データフレーム（df）とオプションのパラメータ（undersampling および coef）を受け取ります。以下は、この関数の詳細な説明です：
# undersampling パラメータ（デフォルトは True）は、クラスバランスの調整を実行するかどうかを制御します。True の場合、クラスバランスの調整を実行します。
# coef パラメータ（デフォルトは 1）は、クラスバランスを調整する際のマイノリティクラスのサンプル数とマジョリティクラスのサンプル数の比率を設定します。例えば、coef が 0.5 の場合、マイノリティクラスのサンプル数はマジョリティクラスのサンプル数の半分になります。

# この関数は次の手順で動作します：
# ターゲット列からラベルを取得し、クラスバランスを評価します。
# undersampling パラメータが True で、クラスバランスの調整が必要な場合、マイノリティクラスとマジョリティクラスのインデックスを特定します。
# マイノリティクラスとマジョリティクラスのインデックスを使用して、クラスバランスを調整します。マイノリティクラスのサンプル数が coef 倍になるように、マジョリティクラスからサンプルをアンダーサンプリングします。
# クラスバランスが調整されたデータセットのインデックスを返します。
# 最後の部分では、setup() 関数を呼び出し、調整されたデータセットのインデックスを idx に格納しています。このインデックスは、調整されたデータセット内のサンプルを指すために使用できます。
