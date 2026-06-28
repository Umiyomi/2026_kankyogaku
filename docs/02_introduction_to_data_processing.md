# 02 データ読み込み
ここからは実際の観測データを触りながら、プログラミングでデータ処理を行うための視点を導入します。

---

## データはどこにある？
今回はGoogle Colabでプログラミングを行うため、Google Drive上のフォルダにデータをアップロードしました。  
プログラミングではフォルダのことを**ディレクトリ**と呼びます。
データがどこにあるかは**ディレクトリパス**で表現します。
```
wakasa_st1 = "/content/drive/MyDrive/kankyogaku2026/data/20260624/202606241429_ASTD152-ALC-R02_0184_142943.Csv"
```
プログラムにデータの在処を伝えるためには、ディレクトリパスを使います。
ディレクトリパスを変数に代入しておきましょう。


## 表データ処理ライブラリ"Pandas"
Pythonには表データの読み込みや図を作成など、多くの人が使う機能があらかじめライブラリとしてまとめられています。表データを処理するための代表的なライブラリとして**Pandas**があります。
```
# pandasをコードセル内で呼び出す
import pandas as pd
from io import StringIO

# テストデータ
csv_text = """
depth,temp,sal
0,25.1,33.4
1,24.8,33.5
2,24.3,33.6
"""

dataframe = pd.read_csv(StringIO(csv_text))
print(dataframe)

```
---

## Pandasで実際のデータを読み込んでみる
先ほどはコード内で定義したテストデータを読み込みました。
今度はGoogle Driveにアップした実際の観測データをプログラムで読み込んでみましょう。
```
import pandas as pd

wakasa_st1 = "/content/drive/MyDrive/kankyogaku2026/data/20260624/202606241429_ASTD152-ALC-R02_0184_142943.Csv"

df = pd.read_csv(wakasa_st1)
print(df)
```
エラーが出てしまいますね。
```
ParserError: Error tokenizing data. C error: Expected 1 fields in line 4, saw 2
```
これは”CSVの列数が行によって揃っていない”ときに出るエラーです。  
どういうことか、元のデータファイルを見てみましょう。
```
// AAQ-RINKO Series Data Processing Software
// Version 1.12
// File Date:2026/06/21 10:32:51
// Copyright (C) JFE Advantech Co., Ltd.

~中略~

[Item]
深度 [m],水温 [℃],塩分,電導度 [mS/cm],EC25 [μS/cm],密度 [kg/m3],シグマＴ,Chl-Flu. [ppb],Chl-a [μg/l],濁度 [FTU],pH,ORP [mV],DO [%],Weiss-DO [mg/l],光量子 [μmol/(m2*s)],G&G-DO [mg/l],B&K-DO [mg/l],
0.000,24.284,30.405,46.152,46890.3,1020.085,20.085,1.204,1.204,1.334,6.061,167.930,96.321,6.752,519.690,6.771,6.772,
0.100,24.287,30.404,46.152,46887.6,1020.083,20.082,1.249,1.249,1.364,6.062,167.968,96.186,6.745,606.444,6.764,6.764,
0.200,24.278,30.420,46.166,46911.2,1020.098,20.097,1.219,1.219,1.394,6.062,168.006,96.220,6.747,679.274,6.765,6.766,
```  
観測データのファイルの先頭には観測機器の情報などが入っています。
表データとして行と列が揃っているのは、**[Item]** と書かれた行から下ですね。  
このままではCSVデータとして扱えず、エラーを起こしてしまいます。
そのため、[Item]より上の行を**スキップして**読み込みます。  

---

## データをスキップして読み込む
(複雑な構文なので、覚えなくていいです。そういう発想、機能があるんだなぁと思ってください。)

```
# [Item]という文字列が出現する行番号numを得て、skiprows変数に格納する
skiprows = None
with open(wakasa_st1, 'r', encoding='shift-jis') as f:
    for num, line in enumerate(f):
        if "[Item]" in line:
            skiprows = num

if skiprows is None:
    raise ValueError(f"[Item] 行が見つかりません: {wakasa_st1}")

# skiprows引数にskiprows+1を与えて[Item]の直後からをcsvデータとして読み込む
df = pd.read_csv(
    wakasa_st1, skiprows=skiprows + 1 , encoding='shift-jis')
print(df)
```
実際の観測データをプログラムで読み込むことができました。
このように、観測データはそのまま扱えるとは限りません。
元のファイルの形式などをよく観察する必要があるのです。

---

最後に、データ読み込みの流れを関数にまとめておきましょう。
```
def load_data(csv_file_path):

    skiprows = None
    with open(csv_file_path, 'r', encoding='shift-jis') as f:
        for num, line in enumerate(f):
            if "[Item]" in line:
                skiprows = num

    if skiprows is None:
        raise ValueError(f"[Item] 行が見つかりません: {csv_file_path}")

    df = pd.read_csv(
        csv_file_path, skiprows=skiprows + 1, encoding="shift-jis",
        header=None)

    return df
```

これで他のステーションのデータも簡単に読み込めます
```
wakasa_st2 = "/content/drive/MyDrive/kankyogaku2026/data/20260624/202606241417_ASTD152-ALC-R02_0184_141756.Csv"

df2 = load_data(wakasa_st2)
print(df2)
```

---

## まとめ

ここまでで、

* **ディレクトリパス**を使って、Google Drive上の観測データの場所をプログラムに伝える
* **Pandas** を使って、CSVファイルを `DataFrame` として読み込む
* 実際の観測データは、そのままでは読めないことがある
* その場合は、**元のファイルを観察して、どこからが表データなのかを見極める**必要がある
* 同じ読み込み処理は、`def load_data()` のように**関数にまとめて再利用**できる

ということを体験しました。

今回のCTDデータでは、ファイルの先頭に観測機器の情報が入っていたため、`pd.read_csv()` をそのまま使うとエラーになりました。
そこで、`[Item]` という行を手がかりにして、その下だけをCSVデータとして読み込むようにしました。

つまり、データ処理では「とりあえずコードを書く」のではなく、まず**元のデータファイルを観察し、どの部分が表データとして使えるのかを確かめる**ことが大切です。

---

ここまでで、観測データを `DataFrame` としてプログラムに読み込めるようになりました。
次は、この `DataFrame` の列を使って、**水深と水温の関係を図にする**ことを考えます。

次は、

* `DataFrame` の列を使ってグラフを描く
* 水深を縦軸にした図を作る
* 作図の処理を `def plot_profile()` のような関数にまとめる

という流れで、**「読み込んだデータを可視化する」** ところまで進みます。
