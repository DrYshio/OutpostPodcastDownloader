import urllib.request
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



url = 'https://giantgnome.com/our-shows/audio-drama/star-trek-outpost/#STOepisodes'


