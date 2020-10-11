import urllib.request
import os
from bs4 import BeautifulSoup


def get_contents_links(url):
    episode_list = {}
    req = urllib.request.Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    content = soup.find_all("ul", class_="episodeList")[0]
    for episode in content('a'):
        try:
            episode_name = episode['title'][19:]
        except KeyError:
            episode_name = episode.contents[0]
        episode_list[episode_name] = episode['href']
    return episode_list


def download_content(episode_list):

    for episode_name in episode_list.keys():
        url = urllib.request.urlopen(episode_list[episode_name])
        try:
            os.mkdir(os.path.join(os.getcwd(), "content"))
        except FileExistsError:
            pass
        f = open(os.path.join(os.getcwd(), "content", episode_name), 'wb')
        meta = url.info()
        file_size = int(meta['Content-Length'])
        print(f"Downloading: {episode_name} Bytes: {file_size}")

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = url.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = f"{file_size_dl} bytes - {' ' * (10-len(str(file_size_dl)))}{round(file_size_dl * 100. / file_size, 1)}%"
            status = status + chr(8) * (len(status) + 1)
            print(status)

        f.close()

url = 'https://giantgnome.com/our-shows/audio-drama/star-trek-outpost/#STOepisodes'


