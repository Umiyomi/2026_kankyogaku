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
[`01_introduction_to_programming.md`](./docs/01_introduction_to_programming.md)
[`02_introduction_to_data_processing.md`](./docs/02_introduction_to_data_processing.md)
[`03_introducting_draw_graph.md`](./docs/03_introducting_draw_graph.md)
[`04_requirements_definition.md`](./docs/04_requirements_definition.md)


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

