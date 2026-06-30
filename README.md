# 増養殖環境学実験2026

## このページについて

このページは、増養殖環境学実験の海洋環境データ分析パートで使用する資料集です。

本日の実習は、

1. Google Drive の`マイドライブ`に観測データをアップロードする
2. Google Colab に`ノートブック`を作成する
3. プログラムをコピペ・実行しながらデータサイエンスの基礎を学ぶ
4. 海洋観測データを可視化する

という流れで進めます。

---

## 資料

### Google Drive
観測データをアップロードします
https://drive.google.com

### Google Colab
プログラムを作成・実行するサイトです。
https://colab.research.google.com/

### テキスト
本講義で使うテキストです  
コピペ可能なプログラムが付属します  
[`introduction_to_programming.md`](./docs/introduction_to_programming.md)  
[`load_data_and_draw_graph.md`](./docs/load_data_and_draw_graph.md)  
[`prompt.md`](./docs/prompt.md)  


### プログラム完成例

[`contour.py`](./script/contour.py)  
コンター図を描くプログラム  

[`vertical_profile.py`](./script/vertical_profile.py)
鉛直プロファイルを描くプログラム

### AIへの指示書の例

[`prompt.md`](./docs/prompt.md)
AIにプログラムを書かせる際の命令(プロンプト)の例です。
プログラム完成例に近いコードを出力させるための全ての情報が記載されています。

---

## Google Colab について
Google Colab はWebブラウザ上で動作するPython実行環境です(以下、Colab)。   
**Colab においてプログラムを記述、実行、保存するページを`ノートブック` と呼びます。**  
ノートブックは作成すると自動でGoogleドライブに保存されます。  
ノートブックは`*.ipynb`という拡張子で保存されます。  
(*部分にはファイル名、デフォルトではUntitled0.ipynb)

### ドライブへの接続
Colab で使用するデータは`Google Drive`にアップロードしておく必要があります。
**Colab はパソコン内に保存されたローカルデータに直接アクセスすることはできません**
ColabとDriveの紐付けは`ノートブック`毎に行われます。  
ノートブックを開くと、画面左側に`フォルダ`のアイコン🗂️があります。  
フォルダアイコンをクリックすると、`ドライブをマウント`というボタンがあります。  
ボタンをクリックすると`Googleドライブをマウントするには、このセルを実行してください`という指示が出るので実行する。  
実行すると、ノートブックにGoogleドライブが紐付けられます。  
**この作業はノートブックを作成したり開き直したりする度に実行する必要があります。**


### 手順まとめ
- ログインする
- `ノートブックを新規作成` ボタンをクリック
- ノートブック画面上部の`Untitled0.ipynb`と書かれた所でファイル名を変更
- フォルダマークをクリックしてファイルメニューを開き`ドライブをマウント`する
- しばらく待つとノートブックからドライブを参照できるようになる
- 二回目以降のログイン時は`ノートブックを開く`画面で過去に作成した`ノートブック.ipynb`を開く
  ("最近"に無いときは"Googleドライブ"の方を見てみる)

---


## このページの構造

```text
.
├── docs
│   ├── 01_introduction_to_programming.md
│   ├── 02_introduction_to_data_processing.md
│   ├── 03_introducting_draw_graph.md
│   ├── 04_requirements_definition.md
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

