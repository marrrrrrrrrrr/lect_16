# დაწერეთ პროგრამა, რომელიც ქმნის რამდენიმე ძაფს (Thread) და იწერს რამდენიმე mp3 ფაილს ინტერნეტიდან.


import requests, time, concurrent.futures

mp3_urls = [
   "http://commondatastorage.googleapis.com/codeskulptor-demos/DDR_assets/Kangaroo_MusiQue_-_The_Neverwritten_Role_Playing_Game.mp3",

   "http://codeskulptor-demos.commondatastorage.googleapis.com/pang/paza-moduless.mp3",

   "http://codeskulptor-demos.commondatastorage.googleapis.com/GalaxyInvaders/theme_01.mp3"

]


def download(url):
  mp3_bytes = requests.get(url).content
  mp3_name = url.split('/')[-1]

  with open(mp3_name, mode="wb") as mp3_file:
    mp3_file.write(mp3_bytes)

  print(f"{mp3_name} was downloaded!")


t1 = time.time()

with concurrent.futures.ThreadPoolExecutor() as executor:
  executor.map(download, mp3_urls)

t2 = time.time()

print(f"Toral time is {t2 - t1} seconds...")