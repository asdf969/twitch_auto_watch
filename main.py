import requests
import webbrowser
import time

# Twitch API設定
client_id = 'ここにクライアントIDを入力してください'
access_token = 'ここにアクセストークンを入力してください'
streamer_username_yuyu = 'yuyuta0702'
streamer_username_katou = 'kato_junichi0817'  # ここに好きな配信者のユーザー名を入力してください

# Twitch配信者のページURL
stream_url_yuyu = f'https://www.twitch.tv/{streamer_username_yuyu}'
stream_url_katou = f'https://www.twitch.tv/{streamer_username_katou}'

# APIのURL
url_yuyu = f'https://api.twitch.tv/helix/streams?user_login={streamer_username_yuyu}'
url_katou = f'https://api.twitch.tv/helix/streams?user_login={streamer_username_katou}'

# ヘッダー情報
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}'
}

# 配信者がオンラインかチェックする関数
def check_streamer_online_yuyu():
    response = requests.get(url_yuyu, headers=headers).json()
    return bool(response['data'])

def check_streamer_online_katou():
    response = requests.get(url_katou, headers=headers).json()
    return bool(response['data'])

# 配信者の状態をポーリングする
while True:
    if check_streamer_online_yuyu():
        print(f"{streamer_username_yuyu} is streaming now! Opening in browser.")
        webbrowser.open(stream_url_yuyu)
        break
    elif check_streamer_online_katou():
        print(f"{streamer_username_katou} is streaming now! Opening in browser.")
        webbrowser.open(stream_url_katou)
        break
    else:
        print(f"{streamer_username_yuyu, streamer_username_katou} is not streaming. Checking again in 180 seconds.")
        time.sleep(180)  # 180秒待って再チェック
