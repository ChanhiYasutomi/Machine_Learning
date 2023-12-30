import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import OneClassSVM
from sklearn.metrics.pairwise import euclidean_distances
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(0)
n_samples = 1000

data = {
    'dr_id': list(range(1, n_samples + 1)),
    'attribute_1': np.random.uniform(0, 1, n_samples),
    'attribute_2': np.random.uniform(0, 1, n_samples),
    'open_rate': np.random.uniform(0, 1, n_samples),
    'click_rate': np.random.uniform(0, 1, n_samples)
}
df = pd.DataFrame(data)

# キーワードAに反応した医師の集める:キーワードAに反応した医師を特定し、興味を持ったユーザーグループを形成します。
# キーワードAに反応した医師を特定
keyword_a_reacted = df[df['open_rate'] > 0.6]
keyword_a_reacted

# ワンクラスSVMによる正常と異常の判定:ワンクラスSVMを用いて、通常の医師群と異常な医師を区別します。モデルは通常のパターンを学習し、それに従って異常なケースを検出します。
# ワンクラスSVMによる正常と異常の判定
svm_model = OneClassSVM()
svm_model.fit(keyword_a_reacted[['attribute_1', 'attribute_2', 'open_rate', 'click_rate']])
predictions = svm_model.predict(keyword_a_reacted[['attribute_1', 'attribute_2', 'open_rate', 'click_rate']])

# 正常の方に注目:ワンクラスSVMの結果を元に、通常の医師グループに注目します。これにより、真に関心のある医師を特定します。
# 正常グループと非反応医師の結合:通常の医師グループと、キーワードAに反応しなかった医師グループを結合します。この一環で、より幅広いターゲットを対象にすることができます。

keyword_a_reacted[predictions == 1]

# 正常の医師グループと非反応医師を結合
normal_group = keyword_a_reacted[predictions == 1]
non_reacted_doctors = df[~df['dr_id'].isin(normal_group['dr_id'])]

# 距離に基づく医師のランキング付け:正常グループから距離の近い医師をランキング付けし、優先度を設定します。これにより、より関心を持ちそうな医師に焦点を当てることが可能です。
# 正常グループとdistanceの近い医師のランキング付け
distances = euclidean_distances(normal_group[['attribute_1', 'attribute_2', 'open_rate', 'click_rate']], non_reacted_doctors[['attribute_1', 'attribute_2', 'open_rate', 'click_rate']])
ranked_doctors = non_reacted_doctors.copy()
ranked_doctors['distance'] = distances.min(axis=0)

# ターゲティング
target_doctor = ranked_doctors.sort_values(by='distance')
print("ターゲット医師情報:")
target_doctor

# 3Dプロット
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(normal_group['attribute_1'], normal_group['attribute_2'], normal_group['open_rate'], c='blue', label='normal_dr')
ax.scatter(non_reacted_doctors['attribute_1'], non_reacted_doctors['attribute_2'], non_reacted_doctors['open_rate'], c='red', label='non_react_dr')
ax.scatter(target_doctor['attribute_1'], target_doctor['attribute_2'], target_doctor['open_rate'], c='green', label='target_dr')
ax.set_xlabel('attribute_1')
ax.set_ylabel('attribute_2')
ax.set_zlabel('open_rate')
ax.legend()
plt.show()
