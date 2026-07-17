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
    link_halaman += f'<li><a href="{nama_file}">Budget Travel Guide to {item["city"]}</a></li>\n'
    
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
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; margin: 40px; background-color: #f0f2f5; color: #333; }}
        .container {{ max-width: 800px; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); margin: 0 auto; }}
        h1 {{ color: #2c3e50; font-size: 2.2em; margin-bottom: 5px; }}
        .badge {{ background: #f1c40f; color: #856404; padding: 5px 12px; border-radius: 20px; font-weight: bold; font-size: 14px; display: inline-block; margin-bottom: 20px; }}
        .highlight {{ font-weight: bold; color: #e67e22; }}
        
        .fomo-alert {{ background-color: #fff3cd; color: #856404; padding: 12px; border-left: 4px solid #ffc107; margin: 25px 0 15px 0; font-weight: bold; font-size: 15px; border-radius: 0 4px 4px 0; }}
        
        .hotel-tier {{ border: 1px solid #e1e8ed; border-radius: 8px; margin-bottom: 20px; padding: 20px; background: #fafbfc; }}
        .hotel-tier h3 {{ margin-top: 0; color: #2c3e50; border-bottom: 2px solid #e1e8ed; padding-bottom: 10px; margin-bottom: 15px; font-size: 1.2em; }}
        .hotel-name {{ font-size: 1.1em; font-weight: bold; color: #2980b9; margin-bottom: 15px; display: block; }}
        
        .btn-box {{ padding: 12px; text-align: center; border-radius: 6px; margin: 15px 0 5px 0; }}
        .btn-box a {{ color: white; text-decoration: none; font-weight: bold; font-size: 16px; display: block; }}
        .micro-copy {{ font-size: 12px; color: #7f8c8d; text-align: center; margin-top: 0; }}
        
        .tour-section {{ margin-top: 40px; padding-top: 20px; border-top: 1px solid #eee; }}
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

        <hr style="margin-top: 40px; border: 0; border-top: 1px solid #eee;">
        <p><a href="index.html" style="color: #3498db; text-decoration: none; font-weight: bold;">← Back to Homepage</a></p>
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
        body {{ font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; line-height: 1.6; margin: 40px; background-color: #f4f4f9; }}
        .container {{ max-width: 800px; background: white; padding: 40px; border-radius: 12px; margin: 0 auto; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        h1 {{ color: #2c3e50; text-align: center; margin-bottom: 30px; }}
        ul {{ list-style-type: none; padding: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 15px; }}
        li {{ padding: 15px; background: #fafbfc; border: 1px solid #e1e8ed; border-radius: 8px; border-left: 5px solid #2ecc71; transition: transform 0.2s; }}
        li:hover {{ transform: translateY(-3px); box-shadow: 0 4px 10px rgba(0,0,0,0.1); }}
        a {{ color: #2c3e50; text-decoration: none; font-size: 16px; font-weight: 600; display: block; }}
        @media (max-width: 600px) {{ ul {{ grid-template-columns: 1fr; }} }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Global Travel Guide Portal</h1>
        <p style="text-align: center; color: #7f8c8d; margin-bottom: 30px;">Discover Local Expert Verified travel guides to major cities worldwide.</p>
        <ul>
            {link_halaman}
        </ul>
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