#mainでは旧データと比較し差分を確認、必要があれば通知を飛ばす


from file_io import read_list_from_file
from file_io import save_list_to_file
from file_io import read_or_create_config
from gift import get_data
from discord import sent_discord

tn_percents, global_level = read_or_create_config()
if tn_percents is None:
   tn_percents = 90
if global_level is None:
   global_level = 1

def find_difference(original_data, updated_data):
    added_data = [line for line in updated_data if line not in original_data]
    removed_data = [line for line in original_data if line not in updated_data]
    return added_data, removed_data

# 設定されたレベル(global_level)が与えられた(必要な)レベルを超えたときのみ通知
def send_message(lv, text):
    global global_level
    if global_level >= lv:
       sent_discord(text)

get_list = []
try:
    get_list = read_list_from_file("data_numlist.txt", is_numlist=True)
except FileNotFoundError as e:
    print(str(e))

#ファイルが存在しなければ比較処理をスルーする
new_id = []
old_data_dict = dict()
for i in get_list:
    try:
      l = read_list_from_file("gift_" + str(i[0]) + ".txt")
      old_data_dict[str(i[0])] = l
    except FileNotFoundError as e:
      print(str(e))
      send_message(2, "新規 --> " + str(i[0]))
      new_id.append(i[0])

for i in get_list:
    t_list = get_data(i[0])
    save_list_to_file("gift_" + str(i[0]) + ".txt", t_list)
    if i[0] in new_id:
       continue
    added, removed = find_difference(old_data_dict[str(i[0])], t_list)
    added = [' '.join(i) for i in added]
    removed = [' '.join(i) for i in removed]

    # 差分通知
    # Ctrl+K -> Ctrl+C (Ctrl+U)
    added_str = '\n'.join(added)
    removed_str = '\n'.join(removed)
    if added_str == "" and removed_str == "":
       continue
    s = f""" \
{i[1]} 差分\n \
    ★削除データ\n \
{removed_str}\n \
    ★追加データ\n \
{added_str}\n \
    """
    send_message(2, s)

    # 追加データのうち、threshold_notificationを下回っているデータを通知


"""
今後
設定ファイルを読み込むようにして、一定パーセンテージ以上の商品が追加されたときに通知する、他は通知しないように設定したい
embedで送っているので、もうちょっと見栄えを良くしたい
Linuxサーバ上で動くように対応させる(そのままでも動くか・・・？
データの中身について詳しくみられるように（エラー回数は無視、点数確認、パーセンテージ通知など）したい
"""