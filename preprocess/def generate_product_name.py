import string
import random

def generate_product_name(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for character in range(length))

# 100個の商品名を生成
product_names = [generate_product_name() for character in range(100)]

# 生成した商品名を表示
for i, name in enumerate(product_names, start=1):
    print(f"Product {i}: {name}")

# このコードは、指定された長さのランダムな英字と数字の組み合わせからなる商品名を生成し、その生成された商品名をリストに格納して表示するものです。以下に各部分の説明を示します：
# generate_product_name 関数：指定された長さ（デフォルトは6）のランダムな英字と数字の組み合わせからなる文字列を生成する関数です。string.ascii_letters はアルファベット（大文字と小文字の両方）を、string.digits は数字を表します。
# random.choice を使用してランダムな文字を選択し、for ループで指定された長さ分の文字列を生成します。
# product_names リスト：generate_product_name() を100回呼び出して生成された商品名を格納するためのリストです。リスト内包表記を使用して簡潔に書かれています。

# リスト内の商品名を enumerate を使用してループし、f-string を使って商品名を表示しています。enumerate はインデックスとリストの要素を同時に取得するための便利な関数です。
# 最終的に、100個の商品名が生成され、それぞれが "Product 1: [商品名]", "Product 2: [商品名]", ... といった形で表示されます。ランダムに生成された商品名がリストに格納され、それが表示されていることが確認できます。
