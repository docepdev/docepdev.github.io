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
    {"city": "Matera", "country": "Italy", "region": "Europe", "main_attraction": "Sassi di Matera", "target_keyword": "best luxury cave hotels in Matera Sassi"},
    {"city": "Tropea", "country": "Italy", "region": "Europe", "main_attraction": "Spiaggia della Rotonda (Tropea Beach)", "target_keyword": "affordable beachfront cliff hotels in Tropea"},
    {"city": "Ksamil", "country": "Albania", "region": "Europe", "main_attraction": "Ksamil Islands", "target_keyword": "best apartments with sea view in Ksamil Riviera"},
    {"city": "Kotor", "country": "Montenegro", "region": "Europe", "main_attraction": "Bay of Kotor", "target_keyword": "top boutique guesthouses near Kotor Old Town"},
    {"city": "Budva", "country": "Montenegro", "region": "Europe", "main_attraction": "Budva Citadel", "target_keyword": "best luxury spa resorts in Budva Montenegro"},
    {"city": "Tartu", "country": "Estonia", "region": "Europe", "main_attraction": "Tartu Old Town Square", "target_keyword": "romantic boutique hotels in Tartu city center"},
    {"city": "Plovdiv", "country": "Bulgaria", "region": "Europe", "main_attraction": "Ancient Theatre of Philippopolis", "target_keyword": "cheap historical hotels in Plovdiv Old Town"},
    {"city": "Ghent", "country": "Belgium", "region": "Europe", "main_attraction": "Gravensteen Castle", "target_keyword": "top rated canal view hotels in Ghent center"},
    {"city": "Lecce", "country": "Italy", "region": "Europe", "main_attraction": "Piazza del Duomo", "target_keyword": "best traditional bed and breakfast in Lecce Puglia"},
    {"city": "Naxos", "country": "Greece", "region": "Europe", "main_attraction": "Portara (Temple of Apollo)", "target_keyword": "best quiet family beach resorts in Naxos island"},
    {"city": "Milos", "country": "Greece", "region": "Europe", "main_attraction": "Sarakiniko Beach", "target_keyword": "luxury whitewashed hotels with private pool in Milos"},
    {"city": "Riga", "country": "Latvia", "region": "Europe", "main_attraction": "House of the Black Heads", "target_keyword": "best affordable boutique hotels in Riga Old Town"},
    {"city": "Ischia", "country": "Italy", "region": "Europe", "main_attraction": "Aragonese Castle", "target_keyword": "best volcanic thermal spa hotels in Ischia Italy"},
    {"city": "Faro", "country": "Portugal", "region": "Europe", "main_attraction": "Ria Formosa Natural Park", "target_keyword": "cheap authentic guesthouses near Faro Algarve"},
    {"city": "Sibiu", "country": "Romania", "region": "Europe", "main_attraction": "Piata Mare (Large Square)", "target_keyword": "best medieval places to stay in Sibiu Transylvania"},
    {"city": "Labuan Bajo", "country": "Indonesia", "region": "Asia", "main_attraction": "Komodo National Park", "target_keyword": "luxury phinisi liveaboard tours Labuan Bajo"},
    {"city": "Lombok", "country": "Indonesia", "region": "Asia", "main_attraction": "Mount Rinjani", "target_keyword": "best quiet beachfront eco villas in south Lombok"},
    {"city": "Gili Air", "country": "Indonesia", "region": "Asia", "main_attraction": "Gili Air Coral Reefs", "target_keyword": "top sustainable diving resorts in Gili Air"},
    {"city": "Mui Ne", "country": "Vietnam", "region": "Asia", "main_attraction": "Red Sand Dunes", "target_keyword": "best kitesurfing beach resorts near Mui Ne"},
    {"city": "Sa Pa", "country": "Vietnam", "region": "Asia", "main_attraction": "Fansipan Mountain", "target_keyword": "best authentic mountain view homestays in Sa Pa"},
    {"city": "Phu Quoc", "country": "Vietnam", "region": "Asia", "main_attraction": "Sao Beach", "target_keyword": "luxury private family beachfront resorts Phu Quoc"},
    {"city": "Port Barton", "country": "Philippines", "region": "Asia", "main_attraction": "Port Barton Marine Park", "target_keyword": "affordable beachfront cottages in Port Barton Palawan"},
    {"city": "Coron", "country": "Philippines", "region": "Asia", "main_attraction": "Kayangan Lake", "target_keyword": "best private island hopping tour packages from Coron"},
    {"city": "Semporna", "country": "Malaysia", "region": "Asia", "main_attraction": "Sipadan Island", "target_keyword": "top scuba diving water bungalows in Semporna Sabah"},
    {"city": "Kampot", "country": "Cambodia", "region": "Asia", "main_attraction": "Bokor National Park", "target_keyword": "best french colonial boutique hotels near Kampot river"},
    {"city": "Koh Rong", "country": "Cambodia", "region": "Asia", "main_attraction": "Long Set Beach", "target_keyword": "best luxury white sand beach resorts in Koh Rong island"},
    {"city": "Luang Prabang", "country": "Laos", "region": "Asia", "main_attraction": "Kuang Si Falls", "target_keyword": "best heritage boutique eco hotels in Luang Prabang"},
    {"city": "Si Phan Don", "country": "Laos", "region": "Asia", "main_attraction": "Mekong River Waterfalls", "target_keyword": "best relaxing riverfront guesthouses in 4000 islands Laos"},
    {"city": "Hoi An", "country": "Vietnam", "region": "Asia", "main_attraction": "Hoi An Ancient Town", "target_keyword": "romantic lantern view boutique hotels near Hoi An ancient town"},
    {"city": "Chiang Rai", "country": "Thailand", "region": "Asia", "main_attraction": "White Temple (Wat Rong Khun)", "target_keyword": "best serene eco lodges near White Temple Chiang Rai"}
]

