import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
# tugas scraping itu ngambil data2 yg ada di halaman itu. sekalian masukin ke json nya juga 
# url = "https://plus.bisnis.com/read/129/konglomerat-ri-penikmat-cuan-bisnis-ebt-saat-barat-mulai-berpaling"

def get_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    script_tag = soup.find("script")

    batas_kiri = script_tag.text.rfind('{')
    batas_kanan = script_tag.text.rfind('}')
    isi_content = script_tag.text[batas_kiri:batas_kanan+1]

    isi_content_json = json.loads(isi_content)

    tanggal = isi_content_json['content_published_date']
    datetime_object = datetime.strptime(tanggal, '%Y-%m-%d %H:%M:%S')

    isi = ""
    artikel_tags = soup.find('article', class_="detailsContent")
    if artikel_tags:
        # if ada, cari paragraph-paragraph yang ada di <p> di dalam article
        # if ada, masukin ke isi
        paragraph = artikel_tags.find_all('p')
        for p in paragraph:
            isi += p.text.strip() + "\n"
    else:
        # if gak ada, cari di class 1 nya lagi, terus repeat
        artikel_tags = soup.find('div', class_="detail-news__article")
        if artikel_tags:
            paragraph = artikel_tags.find_all('p')
            for p in paragraph:
                isi += p.text.strip() + "\n"
        if not isi: # bisa karena artikel premium/interaktif/yg lainnya
            isi = ""

    data = {
        'Judul': isi_content_json['content_title'],
        'Tanggal': datetime_object.isoformat(),
        'Isi': isi,
        'Link': url
    }
    return data

# print(get_data(url))

# print("judul:", isi_content_json['content_published_date'])

def save_to_json(data, filename):
    import json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)