# 実際のデータを読み込み、グラフを書いてみる
ここからは実際の観測データを触りながら、プログラミングでデータ処理を行うための視座を導入します

---

## プログラムにデータを渡そう
今回はGoogle Colabでプログラミングを行うため、Google Drive上のフォルダにデータをアップロードしました。  
プログラミングではフォルダのことを**ディレクトリ**と呼びます。
データがどこにあるかは**ディレクトリパス**で表現します。
```Python
PROJECT_ROOT = "/content/drive/MyDrive/kankyogaku2026"

wakasa_st1 = f"{PROJECT_ROOT}/data/wakasa/20260624/202606241429_ASTD152-ALC-R02_0184_142943.Csv"
```
プログラムにデータの在処を伝えるためには、ディレクトリパスを使います。
ディレクトリパスを`wakasa_st1`変数に代入しておきましょう。

---

## Pythonの表データ処理機能"Pandas"
Pythonで表データを処理するために**Pandas**という機能があります。    
**Pandas**はコード内で`import`して使用します。

```Python
# Pandasのテストコード

# pandasをimport
import pandas as pd

# df は DataFrameの略
test_df = pd.DataFrame({
    "depth": [0, 1, 2],
    "temp": [26, 25, 24],
    "sal": [32, 33, 34],
    "chl": [1, 2, 3]
})

print(test_data)

```
Pandasは`DataFrame`という表データを扱うことができます。  
また、 **読み込んだCSVファイルをDataFrameに変換**することができます。  
ここで、先ほど`wakasa_st1`変数に代入したデータを読み込んでみます。  


```Python
# Pandasをimport
import pandas as pd

# データのパスを定義
PROJECT_ROOT = "/content/drive/MyDrive/kankyogaku2026"
wakasa_st1 = f"{PROJECT_ROOT}/data/wakasa/20260624/202606241429_ASTD152-ALC-R02_0184_142943.Csv"

# データ読み込みのメイン処理
def load_csv_data():
    
    skiprows = get_skip_rows(wakasa_st1) # <-ここでサブ処理を呼び出している
    # Pandasのread_csv関数にデータパスを渡している
    df = pd.read_csv(wakasa_st1, skiprows=skiprows, encoding='shift-jis')
    print(df.head(10))


# csvファイルの不要な行をskipするためのサブ処理
def get_skip_rows(csv_file_path):
    skiprows = None
    with open(csv_file_path, 'r', encoding='shift-jis') as f:
        for num, line in enumerate(f):
            if "[Item]" in line:
                skiprows = num

    if skiprows is None:
        raise ValueError(f"[Item] 行が見つかりません: {csv_file_path}")
    
    return skiprows + 1

# この行でメイン処理が実行されている
load_csv_data()
```
Pandasの`read_csv`関数は**行と列の数が揃ったCSVデータを与えないとエラーを起こしてしまいます。**  
今回のデータはファイルの上部に非CSVデータ行が存在するため、`get_skip_rows`関数を組み合わせてエラーを回避しました。  
このように、**観測データを読み込む際には不要行のスキップなどの前処理が必要な場合があります。**  
どのような前処理が必要かは実際のデータの性質や目的によって異なるので、一般化しにくいです。  
そのため、AI時代においても人間のデータ観察力・目的意識が試されるところです。  

---

## Pythonの作図機能"Matplotlib"
ここからは先ほど読み込んだデータをグラフとして可視化していきます。
Pythonでグラフを描画するために**Matplotlib**という機能があります。
**Matplotlib**もPandasと同様に`import`して使います。
まずは**x軸, y軸を持つ散布図(scatter graph)にテストデータをプロット**してみましょう。

```Python
# 機能をimport
import pandas as pd
import matplotlib.pyplot as plt

# pandasのDataFrameで作図用のテストデータを定義
test_df = pd.DataFrame({
    "depth": [0, 1, 2],
    "temp": [26, 25, 24],
    "sal": [32, 33, 34],
    "chl": [1, 2, 3]
})

# x軸を温度(temp)とする
x = test_df["temp"]
# y軸を水深(depth)とする
y = test_df["depth"]

# matplotlibのscatter関数にx,yを与える
plt.scatter(x, y)
# show関数で表示
plt.show()

```
