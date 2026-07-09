import os
import csv
import datetime

# ==========================================
# 1. SAKELAR DUIT UTAMA
# ==========================================
ID_AGODA = "1234567"
ID_BOOKING = "99999"
ID_KLOOK = "88888"
ID_GETYOURGUIDE = "77777"
BASE_URL = "https://docepdev.github.io/"

# ==========================================
# 2. DATABASE MASSAL (DARI CSV)
# ==========================================
data_destinasi = []
with open("destinasi.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        data_destinasi.append(row)

# ==========================================
# 3. PROSES PRODUKSI HTML & SITEMAP
# ==========================================
link_halaman = ""
xml_urls = f"  <url>\n    <loc>{BASE_URL}</loc>\n  </url>\n"

current_time = datetime.datetime.now()
updated_str = current_time.strftime("Updated %B %Y")

for item in data_destinasi:
    nama_file = f"liburan-ke-{item['kota'].lower().replace(' ', '-')}.html"
    link_halaman += f'<li><a href="{nama_file}">Budget Travel Guide to {item["kota"]}</a></li>\n'
    
    # Tambah ke daftar sitemap XML
    xml_urls += f"  <url>\n    <loc>{BASE_URL}{nama_file}</loc>\n  </url>\n"
    
    kota_encoded = item['kota'].replace(' ', '%20')
    if item['wilayah'].lower() == 'asia':
        LINK_AFFILIATE_HOTEL = f"https://www.agoda.com/partners/partnerlanding.aspx?pcs=1&cid={ID_AGODA}&city={kota_encoded}"
        LINK_AFFILIATE_TOUR = f"https://www.klook.com/search/result/?query={kota_encoded}&aid={ID_KLOOK}"
        hotel_brand = "Agoda"
    else:
        LINK_AFFILIATE_HOTEL = f"https://www.booking.com/searchresults.html?city={kota_encoded}&aid={ID_BOOKING}"
        LINK_AFFILIATE_TOUR = f"https://www.getyourguide.com/s/?q={kota_encoded}&partner_id={ID_GETYOURGUIDE}"
        hotel_brand = "Booking.com"

    konten_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Budget travel guide to {item['kota']}, {item['negara']}. Explore attractions, costs, and hotels ({updated_str}).">
    <title>Budget Travel Guide to {item['kota']} ({updated_str})</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color: #f9f9f9; color: #333; }}
        .container {{ max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: 0 auto; }}
        h1 {{ color: #2c3e50; }}
        .highlight {{ font-weight: bold; color: #e67e22; }}
        .btn-box {{ background: #2ecc71; padding: 15px; text-align: center; border-radius: 5px; margin: 20px 0; }}
        .btn-box a {{ color: white; text-decoration: none; font-weight: bold; font-size: 18px; display: block; }}
        .hotel-box {{ background: #fff3cd; padding: 20px; border-left: 5px solid #ffc107; margin-top: 25px; border-radius: 5px; }}
        .hotel-box h2 {{ margin-top: 0; color: #856404; font-size: 22px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Budget Travel Guide to {item['kota']} ({updated_str})</h1>
        <p>Looking for a vacation with <strong>{item['cuaca']}</strong> weather? <span class="highlight">{item['kota']}</span> is the perfect destination for you!</p>
        
        <h2>Must-Visit Attractions</h2>
        <p>Don't miss the chance to explore <strong>{item['tempat']}</strong>, the ultimate iconic spots in the city.</p>
        
        <div class="hotel-box">
            <h2>Where to Stay & Recommended Hotels</h2>
            <p><strong>Best Area to Stay:</strong> {item.get('area_terbaik', '')}</p>
            <p><strong>Recommended Hotels:</strong> {item.get('hotel_rekomendasi', '')}</p>
            <div class="btn-box" style="background: #e74c3c; margin-bottom: 5px;">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow">Check Room Availability on {hotel_brand} ↗</a>
            </div>
            <p style="font-size: 12px; color: #7f8c8d; text-align: center; margin-top: 0;">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <h2>Estimated Budget & Expenses</h2>
        <p>To fully enjoy your trip here, we highly recommend preparing a budget around <span class="highlight">{item['biaya']}</span>.</p>
        
        <div class="btn-box" style="background: #3498db;">
            <a href="{LINK_AFFILIATE_TOUR}" target="_blank" rel="nofollow">Check Best Activities & Tours HERE ↗</a>
        </div>

        <hr>
        <p><a href="index.html">← Back to Homepage</a></p>
    </div>
</body>
</html>"""
    
    with open(nama_file, "w") as f:
        f.write(konten_html)

# ==========================================
# 4. CETAK INDEX & SITEMAP.XML
# ==========================================
beranda_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Travel Guide Portal</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color: #f4f4f9; }}
        .container {{ max-width: 800px; background: white; padding: 30px; border-radius: 8px; margin: 0 auto; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 15px 0; padding: 10px; background: #fdfdfd; border-left: 5px solid #2ecc71; }}
        a {{ color: #2ecc71; text-decoration: none; font-size: 18px; font-weight: bold; }}
        a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Global Travel Guide Portal</h1>
        <p>Discover affordable and budget-friendly travel guides to major cities worldwide:</p>
        <ul>
            {link_halaman}
        </ul>
    </div>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(beranda_html)

# Bungkus sitemap ke format XML standard Google
sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_urls}</urlset>"""

with open("sitemap.xml", "w") as f:
    f.write(sitemap_xml)

print("---")
print("SITEMAP GENERATED: File sitemap.xml berhasil dibuat!")
print("---")
