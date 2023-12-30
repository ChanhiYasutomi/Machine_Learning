# ベストパラメータを呼び出す
import json

now = filename.replace('xxx', '').replace('.pkl', '')
path = f"./data/best_params_{now}.json"

with open(path, 'r') as f:
    d_json = f.read()
    d = json.loads(d_json)
    
print(d)

# このPythonコードは、JSONファイルから保存されたベストパラメータを読み込む方法を示しています。以下は、コードの詳細な説明です。
# now = filename.replace('xxx', '').replace('.pkl', '')：filenameから日付部分を抽出して、対応するベストパラメータのJSONファイルのパスを生成します。このパスは、前のセクションでベストパラメータを保存したファイルのパスと一致する必要があります。
# with open(path, 'r') as f:：生成されたJSONファイルのパスを使用して、ファイルを読み込みモードで開きます。
# d_json = f.read()：ファイルからJSONデータを読み込みます。
# d = json.loads(d_json)：json.loads()関数を使用してJSON文字列をPythonの辞書オブジェクトに変換します。これにより、ベストパラメータがPythonの変数dに読み込まれます。
# print(d)：ベストパラメータを印刷して確認します。

# このコードを実行すると、指定されたJSONファイルからベストパラメータが読み込まれ、d変数に格納されます。その後、ベストパラメータが印刷されます。
