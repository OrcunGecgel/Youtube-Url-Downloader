import pytube
from pytube import YouTube

url=input("Bir YouTube Url'si Giriniz:")
YouTube1=pytube.YouTube(url)

if YouTube1.length>=120:
    long=input("Videonun süresi 2 dakikadan uzun yine de indirmek istiyor musun?:")
    if long=='evet' or long=='Evet':
        print("Video indiriliyor..")
    elif long=='hayır' or long=='Hayır':
         print("O halde 2 dakikadan kısa bir video Url'si gir" )
         print("Video İsmi:",YouTube1.title)
         if YouTube1.views>1000000:
            print("Video Çok Populer Bir Video..:)")
         else:
            print("Video izlenme sayısı düşük.. :(")
         print("Videoyu Yükleyen Kanal:",YouTube1.author)
         print("Videonun Resmi:",YouTube1.thumbnail_url,)
         print("Videonun Açıklaması:",YouTube1.description)
         print("Videonun Yüklendiği Tarih",YouTube1.publish_date)

