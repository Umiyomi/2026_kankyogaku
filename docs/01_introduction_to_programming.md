# Pythonでプログラミング入門
Google Colabでプログラミング言語 "Python" を動かしながら、基本的な概念を導入します。
コードをColabのセルにコピペして、実行してみましょう。  
壊れたりしないので、色々弄ってとにかく試してみましょう。

## まずはやってみる
```
print("hello!!")
print("こんにちは")
print(100)
```
print()は文字や数値を画面に出力する関数です。
プログラムは上から順番に実行されます。
これでプログラミングに入門しました。

## 変数
```
a = "hello"
b = "こんにちは"
c = 100

print(a)
print(b)
print(a)
print(a)
print(c)
```
"変数名 = 中身" という記法で、値を変数に代入し、利用することができます。

## 数値の演算
```
a = 100 - 50
b = 200

print(a+b)

c = a * b

print(c)
```
数値を演算したり、その結果を変数に代入したりすることができます。

## 関数
```
# 足し算関数を定義する
def tashizan(a, b):
    result = a + b
    return result

# 変数a, bを受け取り、足し算し、result変数に代入してreturn(関数の結果を返す)します

# 定義したtashizan関数を呼び出す

answer1 = tashizan(100, 200)
print(answer1)

answer2 = tashizan(a=1000, b=40)
print(answer2)


# 引き算関数も定義してみる
def hikizan(a, b)
    result = a - b
    return result

# 定義したhikizan関数を呼び出し、その返り値をanswer3変数に代入する
answer3 = hikizan(a=500, b=300)
print(answer3)
```
関数を定義(definition)することで、定義した動作を繰り返し呼び出すことができます。
適切な関数名、変数名を名付けすることで処理の流れが見えやすくなります。

---

ここまでに、プログラミングの基本である
- 値の表示(print)
- 変数の定義(a=100, b=200)
- 演算(a+b)
- 関数の定義(def a+b)
を学びました。

次は、実際のデータを使いながら、表データの読み込み、処理を学びます。

