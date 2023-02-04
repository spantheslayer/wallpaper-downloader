import requests
import os
import progressbar

def download_wallpapers(query):
    API_KEY = "unsplash_APi_key"
    URL = f"https://api.unsplash.com/search/photos?query={query}&per_page=30&orientation=landscape&client_id={API_KEY}"
    response = requests.get(URL)
    data = response.json()
    wallpapers = [img for img in data['results'] if img['width'] >= 3840 and img['height'] >= 2160]

    widgets = [progressbar.Percentage(), ' ', progressbar.Bar(), ' ', progressbar.ETA()]
    bar = progressbar.ProgressBar(widgets=widgets, maxval=len(wallpapers)).start()

    for index, wallpaper in enumerate(wallpapers):
        response = requests.get(wallpaper['urls']['full'])
        if response.status_code == 200:
            open(f"wallpapers/{wallpaper['id']}.jpg", "wb").write(response.content)
        bar.update(index + 1)
    bar.finish()

if not os.path.exists("wallpapers"):
    os.makedirs("wallpapers")

query = input("Enter the wallpaper tag: ")
download_wallpapers(query)
