import vk_api
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

def upload_stories_vk(date_stories):
    group_settings = config["vk_send_stories"]
    vk, upload = _initial_connect_vk(token=group_settings["token"])

    id_group = int(group_settings["id_group"])

    upload.story(file=f"/sled_schedule/src/img/result/sled_{date_stories.strftime('%Y%m%d')}.jpg", 
                file_type="photo", 
                add_to_news=True, 
                group_id=id_group)

if __name__ == "__main__":
    #публикуем сториз
    today = datetime.date.today()
    upload_stories_vk(date_stories=today)
