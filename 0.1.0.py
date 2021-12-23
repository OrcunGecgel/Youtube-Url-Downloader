from pytube import YouTube
url=input("Bir YouTube Url'si Giriniz:")
YouTube1=pytube.YouTube(url)

print(YouTube1.title)
print(YouTube1.views)
print(YouTube1.author)
print(YouTube1.length)
print(YouTube1.thumbnail_url)
print(YouTube1.description)
print(YouTube1.publish_date)










