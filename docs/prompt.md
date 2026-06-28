# CTDデータから鉛直プロファイルとコンターを作図し海洋観測結果を可視化する
---
## データの概要
- 1日目、2日目、マガキ調査の3種類のサンプリングを実施
- 1日目、2日目は各3ファイルのcsv
- マガキ調査は6ファイルのcsv
- 1ファイルが1サンプリングステーションに対応

```python
PROJECT_ROOT = "/content/drive/MyDrive/kankyogaku2026"
WAKASA_DATA_DIR = f"{PROJECT_ROOT}/data/wakasa"
MAGAKI_DATA_DIR = f"{PROJECT_ROOT}/data/magaki"

# wakasa data
WAKASA_ST1_PATH = f"{WAKASA_DATA_DIR}/202606241429_ASTD152-ALC-R02_0184_142943.Csv"
WAKASA_ST2_PATH = f"{WAKASA_DATA_DIR}/202606241417_ASTD152-ALC-R02_0184_141756.Csv"
WAKASA_ST3_PATH = f"{WAKASA_DATA_DIR}/202606241356_ASTD152-ALC-R02_0184_135631.Csv"
WAKASA_ST4_PATH = f"{WAKASA_DATA_DIR}/202606241340_ASTD152-ALC-R02_0184_134017.Csv"

# magaki data
MAGAKI_ST1_PATH = f"{MAGAKI_DATA_DIR}/0621090317_AAQ177_SNo0636.csv"
MAGAKI_ST2_PATH = f"{MAGAKI_DATA_DIR}/0621090953_AAQ177_SNo0636.csv"
MAGAKI_ST3_PATH = f"{MAGAKI_DATA_DIR}/0621092021_AAQ177_SNo0636.csv"
MAGAKI_ST4_PATH = f"{MAGAKI_DATA_DIR}/0621092708_AAQ177_SNo0636.csv"
MAGAKI_ST5_PATH = f"{MAGAKI_DATA_DIR}/0621094533_AAQ177_SNo0636.csv"
MAGAKI_ST6_PATH = f"{MAGAKI_DATA_DIR}/0621095111_AAQ177_SNo0636.csv"
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
- 使うカラムは[0, 1, 2, 8]
- ヘッダ行までスキップしてカラム名は新たに設定
```
["depth(m)", "temp(℃)", "sal", "chl-a(μg/l)"]
```


### 出力
```
/content/drive/MyDrive/kankyogaku2026/outputs
```

---

### 作図の要件
#### 共通要件
- 図は水温、塩分等、測定項目毎に分ける(temp_fig, sal_fig, chl_fig)
- depthmax, vmin, vmaxは引数化し手動で調整できるようにする(settings_dictとしてコード上部に定数としてまとめる)
- タイトル、保存先も引数化する
- figの保存名とタイトルは以下のフォーマット
```
{temp}_{day1}_{profile}
{sal}_{day2}_{contour}
```

#### 鉛直プロファイル
- y軸を水深、x軸を観測値(水温、塩分、クロロフィル)
- ステーションを色分けする(st1:red, st2:blue, st3:green, ...)
#### コンター
- y軸を水深、x軸をステーション番号


### 関数の分割
- 単一ファイルの前処理関数
- ステーションデータ結合関数
- 作図&保存の関数  
の3関数で構成、main関数にパイプラインを書く  
スクリプトは1枚の.pyで完結する

