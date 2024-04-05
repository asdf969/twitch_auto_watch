import requests
import webbrowser
import time

# Twitch API�ݒ�
client_id = '�����ɃN���C�A���gID����͂��Ă�������'
access_token = '�����ɃA�N�Z�X�g�[�N������͂��Ă�������'
streamer_username_yuyu = 'yuyuta0702'
streamer_username_katou = 'kato_junichi0817'  # �����ɍD���Ȕz�M�҂̃��[�U�[������͂��Ă�������

# Twitch�z�M�҂̃y�[�WURL
stream_url_yuyu = f'https://www.twitch.tv/{streamer_username_yuyu}'
stream_url_katou = f'https://www.twitch.tv/{streamer_username_katou}'

# API��URL
url_yuyu = f'https://api.twitch.tv/helix/streams?user_login={streamer_username_yuyu}'
url_katou = f'https://api.twitch.tv/helix/streams?user_login={streamer_username_katou}'

# �w�b�_�[���
headers = {
    'Client-ID': client_id,
    'Authorization': f'Bearer {access_token}'
}

# �z�M�҂��I�����C�����`�F�b�N����֐�
def check_streamer_online_yuyu():
    response = requests.get(url_yuyu, headers=headers).json()
    return bool(response['data'])

def check_streamer_online_katou():
    response = requests.get(url_katou, headers=headers).json()
    return bool(response['data'])

# �z�M�҂̏�Ԃ��|�[�����O����
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
        time.sleep(180)  # 180�b�҂��čă`�F�b�N
