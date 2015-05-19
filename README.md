Bitly
====

短縮URLサービスを短いコードで書く練習。

## Requirement
Python 2系

## Usage
以下のコマンドでサーバを起動する。

```
python main.py
```

`POST` で短縮URLを登録すると、短縮URLが返ってくる。

```
$ curl localhost:8080 -X POST -H "Content-Type:text/plain" -d "http://www.google.co.jp"
http://localhost:8080/b2f9a84f3
```

このURLにブラウザからアクセスすると、登録したURLにリダイレクトされる。

## Author
[shibataka000](https://github.com/shibataka000)
