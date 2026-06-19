# CTDデータから鉛直プロファイルとコンターを作図し海洋観測結果を可視化する

## データ様式
- csvファイル
- encoding='shift-jis'
- "[Item]"と書かれた行の1行下にヘッダ行
- カラム構成は

```
深度 [m],水温 [℃],塩分,電導度 [mS/cm],EC25 [μS/cm],密度 [kg/m3],シグマＴ,Chl-Flu. [ppb],Chl-a [μg/l],濁度 [FTU],pH,ORP [mV],DO [%],Weiss-DO [mg/l],光量子 [μmol/(m2*s)],G&G-DO [mg/l],B&K-DO [mg/l],
```

## データの概要
- 1日目、2日目、マガキ調査の3種類のサンプリングを実施
- 1日目、2日目は各3ファイルのcsv
- マガキ調査は6ファイルのcsv


## 要件定義
### 概要
csvファイルを読み込み、鉛直プロファイルとコンターの作図を行う。スクリプトは別々に作成する。データの前処理部分は共通化する。csvファイルは複数存在し、その対応関係は手動で定義する。

### データの読み込み
- csvをpandasのDataframeで扱う
- 使うカラムは[0, 1, 2, 8, 9, 12]
- ヘッダ行までスキップしてカラム名は新たに設定
```
["depth(m)", "temp(℃)", "sal", "chl-a(μg/l)", "turb(FTU)", "DO(%)"]
```

### 入力
```
/content/drive/MyDrive/test2026kankyogaku/data/*.csv
```
### 出力
```
/content/drive/MyDrive/test2026kankyogaku/outputs
```

### 