# ==========================================
# 3. PROSES PRODUKSI HTML & SITEMAP
# ==========================================
link_halaman = ""
xml_urls = f"  <url>\n    <loc>{BASE_URL}</loc>\n  </url>\n"

current_time = datetime.datetime.now()
updated_str = current_time.strftime("Updated %B %Y")

for item in data_destinasi:
    slug_keyword = item['target_keyword'].lower().replace(' ', '-').replace(',', '')
    nama_file = f"{slug_keyword}.html"
    judul_seo = item['target_keyword'].title()
    
    # Grid item untuk beranda (Desain Card/Kartu)
    link_halaman += f'''
    <a href="{nama_file}" class="card-link">
        <div class="card">
            <h3>{judul_seo}</h3>
            <p>📍 {item["city"]}, {item["country"]}</p>
        </div>
    </a>\n'''
    
    xml_urls += f"  <url>\n    <loc>{BASE_URL}{nama_file}</loc>\n  </url>\n"
    
    kota_encoded = item['city'].replace(' ', '%20')
    if item['region'].lower() == 'asia':
        LINK_AFFILIATE_HOTEL = f"https://www.agoda.com/partners/partnerlanding.aspx?pcs=1&cid={ID_AGODA}&city={kota_encoded}"
        LINK_AFFILIATE_TOUR = f"https://www.klook.com/search/result/?query={kota_encoded}&aid={ID_KLOOK}"
        hotel_brand = "Agoda"
        btn_color = "#e53935" # Merah Agoda
    else:
        LINK_AFFILIATE_HOTEL = f"https://www.booking.com/searchresults.html?city={kota_encoded}&aid={ID_BOOKING}"
        LINK_AFFILIATE_TOUR = f"https://www.getyourguide.com/s/?q={kota_encoded}&partner_id={ID_GETYOURGUIDE}"
        hotel_brand = "Booking.com"
        btn_color = "#003580" # Biru Booking

    # DESAIN ARTIKEL PREMIUM
    konten_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Looking for the {item['target_keyword']}? Discover the ultimate guide to visiting {item['main_attraction']} in {item['city']}, {item['country']} ({updated_str}).">
    <title>{judul_seo} | {item['city']} Travel Guide</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Poppins', sans-serif; line-height: 1.7; margin: 0; background-color: #f4f7f6; color: #2d3436; }}
        .header {{ background: linear-gradient(135deg, #0984e3, #74b9ff); color: white; padding: 60px 20px; text-align: center; }}
        .header h1 {{ margin: 0; font-size: 32px; font-weight: 700; text-shadow: 1px 1px 5px rgba(0,0,0,0.2); }}
        .header p {{ font-size: 16px; opacity: 0.9; margin-top: 10px; }}
        .container {{ max-width: 800px; background: white; padding: 40px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); margin: -30px auto 40px; position: relative; }}
        h2 {{ color: #0984e3; font-size: 24px; border-bottom: 2px solid #f1f2f6; padding-bottom: 10px; margin-top: 30px; }}
        .highlight {{ font-weight: 600; color: #d63031; background: #ffeaa7; padding: 2px 6px; border-radius: 4px; }}
        .hotel-box {{ background: #f8fbff; padding: 25px; border: 1px solid #dff9fb; border-left: 5px solid {btn_color}; margin-top: 30px; border-radius: 12px; }}
        .hotel-box h2 {{ margin-top: 0; color: {btn_color}; border: none; padding: 0; font-size: 20px; }}
        .btn-cta {{ display: block; background: {btn_color}; color: white; text-align: center; padding: 16px; border-radius: 8px; font-weight: 600; font-size: 18px; text-decoration: none; margin: 20px 0; transition: transform 0.3s ease, box-shadow 0.3s ease; }}
        .btn-cta:hover {{ transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.15); }}
        .btn-tour {{ background: #00b894; }}
        .back-link {{ display: inline-block; margin-top: 30px; color: #636e72; text-decoration: none; font-weight: 600; transition: color 0.3s; }}
        .back-link:hover {{ color: #0984e3; }}
        @media (max-width: 600px) {{ .container {{ margin: 10px; padding: 20px; }} .header h1 {{ font-size: 24px; }} }}
    </style>
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
    <div class="header">
        <h1>{judul_seo}</h1>
        <p>Expert Guide to {item['city']}, {item['country']} — {updated_str}</p>
    </div>
    
    <div class="container">
        <p>Planning a trip to <span class="highlight">{item['city']}, {item['country']}</span>? If you are searching for the <strong>{item['target_keyword']}</strong>, you have come to the right place. Recent trends show that this destination is becoming a top-tier choice for smart travelers seeking authenticity!</p>
        
        <h2>✨ Must-Visit: {item['main_attraction']}</h2>
        <p>Your trip won't be complete without experiencing the iconic <strong>{item['main_attraction']}</strong>. It is the cultural heart of {item['city']} and offers an unforgettable adventure for both solo travelers and families.</p>
        
        <div class="hotel-box">
            <h2>🏨 Where to Stay: Top Recommendations</h2>
            <p>To get the best experience and easy access to <strong>{item['main_attraction']}</strong>, securing your accommodation early is crucial before they sell out.</p>
            <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow" class="btn-cta">Check Room Availability on {hotel_brand} ↗</a>
            <p style="font-size: 12px; color: #636e72; text-align: center; margin-bottom: 0;">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <h2>🗺️ Tours & Local Experiences</h2>
        <p>Maximize your journey by booking local guided tours. Discover hidden gems around {item['city']}, skip the lines, and travel like a true insider.</p>
        <a href="{LINK_AFFILIATE_TOUR}" target="_blank" rel="nofollow" class="btn-cta btn-tour">Check Best Activities & Tours HERE ↗</a>

        <a href="index.html" class="back-link">← Back to Global Travel Portal</a>
    </div>
</body>
</html>"""
    
    with open(nama_file, "w") as f:
        f.write(konten_html)

# ==========================================
# 4. CETAK INDEX & SITEMAP.XML (DESAIN GRID)
# ==========================================
beranda_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Travel Guide Portal | Insider Tips</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ font-family: 'Poppins', sans-serif; background-color: #f4f7f6; margin: 0; color: #2d3436; }}
        .hero {{ background: #000 url('https://images.unsplash.com/photo-1436491865332-7a61a109cc05?q=80&w=2000&auto=format&fit=crop') center/cover; padding: 100px 20px; text-align: center; color: white; position: relative; }}
        .hero::before {{ content: ''; position: absolute; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); }}
        .hero-content {{ position: relative; z-index: 1; }}
        .hero h1 {{ font-size: 40px; margin-bottom: 10px; font-weight: 700; text-shadow: 2px 2px 10px rgba(0,0,0,0.5); }}
        .hero p {{ font-size: 18px; max-width: 600px; margin: 0 auto; opacity: 0.9; }}
        .container {{ max-width: 1100px; margin: -40px auto 50px; padding: 20px; position: relative; z-index: 2; }}
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 20px; }}
        .card-link {{ text-decoration: none; color: inherit; }}
        .card {{ background: white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); transition: transform 0.3s ease, box-shadow 0.3s ease; border-top: 4px solid #0984e3; height: 100%; box-sizing: border-box; }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.1); border-top: 4px solid #00b894; }}
        .card h3 {{ margin: 0 0 10px; font-size: 18px; color: #2d3436; line-height: 1.4; }}
        .card p {{ margin: 0; font-size: 14px; color: #636e72; font-weight: 600; }}
        @media (max-width: 600px) {{ .hero h1 {{ font-size: 30px; }} }}
    </style>
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
    <div class="hero">
        <div class="hero-content">
            <h1>Global Travel Guide Portal</h1>
            <p>Discover insider travel guides, hidden gems, and the best affordable stays worldwide.</p>
        </div>
    </div>
    <div class="container">
        <div class="grid">
            {link_halaman}
        </div>
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
print("✅ 30 HALAMAN PREMIUM BERHASIL DICETAK!")
print("========================================")