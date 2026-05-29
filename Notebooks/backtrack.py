# crawler menerima parameter start date dan end date. Outputnya adalah json file yg berisi list artikel 
# dari bisnis.com yg tanggal terbitnya berada di rentang start dan end date. 
from crawler import get_link
from scraper2 import get_data, save_to_json
from datetime import datetime

start_date = datetime.strptime("2026-05-27", "%Y-%m-%d")
end_date = datetime.strptime("2026-05-29", "%Y-%m-%d")
data_list = []

# proses crawling
links = get_link("https://bisnis.com/")
# print(links)

# proses loop
for link in links:
    # proses scraping
    try:
        data = get_data(link)
    except:
        continue
    # print(data) 
    # kalo hasil scraping date nya sesuai maka output get_data di masukan ke list data_list
    data_tanggal = datetime.fromisoformat(data['Tanggal'])
    if start_date <= data_tanggal <= end_date:
        data_list.append(data)
    # kalo hasil scraping date nya tidak sesuai maka skip
# looping nya sampe semua link di crawler abis
# data_list disave to json
save_to_json(data_list, 'data_full.json')