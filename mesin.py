import os
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
# 2. DATABASE MASSAL (30 DESTINASI EMAS 2026)
# ==========================================
data_destinasi = [
    {
        "city": "Matera",
        "country": "Italy",
        "region": "Europe",
        "main_attraction": "Sassi di Matera",
        "target_keyword": "best luxury cave hotels in Matera Sassi"
    },
    {
        "city": "Tropea",
        "country": "Italy",
        "region": "Europe",
        "main_attraction": "Spiaggia della Rotonda (Tropea Beach)",
        "target_keyword": "affordable beachfront cliff hotels in Tropea"
    },
    {
        "city": "Ksamil",
        "country": "Albania",
        "region": "Europe",
        "main_attraction": "Ksamil Islands",
        "target_keyword": "best apartments with sea view in Ksamil Riviera"
    },
    {
        "city": "Kotor",
        "country": "Montenegro",
        "region": "Europe",
        "main_attraction": "Bay of Kotor",
        "target_keyword": "top boutique guesthouses near Kotor Old Town"
    },
    {
        "city": "Budva",
        "country": "Montenegro",
        "region": "Europe",
        "main_attraction": "Budva Citadel",
        "target_keyword": "best luxury spa resorts in Budva Montenegro"
    },
    {
        "city": "Tartu",
        "country": "Estonia",
        "region": "Europe",
        "main_attraction": "Tartu Old Town Square",
        "target_keyword": "romantic boutique hotels in Tartu city center"
    },
    {
        "city": "Plovdiv",
        "country": "Bulgaria",
        "region": "Europe",
        "main_attraction": "Ancient Theatre of Philippopolis",
        "target_keyword": "cheap historical hotels in Plovdiv Old Town"
    },
    {
        "city": "Ghent",
        "country": "Belgium",
        "region": "Europe",
        "main_attraction": "Gravensteen Castle",
        "target_keyword": "top rated canal view hotels in Ghent center"
    },
    {
        "city": "Lecce",
        "country": "Italy",
        "region": "Europe",
        "main_attraction": "Piazza del Duomo",
        "target_keyword": "best traditional bed and breakfast in Lecce Puglia"
    },
    {
        "city": "Naxos",
        "country": "Greece",
        "region": "Europe",
        "main_attraction": "Portara (Temple of Apollo)",
        "target_keyword": "best quiet family beach resorts in Naxos island"
    },
    {
        "city": "Milos",
        "country": "Greece",
        "region": "Europe",
        "main_attraction": "Sarakiniko Beach",
        "target_keyword": "luxury whitewashed hotels with private pool in Milos"
    },
    {
        "city": "Riga",
        "country": "Latvia",
        "region": "Europe",
        "main_attraction": "House of the Black Heads",
        "target_keyword": "best affordable boutique hotels in Riga Old Town"
    },
    {
        "city": "Ischia",
        "country": "Italy",
        "region": "Europe",
        "main_attraction": "Aragonese Castle",
        "target_keyword": "best volcanic thermal spa hotels in Ischia Italy"
    },
    {
        "city": "Faro",
        "country": "Portugal",
        "region": "Europe",
        "main_attraction": "Ria Formosa Natural Park",
        "target_keyword": "cheap authentic guesthouses near Faro Algarve"
    },
    {
        "city": "Sibiu",
        "country": "Romania",
        "region": "Europe",
        "main_attraction": "Piata Mare (Large Square)",
        "target_keyword": "best medieval places to stay in Sibiu Transylvania"
    },
    {
        "city": "Labuan Bajo",
        "country": "Indonesia",
        "region": "Asia",
        "main_attraction": "Komodo National Park",
        "target_keyword": "luxury phinisi liveaboard tours Labuan Bajo"
    },
    {
        "city": "Lombok",
        "country": "Indonesia",
        "region": "Asia",
        "main_attraction": "Mount Rinjani",
        "target_keyword": "best quiet beachfront eco villas in south Lombok"
    },
    {
        "city": "Gili Air",
        "country": "Indonesia",
        "region": "Asia",
        "main_attraction": "Gili Air Coral Reefs",
        "target_keyword": "top sustainable diving resorts in Gili Air"
    },
    {
        "city": "Mui Ne",
        "country": "Vietnam",
        "region": "Asia",
        "main_attraction": "Red Sand Dunes",
        "target_keyword": "best kitesurfing beach resorts near Mui Ne"
    },
    {
        "city": "Sa Pa",
        "country": "Vietnam",
        "region": "Asia",
        "main_attraction": "Fansipan Mountain",
        "target_keyword": "best authentic mountain view homestays in Sa Pa"
    },
    {
        "city": "Phu Quoc",
        "country": "Vietnam",
        "region": "Asia",
        "main_attraction": "Sao Beach",
        "target_keyword": "luxury private family beachfront resorts Phu Quoc"
    },
    {
        "city": "Port Barton",
        "country": "Philippines",
        "region": "Asia",
        "main_attraction": "Port Barton Marine Park",
        "target_keyword": "affordable beachfront cottages in Port Barton Palawan"
    },
    {
        "city": "Coron",
        "country": "Philippines",
        "region": "Asia",
        "main_attraction": "Kayangan Lake",
        "target_keyword": "best private island hopping tour packages from Coron"
    },
    {
        "city": "Semporna",
        "country": "Malaysia",
        "region": "Asia",
        "main_attraction": "Sipadan Island",
        "target_keyword": "top scuba diving water bungalows in Semporna Sabah"
    },
    {
        "city": "Kampot",
        "country": "Cambodia",
        "region": "Asia",
        "main_attraction": "Bokor National Park",
        "target_keyword": "best french colonial boutique hotels near Kampot river"
    },
    {
        "city": "Koh Rong",
        "country": "Cambodia",
        "region": "Asia",
        "main_attraction": "Long Set Beach",
        "target_keyword": "best luxury white sand beach resorts in Koh Rong island"
    },
    {
        "city": "Luang Prabang",
        "country": "Laos",
        "region": "Asia",
        "main_attraction": "Kuang Si Falls",
        "target_keyword": "best heritage boutique eco hotels in Luang Prabang"
    },
    {
        "city": "Si Phan Don",
        "country": "Laos",
        "region": "Asia",
        "main_attraction": "Mekong River Waterfalls",
        "target_keyword": "best relaxing riverfront guesthouses in 4000 islands Laos"
    },
    {
        "city": "Hoi An",
        "country": "Vietnam",
        "region": "Asia",
        "main_attraction": "Hoi An Ancient Town",
        "target_keyword": "romantic lantern view boutique hotels near Hoi An ancient town"
    },
    {
        "city": "Chiang Rai",
        "country": "Thailand",
        "region": "Asia",
        "main_attraction": "White Temple (Wat Rong Khun)",
        "target_keyword": "best serene eco lodges near White Temple Chiang Rai"
    }
]

