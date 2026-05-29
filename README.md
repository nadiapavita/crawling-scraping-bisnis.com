# Bisnis.com Crawler & Scraper

Crawler dan scraper untuk mengambil informasi artikel dari bisnis.com.

## Arsitektur

```text
crawler.py
    ↓
scraper.py
    ↓
backtrack.py / standard.py
```

* `crawler.py` bertugas mengambil link artikel dari bisnis.com.
* `scraper.py` bertugas mengambil detail artikel (judul, tanggal publish, isi artikel, dan link).
* `backtrack.py` menjalankan crawler dan scraper untuk mengambil artikel berdasarkan rentang tanggal tertentu.
* `standard.py` menjalankan crawler sebagai long running process yang melakukan pengecekan artikel terbaru secara berkala.

## Output

Output disimpan dalam format JSON dengan field:

* Judul
* Tanggal
* Isi
* Link

Tanggal disimpan dalam format ISO 8601
