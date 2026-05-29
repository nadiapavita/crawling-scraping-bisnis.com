import requests
from bs4 import BeautifulSoup
# tugas crawling itu ngambil link link artikel yg ada di halaman itu
url = "https://bisnis.com/"

def get_link(url, latest=False):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = []
    if latest:
        # Cari elemen h3 dengan teks "Berita Terbaru"
        h3 = soup.find('h3', string="Berita Terbaru")
        if h3:
            # langsung ambil link href pertama yg muncul setelah h3 tersebut
            a = h3.find_next('a', class_ = "artLink")
            links.append(a['href'])
            return links
    else:
        artikel_tags = soup.find_all('a', class_="artLink")
        for a in artikel_tags:
            links.append(a['href'])
        return links

# print(get_link(url, latest=True))