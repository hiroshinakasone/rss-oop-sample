# rss-oop-sample
RSS加工アプリケーション(CUI)のサンプルリポジトリです

## Install
前提条件: Python3.6インストール済
```bash
$ git clone https://github.com/hiroshinakasone/rss-oop-sample.git
$ cd rss-oop-sample/
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Usage
デフォルト表示
```bash
$ cd src/
$ python3 main.py "http://example.com/feed/1" "http://example.com/feed/2"
```
出力結果
```bash
タイトル: タイトル1
本文: 本文1
公開日時: 日時1

タイトル: タイトル2
本文: 本文2
公開日時: 日時2

タイトル: タイトル3
本文: 本文3
公開日時: 日時3
....
```

タイトルのみ表示
```bash
$ cd src/
$ python3 main.py --title-only "http://example.com/feed/1" "http://example.com/feed/2"
```
出力結果
```bash
タイトル: タイトル1
タイトル: タイトル2
タイトル: タイトル3
.....
```