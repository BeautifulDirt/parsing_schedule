import datetime
from PIL import Image, ImageDraw, ImageFont

def cover_stories(date_stories: datetime.date):
    x = 800
   
    image_path = f"/sled_schedule/src/img/initial/screen_{date_stories.strftime('%Y%m%d')}"

    try:
        img = Image.open(f'{image_path}.jpg')
    except FileNotFoundError:
        img = Image.open(f'/sled_schedule/src/img/initial/screen_.jpg')

    y = int((float(img.size[1])*float(x))/float(img.size[0]))

    new_image = img.resize((x, y))
    new_image.save(f'{image_path}.png')

def create_stories(date_stories: datetime.date, text_time: str, text_name: str):

    date_stories = date_stories.strftime("%Y%m%d")
    img = Image.open('/sled_schedule/src/img/templates/background.jpg')
    watermark = Image.open(f'/sled_schedule/src/img/initial/screen_{date_stories}.png')
    water = Image.open('/sled_schedule/src/img/templates/header.png')

    watermark = watermark.convert('RGBA')

    xx, yy = (0, 0)

    img.paste(watermark, (xx, yy),  watermark)
    img.paste(water, (xx, yy),  water)

    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("/sled_schedule/src/font/calibri.ttf", 32)

    x, y = (80, 700)

    draw.text((x, y), text_time, font=font, fill=(17,183,177))
    draw.text((x+80, y), text_name.upper(), font=font, fill=(255,255,255))

    img.save(f"/sled_schedule/src/img/result/sled_{date_stories}.jpg")
