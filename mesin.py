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
    region_color = "#3498db" if item['region'].lower() == 'europe' else "#2ecc71"
    link_halaman += f'''
            <a href="{nama_file}" class="card-link">
                <div class="card">
                    <span class="region-badge" style="background-color: {region_color};">{item['region']}</span>
                    <h3>{item["city"]}</h3>
                    <p>{item["country"]}</p>
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; margin: 0; padding: 40px 20px; color: #334155; line-height: 1.7; }}
        .container {{ max-width: 800px; background: #ffffff; padding: 40px 50px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); margin: 0 auto; border: 1px solid #f1f5f9; }}
        h1 {{ color: #0f172a; font-size: 2.25rem; font-weight: 700; margin-bottom: 15px; line-height: 1.2; }}
        h2 {{ color: #1e293b; font-size: 1.5rem; margin-top: 40px; margin-bottom: 20px; border-bottom: 2px solid #e2e8f0; padding-bottom: 10px; }}
        .badge {{ background: linear-gradient(135deg, #f59e0b, #d97706); color: white; padding: 6px 14px; border-radius: 9999px; font-weight: 600; font-size: 0.85rem; display: inline-block; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(245, 158, 11, 0.3); }}
        .highlight {{ font-weight: 600; color: #ea580c; }}
        
        .fomo-alert {{ background: linear-gradient(to right, #fffbeb, #fef3c7); color: #92400e; padding: 16px 20px; border-left: 4px solid #f59e0b; margin: 30px 0; font-weight: 500; font-size: 0.95rem; border-radius: 0 8px 8px 0; display: flex; align-items: center; gap: 10px; }}
        
        .hotel-tier {{ border: 1px solid #e2e8f0; border-radius: 12px; margin-bottom: 24px; padding: 25px; background: #ffffff; transition: transform 0.2s, box-shadow 0.2s; position: relative; overflow: hidden; }}
        .hotel-tier:hover {{ transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); border-color: #cbd5e1; }}
        .hotel-tier h3 {{ margin-top: 0; color: #334155; font-size: 1.15rem; margin-bottom: 15px; font-weight: 600; }}
        .hotel-name {{ font-size: 1.2rem; font-weight: 700; color: #2563eb; margin-bottom: 15px; display: block; }}
        
        .btn-box {{ padding: 14px; text-align: center; border-radius: 8px; margin: 20px 0 8px 0; transition: opacity 0.2s; }}
        .btn-box:hover {{ opacity: 0.9; }}
        .btn-box a {{ color: white; text-decoration: none; font-weight: 600; font-size: 1.05rem; display: block; }}
        .micro-copy {{ font-size: 0.75rem; color: #64748b; text-align: center; margin-top: 0; font-weight: 500; }}
        
        .tour-section {{ margin-top: 40px; padding-top: 30px; border-top: 1px solid #e2e8f0; }}
        hr {{ border: 0; border-top: 1px solid #e2e8f0; margin: 40px 0; }}
        .back-btn {{ color: #3b82f6; text-decoration: none; font-weight: 600; display: inline-flex; align-items: center; gap: 5px; transition: color 0.2s; }}
        .back-btn:hover {{ color: #2563eb; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Budget Travel Guide to {item['city']} ({updated_str})</h1>
        <div class="badge">✓ Local Expert Verified</div>
        
        <p>Looking for a vacation with <strong>perfect</strong> weather? <span class="highlight">{item['city']}</span> is the perfect destination for you!</p>
        
        <h2>Must-Visit Attractions</h2>
        <p>Don't miss the chance to explore <strong>{item['main_attraction']}</strong>, the ultimate iconic spots in the city.</p>
        
        <div class="fomo-alert">
            🔥 <strong>Urgent:</strong> 87% of accommodations in {item['city']} for upcoming dates are already booked! Secure your stay immediately.
        </div>
        
        <h2>Where to Stay in {item['city']} (Top Recommended Areas: City Center)</h2>
        
        <div class="hotel-tier">
            <h3>⭐ Premium Luxury (5-Star Experience)</h3>
            <span class="hotel-name">{item.get('hotel_premium', 'Luxury Hotel')}</span>
            <div class="btn-box" style="background: {hotel_btn_color};">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="hotel-tier">
            <h3>👍 Best Value (Mid-Range & Comfort)</h3>
            <span class="hotel-name">{item.get('hotel_midrange', 'Mid-Range Hotel')}</span>
            <div class="btn-box" style="background: {hotel_btn_color};">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="hotel-tier">
            <h3>🎒 Budget Friendly (Smart Budget Options)</h3>
            <span class="hotel-name">{item.get('hotel_budget', 'Budget Hostel')}</span>
            <div class="btn-box" style="background: {hotel_btn_color};">
                <a href="{LINK_AFFILIATE_HOTEL}" target="_blank" rel="nofollow">Check Availability on {hotel_brand} ↗</a>
            </div>
            <p class="micro-copy">🔒 Best Price Guarantee & Free Cancellation on Most Rooms via {hotel_brand}</p>
        </div>

        <div class="tour-section">
            <h2>Estimated Budget & Expenses</h2>
            <p>To fully enjoy your trip here, we highly recommend preparing a budget around <span class="highlight">$500 - $1,500</span>.</p>
            
            <div class="btn-box" style="background: {tour_btn_color};">
                <a href="{LINK_AFFILIATE_TOUR}" target="_blank" rel="nofollow">Check Best Activities & Tours HERE ↗</a>
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; margin: 0; padding: 40px 20px; color: #1e293b; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
        h1 {{ text-align: center; font-size: 2.75rem; color: #0f172a; margin-bottom: 10px; font-weight: 700; }}
        .subtitle {{ text-align: center; color: #64748b; margin-bottom: 40px; font-size: 1.1rem; }}
        .grid-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; }}
        .card-link {{ text-decoration: none; color: inherit; }}
        .card {{ background: #ffffff; border-radius: 12px; padding: 24px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03); transition: transform 0.3s ease, box-shadow 0.3s ease; border: 1px solid #e2e8f0; position: relative; }}
        .card:hover {{ transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05); }}
        .card h3 {{ margin: 10px 0 5px 0; font-size: 1.25rem; color: #0f172a; font-weight: 700; }}
        .card p {{ margin: 0; color: #64748b; font-size: 0.95rem; }}
        .region-badge {{ display: inline-block; padding: 4px 10px; border-radius: 9999px; font-size: 0.75rem; font-weight: 600; color: white; margin-bottom: 8px; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Global Travel Guide Portal</h1>
        <p class="subtitle">Discover Local Expert Verified travel guides to major cities worldwide.</p>
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