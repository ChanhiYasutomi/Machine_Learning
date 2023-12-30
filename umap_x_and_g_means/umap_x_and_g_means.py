https://cocoinit23.com/%E6%AC%A1%E5%85%83%E5%9C%A7%E7%B8%AE%E3%81%AEumap%E3%81%A7%E3%82%A8%E3%83%A9%E3%83%BC-module-umap-has-no-attribute-umap/
!pip install lightgbm optuna torch pyclustering -q
!pip install umap-learn -q
!pip install 'importlib-metadata>=4.8.1' -q

## UMAP で2次元に圧縮する
import umap
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 乱数の種を設定（再現性のため）
np.random.seed(42)

# 2つの特徴量を持つ1000個のランダムなデータポイントを生成
feature_1 = np.random.rand(1000)
feature_2 = np.random.rand(1000)

# データフレームに変換
df_random = pd.DataFrame({'Feature_1': feature_1, 'Feature_2': feature_2})

# UMAPモデルの作成とフィッティング
umap_model = umap.UMAP(n_components=2, random_state=42)
embedding = umap_model.fit_transform(df_random.values)

# 2次元データをデータフレームに変換
embedding_df = pd.DataFrame(embedding, columns=['UMAP_1', 'UMAP_2'])

# グラフの描画
plt.scatter(embedding_df['UMAP_1'], embedding_df['UMAP_2'], cmap='viridis')
plt.xlabel('UMAP Dimension 1')
plt.ylabel('UMAP Dimension 2')
plt.title('UMAP Projection')
plt.show()

# このコードは、umap-learnライブラリを使用してランダムなデータポイントを2次元に圧縮し、UMAPによるデータの視覚化を行います。UMAP（Uniform Manifold Approximation and Projection）は、高次元データを低次元に変換して可視化するための非線形次元削減手法の一つです。

# 以下はコードの詳細な説明です：
# np.random.seed(42)を使用して、乱数のシードを設定しています。これにより、ランダムなデータが再現可能になります。
# feature_1とfeature_2という2つの特徴量を持つ1000個のランダムなデータポイントを生成します。
# pd.DataFrameを使用して、これらの特徴量を持つデータフレーム df_random を作成します。
# UMAPモデルを作成します。umap.UMAPを使用し、n_componentsパラメータを2に設定して2次元に圧縮するように指定しています。また、random_stateパラメータを設定して再現性を確保しています。
# UMAPモデルを使って、元のデータポイントを2次元に圧縮し、embedding変数に格納します。
# 圧縮された2次元データをpd.DataFrameに変換し、embedding_dfに格納します。
# plt.scatterを使用して、2次元のUMAPプロジェクションを散布図として描画します。UMAP_1とUMAP_2は新しい2次元の特徴量です。 cmap='viridis'はカラーマップを指定しています。
# 最終的に、UMAPによって圧縮されたデータの2次元の可視化が表示されます。この方法を使用すると、高次元データを視覚的に理解しやすくすることができます。



# 必要なライブラリのインポート
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from pyclustering.cluster.gmeans import gmeans
from pyclustering.cluster.xmeans import xmeans
from pyclustering.cluster.center_initializer import kmeans_plusplus_initializer

# 説明変数と目的変数を分離
x = embedding_df['UMAP_1'].values
y = embedding_df['UMAP_2'].values
X = embedding_df.values

# X-means実行
xm_c = kmeans_plusplus_initializer(X, 2).initialize()
xm_i = xmeans(data=X, initial_centers=xm_c, kmax=10, ccore=False)
xm_i.process()

z_xm = np.ones(X.shape[0])
for k in range(len(xm_i._xmeans__clusters)):
    z_xm[xm_i._xmeans__clusters[k]] = k+1

# G-means実行
gm_c = kmeans_plusplus_initializer(X, 2).initialize()
gm_i = gmeans(data=X, initial_centers=gm_c, kmax=10, ccore=False)
gm_i.process()

z_gm = np.ones(X.shape[0])
for k in range(len(gm_i._gmeans__clusters)):
    z_gm[gm_i._gmeans__clusters[k]] = k+1

# グラフを描画
plt.title("Sample Origin")
plt.scatter(x,y,c='b',marker='o',s=50)
plt.grid()
plt.show()

plt.title("Sample X-means clster cls num: {}".format(len(xm_i._xmeans__clusters)))
plt.scatter(x,y, c=z_xm)
plt.grid()
centers = np.array(xm_i._xmeans__centers)
plt.scatter(centers[:,0],centers[:,1],s=250, marker='*',c='red')
plt.show()

plt.title("Sample G-means clster cls num: {}".format(len(gm_i._gmeans__clusters)))
plt.scatter(x,y, c=z_gm)
plt.grid()
centers = np.array(gm_i._gmeans__centers)
plt.scatter(centers[:,0],centers[:,1],s=250, marker='*',c='red')
plt.show()

# このコードは、X-meansとG-meansという2つのクラスタリングアルゴリズムを使用してデータのクラスタリングと可視化を行います。以下はコードの詳細な説明です：
# embedding_dfから説明変数 x と y を抽出します。また、説明変数全体を表す X も作成します。
# X-meansクラスタリングを実行します。kmeans_plusplus_initializerを使用して初期センターを初期化し、xmeansを使用してクラスタリングを実行します。クラスタ数の上限はkmax=10に設定されています。
# 各データポイントが所属するX-meansのクラスタを z_xm に格納します。
# G-meansクラスタリングを実行します。X-meansと同様に、初期センターを初期化し、gmeansを使用してクラスタリングを実行します。クラスタ数の上限はkmax=10に設定されています。
# 各データポイントが所属するG-meansのクラスタを z_gm に格納します。
# グラフを描画します。最初のプロットは元のデータポイントを表示し、2番目のプロットはX-meansによるクラスタリングの結果を表示します。各クラスタのセンターは赤い星で示されています。最後のプロットはG-meansによるクラスタリングの結果を表示します。同様に、各クラスタのセンターは赤い星で示されています。
# これにより、データがX-meansおよびG-meansによってクラスタリングされ、クラスタごとに異なる色で表示された散布図が生成されます。また、クラスタのセンターも可視化されます。これにより、データの潜在的な構造が視覚的に理解できます。
