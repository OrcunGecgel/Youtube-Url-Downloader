import pytube


while True:
    url = input("Bir YouTube Url'si Giriniz:")
    if url=="çıkış":
        print("çıkış yapıldı")
        break
    else:
        YouTubed = pytube.YouTube(url)
        if YouTubed.length>=120:
            long=input("Video'nun süresi 2 dakikadan uzun yine de indirmek istiyor musun?:")
            if long=='hayır' or long=='Hayır' or long=='HAYIR':
                print("O halde 2 dakikadan kısa bir video Url'si gir" )
            elif long=='evet' or long=='Evet' or long=='EVET':
                print("Video İsmi:",YouTubed.title)
                if YouTubed.views>1000000:
                    print("Video Çok Populer Bir Video..:)")
                else:
                    print("Video izlenme sayısı düşük.. :(")
                print("Video'yu Yükleyen Kanal:",YouTubed.author)
                print("Video'nun Resmi:",YouTubed.thumbnail_url,)
                print("Video'nun Açıklaması:",YouTubed.description)
                print("Video'nun Yüklendiği Tarih:",YouTubed.publish_date)
                for stream in YouTubed.streams:
                    print(stream)
                video=YouTubed.streams.get_highest_resolution()
                video.download("C:/Users/irem_/Downloads")
                print(YouTubed.title,"Videosu indirildi..")
            else:
                print("Lütfen evet ya da hayır olarak Cevaplayınız..")
