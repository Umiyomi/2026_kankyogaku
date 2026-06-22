# 増養殖環境学実験2026

## このページについて

このリポジトリは、増養殖環境学実験の海洋環境データ分析パートで使用する資料集です。

本日の実習では、

1. Google Colab を開く
2. AIにプログラムを書いてもらう
3. 海洋観測データを可視化する

という流れで進めます。

---

## 今日使うもの

### Google Colab

プログラムを作成・実行するサイトです。

https://colab.research.google.com/

### AIへの命令書

`docs/prompt.md`

AIにどのような指示を出せばよいかを書いてあります。

### 完成例

`script/`

* `contour.py`

  * コンター図を描くプログラム
* `vertical_profile.py`

  * 鉛直プロファイルを描くプログラム

---

## 実習の流れ

### Step 1

Google Colab を開く

### Step 2

配布された観測データをアップロードする

### Step 3

`docs/prompt.md` の内容をAIに入力する

### Step 4

作成されたプログラムを実行する

### Step 5

グラフを確認し、結果を考察する

---

## ファイルのコピー方法

各ファイル名をクリックすると内容を閲覧できます。

右上の「Copy raw file」を押すと内容をコピーできます。

---

## このサイトの構造

```text
.
├── docs
│   └── prompt.md
├── script
│   ├── contour.py
│   └── vertical_profile.py
│
│ # ↓ここから下のファイルは使わない↓
├── .gitignore
├── .python-version
├── README.md
├── pyproject.toml
└── uv.lock
```

※ `.gitignore` や `pyproject.toml` などのファイルは授業では使用しません。
