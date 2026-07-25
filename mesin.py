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
    nama_file = f"liburan-ke-{item['city'].lower().replace(' ', '-')}.html"
    kota_url = item['city'].replace(' ', '%20')
    link_halaman += f'''
            <a href="{nama_file}" class="card-link">
                <div class="card" style="background-image: url('https://source.unsplash.com/featured/?{kota_url},landmark');">
                    <div class="card-gradient">
                        <span class="region-badge">{item['region']}</span>
                        <h3>{item["city"]}</h3>
                        <p>{item["country"]}</p>
                    </div>
                </div>
            </a>
'''
    
    # Tambah ke daftar sitemap XML
    xml_urls += f"  <url>\n    <loc>{BASE_URL}{nama_file}</loc>\n  </url>\n"
    
    kota_encoded = item['city'].replace(' ', '%20')
    if item['region'].lower() == 'asia':
        LINK_AFFILIATE_HOTEL = f"https://www.agoda.com/partners/partnerlanding.aspx?pcs=1&cid={ID_AGODA}&city={kota_encoded}"
        LINK_AFFILIATE_TOUR = f"https://www.klook.com/search/result/?query={kota_encoded}&aid={ID_KLOOK}"
        hotel_brand = "Agoda"
        hotel_btn_color = "#e74c3c" # Merah
        tour_btn_color = "#2ecc71" # Hijau
    else:
        LINK_AFFILIATE_HOTEL = f"https://www.booking.com/searchresults.html?city={kota_encoded}&aid={ID_BOOKING}"
        LINK_AFFILIATE_TOUR = f"https://www.getyourguide.com/s/?q={kota_encoded}&partner_id={ID_GETYOURGUIDE}"
        hotel_brand = "Booking.com"
        hotel_btn_color = "#003580" # Biru tua
        tour_btn_color = "#2ecc71" # Hijau
        
    konten_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Budget travel guide to {item['city']}, {item['country']}. Explore attractions, costs, and hotels ({updated_str}).">
    <title>Budget Travel Guide to {item['city']} ({updated_str})</title>
    
    <!-- Travelpayouts Tracking Script -->
    <script nowprocket data-noptimize="1" data-cfasync="false" data-wpfc-render="false" seraph-accel-crit="1" data-no-defer="1">
      (function () {{
          var script = document.createElement("script");
          script.async = 1;
          script.src = 'https://emrldtp.com/NTQ4NDMx.js?t=548431';
          document.head.appendChild(script);
      }})();
    </script>
    
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: #FAFAFA; margin: 0; padding: 0; color: #4A4A4A; line-height: 1.8; }}
        
        .hero-banner {{ height: 60vh; background-size: cover; background-position: center; display: flex; align-items: center; justify-content: center; text-align: center; padding: 0 20px; }}
        .hero-content h1 {{ font-family: 'Playfair Display', serif; font-size: 3.5rem; color: #FFFFFF; margin: 0; text-shadow: 0 4px 12px rgba(0,0,0,0.4); letter-spacing: 1px; }}
        .hero-subtitle {{ color: #F0F0F0; font-size: 1.1rem; font-weight: 500; margin-top: 15px; text-transform: uppercase; letter-spacing: 3px; }}
        
        .container {{ max-width: 800px; background: #FFFFFF; padding: 60px 80px; margin: -60px auto 60px auto; border-radius: 12px; box-shadow: 0 20px 40px rgba(0,0,0,0.04); position: relative; z-index: 10; }}
        h2 {{ font-family: 'Playfair Display', serif; color: #2C3E50; font-size: 1.8rem; margin-top: 40px; margin-bottom: 20px; }}
        
        .badge {{ background-color: #F8F9FA; color: #2C3E50; padding: 8px 16px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin-bottom: 25px; border-radius: 30px; border: 1px solid #E9ECEF; letter-spacing: 1px; }}
        .highlight {{ font-weight: 600; color: #2C3E50; }}
        
        .fomo-alert {{ background-color: #F8FAFC; color: #475569; padding: 18px 24px; border-left: 4px solid #94A3B8; margin: 30px 0; font-weight: 500; font-size: 1rem; border-radius: 0 8px 8px 0; display: flex; align-items: center; gap: 12px; }}
        
        .hotel-tier {{ border: 1px solid #F1F5F9; margin-bottom: 30px; padding: 35px; background: #FFFFFF; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.02); transition: transform 0.3s ease, box-shadow 0.3s ease; }}
        .hotel-tier:hover {{ transform: translateY(-5px); box-shadow: 0 12px 25px rgba(0,0,0,0.04); }}
        .hotel-tier h3 {{ margin-top: 0; color: #64748B; font-size: 0.9rem; margin-bottom: 10px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; }}
        .hotel-name {{ font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #0F172A; margin-bottom: 25px; display: block; }}
        
        .btn-box {{ margin: 20px 0; }}
        .btn-box a {{ display: block; color: #FFFFFF; text-decoration: none; font-weight: 600; font-size: 1rem; padding: 16px 20px; text-align: center; border-radius: 8px; transition: opacity 0.3s; letter-spacing: 1px; }}
        .btn-box a:hover {{ opacity: 0.9; }}
        
        .micro-copy {{ font-size: 0.75rem; color: #94A3B8; text-align: center; margin-top: 15px; font-weight: 500; }}
        
        .tour-section {{ margin-top: 50px; padding-top: 40px; border-top: 1px solid #F1F5F9; text-align: center; }}
        hr {{ border: 0; border-top: 1px solid #F1F5F9; margin: 50px 0; }}
        .back-btn {{ color: #64748B; text-decoration: none; font-weight: 500; display: inline-flex; align-items: center; gap: 8px; transition: color 0.3s; }}
        .back-btn:hover {{ color: #0F172A; }}
        
        @media (max-width: 768px) {{ .container {{ padding: 40px 25px; margin-top: -30px; }} .hero-content h1 {{ font-size: 2.5rem; }} }}
    </style>
</head>
<body>
    <div class="hero-banner" style="background-image: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.7)), url('https://source.unsplash.com/featured/?{kota_url},landscape');">
        <div class="hero-content">
            <h1>Budget Travel Guide to {item['city']}</h1>
            <p class="hero-subtitle">Updated {updated_str}</p>
        </div>
    </div>
    <div class="container">
        <div class="badge">✓ Local Expert Verified</div>
        
        <p>Looking for a vacation with <strong>perfect</strong> weather? <span class="highlight">{item['city']}</span> is the perfect destination for you!</p>
        
        <h2>Must-Visit Attractions</h2>
        <p>Don't miss the chance to explore <strong>{item['main_attraction']}</strong>, the ultimate iconic spots in the city.</p>
        
        <div class="fomo-alert">
            <span style="font-size: 1.2em;">🔥</span> <strong>Urgent:</strong> 87% of accommodations in {item['city']} for upcoming dates are already booked! Secure your stay immediately.
        </div>
        
        <h2>Where to Stay in {item['city']} (Top Recommended Areas: City Center)</h2>
        
        <div class="hotel-tier">
            <h3>⭐ Premium Luxury (5-Star Experience)</h3>
            <span class="hotel-name">{item.get('hotel_premium', 'Luxury Hotel')}</span>
            <div class="btn-box">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow" style="background-color: {hotel_btn_color};">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="hotel-tier">
            <h3>👍 Best Value (Mid-Range & Comfort)</h3>
            <span class="hotel-name">{item.get('hotel_midrange', 'Mid-Range Hotel')}</span>
            <div class="btn-box">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow" style="background-color: {hotel_btn_color};">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="hotel-tier">
            <h3>🎒 Budget Friendly (Smart Budget Options)</h3>
            <span class="hotel-name">{item.get('hotel_budget', 'Budget Hostel')}</span>
            <div class="btn-box">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow" style="background-color: {hotel_btn_color};">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="tour-section">
            <h2>Estimated Budget & Expenses</h2>
            <p>To fully enjoy your trip here, we highly recommend preparing a budget around <span class="highlight">$500 - $1,500</span>.</p>
            
            <div class="btn-box">
                <a href="{LINK_AFFILIATE_TOUR}" target="_blank" rel="nofollow" style="background-color: {tour_btn_color};">Check Best Activities & Tours HERE ↗</a>
            </div>
        </div>

        <hr>
        <p><a href="index.html" class="back-btn">← Back to Homepage</a></p>
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
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Plus+Jakarta+Sans:wght@400;500;600&display=swap');
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background-color: #FAFAFA; margin: 0; padding: 0; color: #4A4A4A; }}
        
        .header-wrapper {{ background: #FFFFFF; padding: 60px 20px; text-align: center; border-bottom: 1px solid #F1F5F9; margin-bottom: 60px; }}
        h1 {{ font-family: 'Playfair Display', serif; font-size: 2.8rem; color: #0F172A; margin: 0 0 15px 0; letter-spacing: 0.5px; }}
        .subtitle {{ color: #64748B; font-size: 1.1rem; margin: 0; font-weight: 400; max-width: 600px; margin: 0 auto; line-height: 1.6; }}
        
        .container {{ max-width: 1400px; margin: 0 auto; padding: 0 40px 80px 40px; }}
        .grid-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 30px; }}
        
        .card-link {{ text-decoration: none; color: inherit; display: block; outline: none; }}
        .card {{ height: 420px; background-size: cover; background-position: center; border-radius: 16px; position: relative; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.08); transition: transform 0.4s cubic-bezier(0.165, 0.84, 0.44, 1), box-shadow 0.4s ease; }}
        .card:hover {{ transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.15); }}
        
        .card-gradient {{ position: absolute; bottom: 0; left: 0; right: 0; height: 60%; background: linear-gradient(to top, rgba(0,0,0,0.85) 0%, rgba(0,0,0,0.4) 60%, transparent 100%); display: flex; flex-direction: column; justify-content: flex-end; padding: 30px; }}
        
        .card h3 {{ font-family: 'Playfair Display', serif; font-size: 1.8rem; color: #FFFFFF; margin: 0 0 5px 0; letter-spacing: 0.5px; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
        .card p {{ margin: 0; color: #E2E8F0; font-size: 0.95rem; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; }}
        
        .region-badge {{ display: inline-block; padding: 6px 12px; border-radius: 30px; font-size: 0.7rem; font-weight: 600; color: #FFFFFF; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.4); align-self: flex-start; backdrop-filter: blur(4px); }}
        
        @media (max-width: 768px) {{ .container {{ padding: 0 20px 60px 20px; }} .card {{ height: 350px; }} h1 {{ font-size: 2.2rem; }} }}
    </style>
</head>
<body>
    <div class="header-wrapper">
        <h1>Global Travel Guide Portal</h1>
        <p class="subtitle">Discover hand-curated, Local Expert Verified travel guides to the world's most extraordinary destinations.</p>
    </div>
    <div class="container">
        <div class="grid-container">
            {link_halaman}
        </div>
    </div>
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(beranda_html)

sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{xml_urls}</urlset>"""

with open("sitemap.xml", "w") as f:
    f.write(sitemap_xml)

print("---")
print("SITEMAP & HTML GENERATED SUCCESSFULY!")
print("---")