# ==========================================
# 3. PROSES PRODUKSI HTML & SITEMAP
# ==========================================
link_halaman = ""
xml_urls = f"  <url>\n    <loc>{BASE_URL}</loc>\n  </url>\n"

current_time = datetime.datetime.now()
updated_str = current_time.strftime("Updated %B %Y")

for item in data_destinasi:
    # Memaksimalkan SEO: Nama file pakai target_keyword yang sudah di format
    slug_keyword = item['target_keyword'].lower().replace(' ', '-').replace(',', '')
    nama_file = f"{slug_keyword}.html"
    
    # Capitalize the target keyword for aesthetics in HTML
    judul_seo = item['target_keyword'].title()
    
    link_halaman += f'<li><a href="{nama_file}">{judul_seo} ({item["city"]}, {item["country"]})</a></li>\n'
    
    # Tambah ke daftar sitemap XML
    xml_urls += f"  <url>\n    <loc>{BASE_URL}{nama_file}</loc>\n  </url>\n"
    
    kota_encoded = item['city'].replace(' ', '%20')
    if item['region'].lower() == 'asia':
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
    <meta name="description" content="Looking for the {item['target_keyword']}? Discover the ultimate guide to visiting {item['main_attraction']} in {item['city']}, {item['country']} ({updated_str}).">
    <title>{judul_seo} | {item['city']} Travel Guide</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color: #f9f9f9; color: #333; }}
        .container {{ max-width: 800px; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); margin: 0 auto; }}
        h1 {{ color: #2c3e50; font-size: 28px; }}
        .highlight {{ font-weight: bold; color: #e67e22; }}
        .btn-box {{ background: #2ecc71; padding: 15px; text-align: center; border-radius: 5px; margin: 20px 0; }}
        .btn-box a {{ color: white; text-decoration: none; font-weight: bold; font-size: 18px; display: block; }}
        .hotel-box {{ background: #fff3cd; padding: 20px; border-left: 5px solid #ffc107; margin-top: 25px; border-radius: 5px; }}
        .hotel-box h2 {{ margin-top: 0; color: #856404; font-size: 22px; }}
    </style>
    <!-- TRAVELPAYOUTS DRIVE SCRIPT -->
    <script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1">
    (function () {{
        var script = document.createElement("script");
        script.async = 1;
        script.src = 'https://emrldtp.com/NTQ4NDMx.js?t=548431';
        document.head.appendChild(script);
    }})();
    </script>
</head>
<body>
    <div class="container">
        <h1>{judul_seo}</h1>
        <p>Planning a trip to <span class="highlight">{item['city']}, {item['country']}</span>? If you are searching for the <strong>{item['target_keyword']}</strong>, you have come to the right place. {updated_str} updates show that this destination is becoming a top-tier choice for smart travelers!</p>
        
        <h2>Must-Visit: {item['main_attraction']}</h2>
        <p>Your trip won't be complete without experiencing the iconic <strong>{item['main_attraction']}</strong>. It is the heart of {item['city']} and offers an unforgettable adventure for both solo travelers and families.</p>
        
        <div class="hotel-box">
            <h2>Where to Stay: Top Recommendations</h2>
            <p>To get the best experience and easy access to {item['main_attraction']}, securing your accommodation early is crucial.</p>
            <div class="btn-box" style="background: #e74c3c; margin-bottom: 5px;">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow">Check Room Availability on {hotel_brand} ↗</a>
            </div>
            <p style="font-size: 12px; color: #7f8c8d; text-align: center; margin-top: 0;">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <h2>Tours & Local Experiences</h2>
        <p>Maximize your journey by booking local guided tours. Discover hidden gems around {item['city']} and skip the lines.</p>
        
        <div class="btn-box" style="background: #3498db;">
            <a href="{LINK_AFFILIATE_TOUR}" target="_blank" rel="nofollow">Check Best Activities & Tours HERE ↗</a>
        </div>

        <hr>
        <p><a href="index.html">← Back to Global Travel Guide Portal</a></p>
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
    <title>Global Travel Guide Portal | The Insider Tips</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; background-color: #f4f4f9; }}
        .container {{ max-width: 900px; background: white; padding: 30px; border-radius: 8px; margin: 0 auto; box-shadow: 0 0 10px rgba(0,0,0,0.05); }}
        h1 {{ color: #333; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin: 15px 0; padding: 15px; background: #fdfdfd; border-left: 5px solid #2ecc71; transition: 0.3s; }}
        li:hover {{ background: #f0fdf4; border-left: 5px solid #27ae60; }}
        a {{ color: #2ecc71; text-decoration: none; font-size: 18px; font-weight: bold; display: block; }}
        a:hover {{ color: #27ae60; }}
    </style>
    <!-- TRAVELPAYOUTS DRIVE SCRIPT -->
    <script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1">
    (function () {{
        var script = document.createElement("script");
        script.async = 1;
        script.src = 'https://emrldtp.com/NTQ4NDMx.js?t=548431';
        document.head.appendChild(script);
    }})();
    </script>
</head>
<body>
    <div class="container">
        <h1>Welcome to the Global Travel Guide Portal</h1>
        <p>Discover insider travel guides, hidden gems, and the best affordable stays worldwide.</p>
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

print("========================================")
print("✅ SITEMAP GENERATED: File sitemap.xml berhasil dibuat!")
print("✅ 30 HALAMAN EMAS BERHASIL DICETAK!")
print("========================================")