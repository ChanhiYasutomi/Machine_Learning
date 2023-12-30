# 主成分分析と因子分析
#標準化
dfs = df.iloc[:, 0:].apply(lambda x: (x-x.mean())/x.std(), axis=0)
# データフレーム df の各列データを標準化します。標準化は各列の平均を引いてから標準偏差で割る操作で、データを平均が0、標準偏差が1に変換します。

#主成分分析の実行
pca = PCA()
pca.fit(dfs)
# 主成分分析（PCA）を行うための PCA クラスを使用し、fit メソッドで標準化されたデータに適合させます。

# データを主成分空間に写像
feature = pca.transform(dfs)
# データを主成分空間に写像します。transform メソッドを使用して、各サンプルを主成分の空間に変換します。

# 主成分得点
pd.DataFrame(feature, columns=["PC{}".format(x + 1) for x in range(len(dfs.columns))]).head()
# 変換されたデータをデータフレームに変換し、各主成分の得点を表示します。

# 第一主成分と第二主成分でプロットする
plt.figure(figsize=(8, 6))
plt.scatter(feature[:, 0], feature[:, 1], alpha=0.8, c=list(df.iloc[:,1]))  #カラーは目的変数
plt.colorbar()
plt.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()
# 主成分得点を用いて、第一主成分と第二主成分の空間でデータをプロットします。カラーはデータフレーム df の2列目（目的変数）に対応しています。

#因子分析
plt.figure(figsize=(6, 6))
for x, y, name in zip(pca.components_[0], pca.components_[1], dfs.columns[0:]):
    plt.text(x, y, name)
plt.scatter(pca.components_[0], pca.components_[1], alpha=0.8)
plt.grid()
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()

# 因子分析の結果をプロットします。各変数（特徴）が第一主成分と第二主成分に対してどのように影響しているかが視覚的に分かります。



# 主成分得点（Principal Component Scores）は、主成分分析（PCA）の結果得られるもので、元のデータを新しい主成分空間に写像した際の各サンプル（観測値）の位置を示します。
# 以下に、Pythonでの具体例を挙げて説明します。
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# サンプルデータの作成
np.random.seed(42)
data = np.random.rand(10, 3)  # 10サンプル x 3変数のデータ

# データフレームの作成
df = pd.DataFrame(data, columns=["A", "B", "C"])

# データの標準化
dfs = df.apply(lambda x: (x - x.mean()) / x.std(), axis=0)

# 主成分分析の実行
pca = PCA()
pca.fit(dfs)

# データを主成分空間に写像
feature = pca.transform(dfs) # featureが主成分得点

# 主成分得点の表示
pc_df = pd.DataFrame(feature, columns=["PC{}".format(x + 1) for x in range(len(dfs.columns))])
print("Principal Component Scores:")
display(pc_df)

# この例では、df は元のデータフレーム、dfs はデータの標準化、pca は主成分分析のインスタンスです。
# pca.fit(dfs) で主成分分析を実行し、pca.transform(dfs) でデータを主成分空間に写像しています。
# 結果として得られる feature が主成分得点です。

# 主成分得点は、元のデータセットの各サンプルに対して、新しい主成分軸上での座標を示しています。 
# PC1、PC2、PC3 などの列が、それぞれの主成分に対応しています。
# これをデータフレームにして表示すると、各サンプルの主成分得点が確認できます。



# 主成分得点（Principal Component Scores）は、主成分分析（PCA）において、元のデータを新しい座標系で表現した際の各観測点（サンプル）の座標です。
# PCAはデータの次元を削減する手法であり、主成分得点はデータを主成分軸上に射影した結果として得られます。

# 以下に、主成分得点に関する重要なポイントを説明します：
# 主成分得点の計算:
# 主成分得点は、各主成分に対する重み付きの元の変数の合計です。
# 具体的には、各主成分におけるデータの射影が計算され、これが主成分得点となります。主成分得点は、各サンプルごとに主成分空間上の座標を表します。

# 主成分得点の列数:
# 主成分得点の列数は、主成分の数に等しいです。
# 各列がそれぞれの主成分に対応しており、「PC1」、「PC2」、「PC3」といったラベルが通常使われます。

# 主成分得点の解釈:
# 主成分得点は、元の変数と主成分の関係を表しています。
# 主成分得点が大きいほど、元のデータがその主成分に対して重要であると解釈できます。
# 主成分得点の符号も重要で、同じ符号の主成分得点は正の相関があります。

# 主成分得点の利用:
# 主成分得点はデータの可視化や分析に利用されます。
# 例えば、主成分得点を用いて散布図を作成することで、データの構造やクラスタリングを視覚的に理解することができます。

# 簡単な例を挙げると、次元削減された主成分得点を用いて、データセット内のパターンや傾向を把握することが可能です。
