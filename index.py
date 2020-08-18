import requests
import fake_useragent
from bs4 import BeautifulSoup

linkOnWebSite = 'https://zastavok.net'
weNeedPictures = 18 #Сколько изображений вам нужно? Должно быть кратно 18)
classicRange = 2400 #страниц обойдёт парсер, если он раньше не наткнёться на break
counter = 0

for i in range(classicRange):
    response = requests.get(linkOnWebSite).text
    soup = BeautifulSoup(response, 'html5lib')
    motherBlock = soup.find('div', class_='block-photo')
    findAllLinksFromMotherBlock = motherBlock.find_all('a')

    for outLinkOnPageWithImg in findAllLinksFromMotherBlock:
        if (outLinkOnPageWithImg.get('href').find('.html') != -1):
            counter += 1
            pageWithImg = requests.get(f"{linkOnWebSite}{outLinkOnPageWithImg.get('href')}").text
            LinkOnDonwloadImg = BeautifulSoup(pageWithImg,'html5lib')\
                .find('div', class_='block_down')\
                .find('a')\
                .get('href')

            imageByte = requests.get(f"{linkOnWebSite}{LinkOnDonwloadImg}").content
            with open(f'./image/{counter}.jpg', 'wb') as file:
                file.write(imageByte)
    if (counter >= weNeedPictures):
        break

