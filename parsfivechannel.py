from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import datetime
import requests
import re

def _get_name_series(s):
    return _text_series_format(re.findall(r'«([^\"]*)»', s)[0])

def _time_format(t):
    try:
        int(t[:2])
        return t
    except ValueError:
        return '0'+t

def _text_series_format(s):
    text_list = s.split(' ')
    if len(' '.join(text_list[:3])) >= 30 and len(text_list) > 3:
        return ' '.join(text_list[:2]) + '\n' +  ' '.join(text_list[2:]), True
    elif len(text_list) > 4:
        return ' '.join(text_list[:3]) + '\n' +  ' '.join(text_list[3:]), True
    else:
        return s, False
         
def parsFiveChannel(date_stories: datetime.date):

    url = 'https://www.5-tv.ru/schedule/'
    page = requests.get(url, params={
                            'date': date_stories.strftime('%d.%m.%Y'),
                            'User-Agent': UserAgent().firefox})

    filteredTVs = {}
    allTVs = []

    soup = BeautifulSoup(page.text, "html.parser")

    allTVs = soup.findAll('div', class_='tvb')

    for data in allTVs:
        elem = data.find('div', class_='tvbBody')
        if elem is not None:
            if "след." in elem.text.lower():
                series_name, f = _get_name_series(elem.text)
                series_name = series_name.upper()
                s = ''
                if f:
                    s = '\n'
                times = _time_format(data.find('div', class_='tvbTime').text+s)
                filteredTVs.update({times : series_name.replace('СЛЕД. ', '')})

    return '\n'.join(filteredTVs.keys()), '\n'.join(filteredTVs.values())







