import pytube
from pytube import YouTube
import time

url=input("Bir YouTube Url'si Giriniz:")
YouTube1=pytube.YouTube(url)

if YouTube1.length>=120:
    long=input("Video'nun süresi 2 dakikadan uzun yine de indirmek istiyor musun?:")
    if long=='hayır' or long=='Hayır':
        print("O halde 2 dakikadan kısa bir video Url'si gir" )
    elif long=='evet' or long=='Evet':
         print("Video indiriliyor..")
         print("Video İsmi:",YouTube1.title)
         if YouTube1.views>1000000:
            print("Video Çok Populer Bir Video..:)")
         else:
            print("Video izlenme sayısı düşük.. :(")
         print("Video'yu Yükleyen Kanal:",YouTube1.author)
         print("Video'nun Resmi:",YouTube1.thumbnail_url,)
         print("Video'nun Açıklaması:",YouTube1.description)
         print("Video'nun Yüklendiği Tarih",YouTube1.publish_date)