for key, value in model.res.best_params_.items():
    print(f"'{key}': ", value)
    print()
    
# ベストパラメータを保存する   
import json

d = model.res.best_params_
now = filename.replace('xxx', '').replace('.pkl', '')
path = f"./data/best_params_{now}.json"

with open(path, 'w') as f:
    json.dump(d, f)

# このPythonコードは、ベストハイパーパラメータを取得し、それをJSONファイルとして保存する方法を示しています。以下は、コードの詳細な説明です。
# for key, value in model.res.best_params_.items():：model.res.best_params_には、モデルの最適なハイパーパラメータが含まれています。この行では、辞書内の各キー（パラメータ名）とその値を反復処理しています。
# print(f"'{key}': ", value)：反復処理中に、各ハイパーパラメータの名前（キー）とその値を印刷しています。この部分は、ハイパーパラメータの設定を確認するために使用されます。

# ハイパーパラメータの印刷後、ベストパラメータをJSONファイルに保存します。
# d = model.res.best_params_  # ベストパラメータを取得
# now = filename.replace('xxx', '').replace('.pkl', '')  # ファイル名から日付部分を抽出
# path = f"./data/best_params_{now}.json"  # ファイルの保存パスを生成

# with open(path, 'w') as f:
#     json.dump(d, f)  # ベストパラメータをJSONファイルに保存
  
# 上記コードでは、model.res.best_params_からベストパラメータを取得し、ファイル名から日付部分を抽出してベストパラメータを保存するJSONファイルのパスを生成しています。最後に、json.dump()を使用してベストパラメータをJSONファイルに保存します。
# このコードを実行すると、ベストパラメータが印刷され、JSONファイルにも保存されます。
