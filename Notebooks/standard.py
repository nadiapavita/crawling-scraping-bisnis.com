# crawler akan berperan sebagai long running process yg secara berkala akan mengambil artikel terbaru dari bisnis.com. 
# outputnya adalah json file yg berisi artikel terbaru. Interval penarikan bisa di config
from crawler import get_link
from scraper2 import get_data, save_to_json
import time
# config nya, selama sekian menit sekali start loop
# proses looping terus terusan, jeda nya sekian menit
# penanda mulai crawling, dimulai dari h3 Berita Terbaru

last_link = ""
data_list = []
while True:
    # ambil link
    link = get_link("https://bisnis.com/", latest=True)
    # if beda dari last_link:
    if link != last_link:
    # scrape
        try:
            data = get_data(link[0])
            # print(data)
        except:
            continue
    # save
        data_list.append(data)
        save_to_json(data_list, 'output_standard.json')
    # update last_link
        last_link = link

    # sleep interval
    time.sleep(60)
    print("sleep")