from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

month_list     = []
r_list        = []
accuracy_list  = []
precision_list = []
recall_list    = []
f1_list        = []
auc_list       = []

for ym in df.yyyy_mm.unique():
    ## print(ym)
    tmp = df[df['yyyy_mm']==ym]
    
    y_true = tmp["target"].values
    y_pred = tmp["予測結果"].values
    
    month_list.append(ym)
    r_list.append(len(tmp))
    accuracy_list.append(accuracy_score(y_true, y_pred))
    precision_list.append(precision_score(y_true, y_pred))
    recall_list.append(recall_score(y_true, y_pred))
    f1_list.append(f1_score(y_true, y_pred))
    auc_list.append(roc_auc_score(y_true, y_pred))

# pandasのデータフレームにまとめる
df_months = pd.DataFrame({
    'month': month_list,
    'R数': r_list,
    'accuracy': accuracy_list,
    'precision': precision_list,
    'recall': recall_list,
    'f1': f1_list,
    'auc': auc_list
})

df_months

# このPythonコードは、月ごとに異なる評価メトリクス（accuracy、precision、recall、f1-score、およびAUC）を計算し、それらの結果を含むデータフレームを作成します。以下は、コードの説明です：
# month_list、r_list、accuracy_list、precision_list、recall_list、f1_list、auc_listなどの空のリストを初期化します。これらのリストは、各月のメトリクスと月のR数（データ数）を格納します。
# データフレーム（ここではdf）内の一意の年月（yyyy_mm列）を取得します。

# 各月について、以下のステップを実行します：
# yyyy_mmが一致するデータを一時的なデータフレーム（tmp）に抽出します。
# 真のターゲット値（y_true）と予測ターゲット値（y_pred）を取得します。
# 月、R数、および各評価メトリクス（accuracy、precision、recall、f1-score、AUC）をそれぞれのリストに追加します。
# 各月の結果を含むデータフレーム（df_months）を作成します。このデータフレームには、月、R数、および各評価メトリクスの値が含まれています。

# このコードは、異なる月ごとにモデルの評価メトリクスを計算し、月ごとの性能を比較および視覚化するために使用できます。データフレームには、各月の詳細な評価メトリクスが含まれているため、トレンドや変化を分析するのに役立ちます。



# R数（R-value）は、このコードの文脈では「データの数」または「サンプルサイズ」を指します。R数は、データセット内の観測値（データポイント）の総数を表します。
# データ解析や統計処理の際に、サンプルサイズは重要な情報であり、結果の信頼性や有意性を評価する際に考慮されます。
# このコードでは、各月のデータセット内のデータポイントの数をr_listに格納しています。各月のR数は、その月のデータがどれだけ多いかを示す指標として利用されます。
# 月ごとのデータ数を比較することで、異なる月の結果を評価し、傾向や変化を理解するのに役立ちます。
