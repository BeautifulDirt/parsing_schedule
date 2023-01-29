import telebot
import datetime
import configparser

config = configparser.ConfigParser()
config.read("/sled_schedule/src/configs/settings.ini")

def post_stories_tg(date_post: datetime.date, config: dict, text: str = ''):
    bot = telebot.TeleBot(config["token"])
    bot.send_photo(config["channel"], 
                    photo=open(f"/sled_schedule/src/img/result/sled_{date_post.strftime('%Y%m%d')}.jpg", 'rb'), 
                    caption=text)
    
if __name__ == "__main__":
    #публикуем сториз 
    today = datetime.date.today()
    tg_settings = config["tg_send_post"]
    post_stories_tg(date_post=today, config=tg_settings)



