Bitly
====

短縮URLサービスを短いコードで書く練習。

## Requirement
- Python 2系
- [redis-server](http://redis.io/)
- [redis-py](https://redis-py.readthedocs.org/)

## Usage
以下のコマンドでサーバを起動する。

```
$ redis-server
$ python main.py
```

`POST` で短縮URLを登録すると、短縮URLが返ってくる。

```
$ curl localhost:8080 -X POST -H "Content-Type:text/plain" -d "http://www.google.co.jp"
http://localhost:8080/b2f9a84f3
```

このURLにブラウザからアクセスすると、登録したURLにリダイレクトされる。

## Install
```
$ sudo apt-get install redis-server
$ pip install redis
```

## Author
[shibataka000](https://github.com/shibataka000)
