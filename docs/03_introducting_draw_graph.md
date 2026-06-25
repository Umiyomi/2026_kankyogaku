# 作図してみる

ここからは、Pythonで**グラフを描く**方法を体験します。
前の資料では、CSVファイルを読み込み、PandasのDataFrameとして扱うところまで進みました。

今回はその続きとして、**DataFrameに入った観測値を図にする**ための基本を導入します。
最終的には、簡単な作図処理を `def` で関数にまとめます。

---

# Pythonで図を描くには

Pythonには、グラフや図を描くためのライブラリがあります。
代表的なものが **Matplotlib** です。

まずは、Matplotlibを使うための準備をします。

```python
import matplotlib.pyplot as plt
```

`matplotlib.pyplot` には、折れ線グラフや散布図などを描くための機能がまとまっています。
`plt` という短い名前を付けて使うのが一般的です。

---

# まずは点を描いてみる

最初に、データを直接書いて散布図を作ってみます。

```python
import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [25.1, 24.8, 24.3, 23.9]

plt.scatter(x, y)
plt.show()
```

これで、`x` と `y` の組を点として描くことができます。

* `plt.scatter(x, y)` : 散布図を描く
* `plt.show()` : 図を表示する


---

# DataFrameの列を使って図を描く

ここから、前回と同じようにPandasのDataFrameを使います。
まずは、整ったテストデータをDataFrameとして読み込みます。

```python
import pandas as pd
from io import StringIO

csv_text = """
depth,temp,sal
0,25.1,33.4
1,24.8,33.5
2,24.3,33.6
3,23.9,33.7
""".strip()

df = pd.read_csv(StringIO(csv_text))
print(df)
```

この `df` には、`depth`, `temp`, `sal` という列があります。
DataFrameの列をそのままグラフに渡すこともできます。

```python
import matplotlib.pyplot as plt

plt.scatter(df["temp"], df["depth"])

# ラベルやタイトルも設定できる
plt.xlabel("temperature (℃)")
plt.ylabel("depth (m)")
plt.title("temperature profile")

plt.show()
```

ここでは、

* 横軸に `df["temp"]`
* 縦軸に `df["depth"]`

を使っています。

つまり、**DataFrameの列を指定するだけで、観測値を図にできる**わけです。

---

# 塩分でも描いてみる

今度は、水温ではなく塩分の列を使ってみます。

```python
import matplotlib.pyplot as plt

plt.scatter(df["sal"], df["depth"])
plt.xlabel("salinity")
plt.ylabel("depth (m)")
plt.title("salinity profile")
plt.show()
```

ここで変わったのは、主に

* 横軸に使う列
* 軸ラベル
* タイトル

です。

つまり、**同じ形のコードでも、使う列を変えるだけで別の図が作れる**ことが分かります。


---

# 作図処理を関数にまとめる

ここまでで、散布図を描くときに毎回似たようなコードを書くことが分かってきたと思います。
たとえば、

* 横軸に何の列を使うか
* 縦軸に何の列を使うか
* タイトルを何にするか

は変わりますが、**作図の流れそのものはほぼ同じ**です。

そこで、作図処理を関数にまとめます。

```python
import matplotlib.pyplot as plt

def plot_profile(df, x_col, y_col, title, xlabel):
    plt.scatter(df[x_col], df[y_col])
    plt.xlabel(xlabel)
    plt.ylabel(y_col)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.show()
```

この関数は、

* `df` : 作図したいDataFrame
* `x_col` : 横軸に使う列名
* `y_col` : 縦軸に使う列名
* `title` : 図のタイトル
* `xlabel` : 横軸ラベル

を引数として受け取ります。

---

# 関数を呼び出してみる

まず、水温プロファイルを描いてみます。

```python
plot_profile(
    df=df,
    x_col="temp",
    y_col="depth",
    title="temperature profile",
    xlabel="temperature (℃)"
)
```

もし `df` に `sal` 列があれば、塩分プロファイルにも同じ関数を使えます。

```python
plot_profile(
    df=df,
    x_col="sal",
    y_col="depth",
    title="salinity profile",
    xlabel="salinity"
)
```

つまりこの関数は、**「どの列を横軸にするか」を変えるだけで、別の変数の図にも使い回せる**ようになっています。

---

# 作図関数の役割を整理する

今回作った `plot_profile()` 関数は、次の仕事をまとめています。

1. DataFrameから指定した列を取り出す
2. 散布図を描く
3. 軸ラベルを付ける
4. タイトルを付ける
5. 水深が上から下へ深くなるように、縦軸を反転する
6. 図を表示する

つまり、**「プロファイル図を描く」という作業をひとまとまりの処理にした**のが、この関数です。

---

# ここまででできるようになったこと

ここまでで、次のことを体験しました。

* Matplotlibで散布図・折れ線グラフを描く
* 軸ラベルやタイトルを付ける
* DataFrameの列を指定して作図する
* 水深軸を反転して、海のデータらしい向きにする
* ステーションごとに色分けして重ね描きする
* 作図処理を `def` で関数にまとめる

---

# まとめ

今回は、Pythonで図を描くための基本として、Matplotlibを使った作図を体験しました。

特に重要なのは、**DataFrameの列を指定して図を描く**という考え方です。
観測データがDataFrameとして読めていれば、その中の列を使ってグラフを作ることができます。

また、同じような作図コードは、`def` で関数にまとめることで再利用しやすくなります。
実際のデータ解析では、

* データを読み込む関数
* データを整形する関数
* 図を描く関数

を組み合わせて処理を進めていきます。

次の資料では、ここまでの

* 変数
* 関数
* CSVの読み込み
* DataFrame
* 作図

を踏まえて、**実際のCTDデータをどう処理し、どのような図を出力したいのか**を要件として整理していきます。
