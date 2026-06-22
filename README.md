# 増養殖環境学実験2026

## はじめに

このリポジトリは、増養殖環境学実験の海洋環境データ分析パートで使用する資料集です。

### 使用するもの

* [`docs/prompt.md`](./docs/prompt.md)  
  AIにプログラムを書いてもらうための**命令書(プロンプト)**
* [`script/`](./script)  
  [`contour.py`](./script/contour.py)：コンター図を描くプログラム
  [`vertical_profile.py`](./script/vertical_profile.py)：鉛直プロファイルを描くプログラム

### 困ったら

各ページ上部の `2026_kankyogaku` をクリックすると、このページに戻れます。

---

以下は開発用ファイルです。授業では使用しません。

```texts
.gitignore
.python-version
pyproject.toml
uv.lock
```


```
.
├── docs
│   └── prompt.md # AIへの命令書
├── script
│   ├── contour.py # コンター図を書くPythonプログラム
│   └── vertical_profile.py # 鉛直プロファイルを書くPythonプログラム
│
├── .gitignore # ↓ここから下は見なくていい↓
├── .python-version
├── README.md 
├── pyproject.toml
└── uv.lock
```