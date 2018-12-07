# responder-todo
responderを使って簡易的なtodoアプリ

# install
まず最初にstarletteとresponderのインストールが必要です

```
$ pip install starlette==0.8.0
$ pip install responder
```

# create model
以下のコマンドで同ディレクトリ上にdb.sqlite3というファイルが作成されます。

```
$ python models.py
```

# run
以下のコマンドで動作します。

```
$ python app.py
```


# usage
todoリストの作成

```
curl http://127.0.0.1:5000/api/todo -X POST -H "Content-Type: application/json" -d '{"name": "value", "text": "test"}'
```


以下に解説記事を載せました。
[Pythonで話題のWEBフレームワークresponderでサンプルのtodoリストを作成](https://note.mu/shimakaze_soft/n/ne47bc123dc83)
