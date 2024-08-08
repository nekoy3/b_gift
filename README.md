# b_gift_discord
 ベテルギフト( https://beterugift.jp/ )のギフト券出品状況をdiscordに通知する。

## 概要
ベテルギフトのサイトを確認、出品状況をチェックし、webhook URLのdiscordチャンネルに通知を送信する。新規商品のうち、額面比率が一定より下の場合のみ通知する。  
例： **額面比率90%以下の商品を通知する場合、**
> **額面40,000円のギフト券が新規で35,400円で出品された（4,600円OFF、額面比率88.5%）**  
-----> **通知する**

> **額面1,000円のギフト券が新規で950円で出品された（50円OFF、額面比率95%）**  
-----> **通知されない**

すなわち、**一定よりお得なラインの商品のみ通知する**ことが可能。

![スクリーンショット 2024-06-05 011836](https://github.com/nekoy3/b_gift/assets/84169441/361fa2a4-8a79-4b71-b1b6-40fe0e7a2d44)  

## 構築手順
1. python3.10が動く環境とpython3.10-venvが入った環境を用意する。（仮想環境を使う場合）
```shell
$ python -V
Python 3.10.12
$ sudo apt install python3.10-venv
```
2. リポジトリをクローンする
```shell
$ git clone https://github.com/nekoy3/b_gift
```
3. 仮想環境を使う場合はvenvを構築し、アクティベートする。
```shell
$ python3 -m venv b_gift
$ ls -l
total 36
drwxrwxr-x 5 b_gift b_gift 4096 Jun  5 00:57 b_gift
...

$ source b_gift/bin/activate
(b_gift) $
```
4. requirements.txtのライブラリをインストールする
```shell
$ python3 -m pip install requirements.txt
```
5. main.pyを実行して、スクレイピングを開始する。
```shell
$ python3 main.py
Config file config.cfg created.

$ vi config.cfg
※configは後記

$ python3 main.py 
[Errno 2] No such file or directory: 'data_numlist.txt'

$ cp data_numlist-template.txt data_numlist.txt
$ vi data_numlist.txt
※欲しい情報のギフト券のコメントアウトのみ削除してください。

$ vi webhook.txt
※チャンネルのwebhook URLを入力

$ python3 main.py
[Errno 2] No such file or directory: gift_xx.txt
※初回実行時のみエラーが出る。差分の通知を行うプログラムなので、ここで通知は行われない。
```

## config.cfg
```
[general]
threshold_notification = 87
notification_level = 1
extra_notification = 85
```
threshold_notification(50-100) ... 額面比率がn%以下の商品のみ通知する。（default: 90)
notification_level(1-3) ... 通知レベル。2, 3はデバッグ用（default: 1)
extra_notification ... threashold_notification以下の値を入力すると、メンション付き通知を行う。（default: 85)

# License
 
"b_gift_discord" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
