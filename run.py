import datetime

from make_stories import cover_stories, create_stories
from parsfivechannel import parsFiveChannel
from post_vk import upload_msg_chat, upload_stories_vk

if __name__ == "__main__":

    # берем дату завтрешнего дня
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    print(tomorrow)

    #формируем обложку для сторис
    cover_stories(date_stories=tomorrow)

    #берем расписание с сайта Пятого канала
    text_time, text_name = parsFiveChannel(date_stories=tomorrow)
    print(text_time)
    print(text_name)

    # формируем сторис
    create_stories(date_stories=tomorrow, text_time=text_time, text_name=text_name)

    #отправляем сторис в чат ВК
    upload_msg_chat(date_stories=tomorrow, text_name=text_name, text_time=text_time)

    #публикуем сториз
    #upload_stories_vk(date_stories=tomorrow)

    