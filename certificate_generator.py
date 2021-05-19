from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
df = pd.read_csv('form_responses.csv')
font = ImageFont.truetype('/usr/share/fonts/Menlo for Powerline.ttf',60)
for index, j in df.iterrows():
    img = Image.open('img/Certificate_final.jpg')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1361,1275), text='{}'.format(j['Name']),fill=(255,255,255),font=font)
    img.save('pictures/{}.jpg'.format(j['Name']))