import

from collections import Counter
import gc
import random
import time
import pickle

import lightgbm as lgb
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

%matplotlib inline
plt.rcParams['font.family'] = "IPAexGothic"
print("現在使用しているフォント", matplotlib.rcParams['font.family'])

color_black = (76/255, 73/255, 72/255)
color0 = (18/255, 179/255, 199/255)
color1 = (62/255, 150/255, 210/255)
color2 = (20/255, 167/255, 157/255)
color3 = (173/255, 211/255, 97/255)
color4 = (232/255, 173/255, 95/255)
color5 = (215/255, 76/255, 119/255)
color6 = (139/255, 124/255, 186/255)

from sklearn.metrics import auc, accuracy_score, roc_curve, confusion_matrix, roc_auc_score
# from sklearn.model_selection import GridSearchCV
import optuna
from optuna.integration import OptunaSearchCV
from sklearn.utils import resample
import torch
from torch.utils.data import random_split
gc.enable()

# 提供されたコードは、Pythonで機械学習モデルのトレーニングと評価を行うためのセットアップを含んでいます。以下は、このコードの主要な要素について説明します：

# ライブラリのインポート:
# collections: Pythonの標準ライブラリからCounterクラスをインポートします。Counterクラスは、要素の出現回数を数えるために使用されます。
# gc: ガベージコレクションのライブラリです。メモリ管理に関連する操作を行うために使用されます。
# random: 乱数生成を行うためのライブラリです。
# time: 時間に関連する操作を行うためのライブラリです。
# pickle: ピクルス（シリアライズ）およびデシリアライズ（逆シリアライズ）をサポートするライブラリです。
# lightgbm: LightGBMという勾配ブースティングフレームワークのラッパーライブラリです。Gradient Boosting Machine（GBM）モデルをトレーニングおよび評価するために使用されます。
# numpy: 数値計算ライブラリです。多次元配列を操作し、数学的な演算を行うために使用されます。
# pandas: データ操作および解析のためのライブラリです。データフレームの操作に使用されます。
# matplotlib: データの可視化ライブラリです。グラフの描画に使用されます。
# sklearn: Scikit-learnとしても知られる、機械学習のためのライブラリです。モデル評価やハイパーパラメータチューニングのために使用されます。
# optuna: ハイパーパラメータチューニングライブラリです。オプティマイゼーションフレームワークを提供します。
# torch: PyTorchとしても知られる、深層学習ライブラリです。ニューラルネットワークモデルを定義およびトレーニングするために使用されます。

# フォント設定:
# Matplotlibで使用するフォントを設定しています。日本語フォント "IPAexGothic" が設定されています。

# カラーパレットの設定:
# グラフやプロットで使用されるカラーを定義しています。

# Scikit-learn関連のインポート:
# Scikit-learnからさまざまな評価メトリクス、モデル選択、リサンプリング、混同行列などの関数やクラスがインポートされています。
# ガベージコレクションの有効化:

# gc.enable() を呼び出してガベージコレクションを有効にしています。これは不要なメモリの解放を助けるために使用されます。
# このコードは、機械学習プロジェクトのスクリプトのセットアップ段階で使用され、データの前処理、モデルのトレーニング、評価、ハイパーパラメータのチューニングなどのタスクに関連するライブラリと設定を含んでいます。モデルの詳細なトレーニングと評価の手順は、このコードの後に続くでしょう。
