import vk_api
import requests
import datetime
import configparser

config = configparser.ConfigParser()
config.read("/sled_schedule/src/configs/settings.ini")

def _initial_connect_vk(token: str):
    vk = vk_api.VkApi(token=token)
    vk._auth_token()
    vk.get_api()
    upload = vk_api.VkUpload(vk)

    return vk, upload

def upload_msg_chat(date_stories: datetime.date, text_name: str, text_time: str):
    group_settings = config["vk_send_msg"]
    vk, upload = _initial_connect_vk(token=group_settings["token"])
    
    id_chat = int(group_settings["id_chat"])
    photo = upload.photo_messages(f"/sled_schedule/src/img/result/sled_{date_stories.strftime('%Y%m%d')}.jpg")

    owner_id = photo[0]['owner_id']
    photo_id = photo[0]['id']
    access_key = photo[0]['access_key']

    text = f"Расписание серий на {date_stories.strftime('%d.%m.%Y')}: \n \
@beautifuldirt тебе время и серии на пост 👇 \n \
{text_name} \n \
{text_time} \n \
@snowfeniks тебе картинку в инстаграм 👇"

    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.method("messages.send", {"peer_id": id_chat, 
                                "random_id": 0, 
                                "attachment": attachment, 
                                "message": text})

def _vk_get(method, params):
    url = f'https://api.vk.com/method/{method}'

    group_settings = config["vk_send_stories"]
    params['access_token'] = group_settings["token"]
    params['v'] = '5.131'

    res = requests.get(url, params=params)

    return res.json()['response']

def _vk_upload(file_path, url):
    with open(file_path, 'rb') as fp:
        files = {'file': fp}
        resp = requests.post(url, files=files)
    return resp.json()['response']

def upload_stories_vk(date_stories):
    group_settings = config["vk_send_stories"]
    id_group = int(group_settings["id_group"])
    
    resp_get = _vk_get(method="stories.getPhotoUploadServer", params={"add_to_news": 1, "group_id": id_group})
    resp_upload = _vk_upload(file_path=f"/sled_schedule/src/img/result/sled_{date_stories.strftime('%Y%m%d')}.jpg", url=resp_get["upload_url"])
    _vk_get(method="stories.save", params={"upload_results": resp_upload["upload_result"]})

if __name__ == "__main__":
    #публикуем сториз
    today = datetime.date.today()
    upload_stories_vk(date_stories=today)
