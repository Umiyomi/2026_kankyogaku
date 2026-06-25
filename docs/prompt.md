# CTDデータから鉛直プロファイルとコンターを作図し海洋観測結果を可視化する
---
## データの概要
- 1日目、2日目、マガキ調査の3種類のサンプリングを実施
- 1日目、2日目は各3ファイルのcsv
- マガキ調査は6ファイルのcsv
- 1ファイルが1サンプリングステーションに対応

```
PROJECT_ROOT = /content/drive/MyDrive/kankyogaku2026
MAGAKI_DATA_DIR = {PROJECT_ROOT}/data/magaki


MAGAKI_DATA = {
    St1: /magaki/0621090317_AAQ177_SNo0636.csv
    St2: /magaki/0621090953_AAQ177_SNo0636.csv"
    St3: /magaki/0621092021_AAQ177_SNo0636.csv"
    St4: /magaki/0621092708_AAQ177_SNo0636.csv"
    St5: /magaki/0621094533_AAQ177_SNo0636.csv"
    St6: /magaki/0621095111_AAQ177_SNo0636.csv"
}
```

## データ様式
- csvファイル
- encoding='shift-jis'
- "[Item]"と書かれた行の1行下にヘッダ行
- カラム構成は

```
深度 [m],水温 [℃],塩分,電導度 [mS/cm],EC25 [μS/cm],密度 [kg/m3],シグマＴ,Chl-Flu. [ppb],Chl-a [μg/l],濁度 [FTU],pH,ORP [mV],DO [%],Weiss-DO [mg/l],光量子 [μmol/(m2*s)],G&G-DO [mg/l],B&K-DO [mg/l],
```

---

## スクリプト要件定義
### 概要
csvファイルを読み込み、鉛直プロファイルとコンターの作図を行う。スクリプトは別々に作成する。データの前処理部分は共通化する。csvファイルは複数存在し、その対応関係は手動で定義する。

### データの読み込み
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

---

### 作図の要件
#### 共通要件
- 図は水温、塩分等、測定項目毎に分ける(temp_fig, sal_fig, chl_fig)
- depthmax, vmin, vmaxは引数化し手動で調整できるようにする
- タイトル、保存先も引数化する
- figの保存名とタイトルは以下のフォーマット
```
{temp}_{day1}_{profile}
{sal}_{day2}_{contour}
```

#### 鉛直プロファイル
- y軸を水深、x軸を観測値(水温、塩分等)
- ステーションを色分けする(st1:red, st2:blue, st3:green, ...)
#### コンター
- y軸を水深、x軸をステーション座標


### 関数の分割
- 単一ファイルの前処理関数
- ステーションデータ結合関数
- 作図&保存の関数  
の3関数で構成、main関数にパイプラインを書く  
スクリプトは1枚の.pyで完結する

