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
    region_color = "#0071C2" if item['region'].lower() == 'europe' else "#008009"
    trending_badge = '<span class="trending-badge">Trending 🔥</span>' if (len(item['city']) + len(item['country'])) % 3 == 0 else ''
    link_halaman += f'''
            <a href="{nama_file}" class="card-link">
                <div class="card">
                    <div class="badges-row">
                        <span class="region-badge" style="background-color: {region_color};">{item['region']}</span>
                        {trending_badge}
                    </div>
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
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #FFFFFF; margin: 0; padding: 15px; color: #222222; line-height: 1.6; }}
        .container {{ max-width: 800px; background: #FFFFFF; padding: 20px; margin: 0 auto; border: 1px solid #DDDDDD; }}
        h1 {{ color: #000000; font-size: 26px; font-weight: 900; margin-bottom: 10px; line-height: 1.2; }}
        h2 {{ color: #000000; font-size: 20px; font-weight: 800; margin-top: 35px; margin-bottom: 15px; border-bottom: 3px solid #0071C2; padding-bottom: 5px; }}
        .badge {{ background-color: #008009; color: #FFFFFF; padding: 8px 16px; font-weight: 800; font-size: 14px; display: inline-block; margin-bottom: 20px; border-radius: 4px; box-shadow: 0 2px 4px rgba(0,128,9,0.4); text-transform: uppercase; }}
        .highlight {{ font-weight: 800; color: #CC0000; }}
        
        .fomo-alert {{ background-color: #FFFDE7; color: #B71C1C; padding: 15px; border: 2px solid #FBC02D; margin: 25px 0; font-weight: 800; font-size: 16px; border-radius: 4px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }}
        
        .hotel-tier {{ border: 2px solid #E5E5E5; margin-bottom: 20px; padding: 20px; background: #FAFAFA; border-radius: 6px; }}
        .hotel-tier h3 {{ margin-top: 0; color: #333333; font-size: 16px; margin-bottom: 10px; font-weight: 800; text-transform: uppercase; }}
        .hotel-name {{ font-size: 20px; font-weight: 900; color: #0071C2; margin-bottom: 15px; display: block; line-height: 1.2; }}
        
        .btn-box {{ margin: 15px 0; }}
        .btn-box a {{ display: block; color: #FFFFFF; text-decoration: none; font-weight: 900; font-size: 18px; padding: 18px 10px; text-align: center; border-radius: 8px; box-shadow: 0 6px 0px rgba(0,0,0,0.2); transition: transform 0.1s, box-shadow 0.1s; text-transform: uppercase; }}
        .btn-box a:active {{ transform: translateY(4px); box-shadow: 0 2px 0px rgba(0,0,0,0.2); }}
        
        .micro-copy {{ font-size: 12px; color: #555555; text-align: center; margin-top: 10px; font-weight: 700; display: flex; align-items: center; justify-content: center; gap: 5px; }}
        
        .tour-section {{ margin-top: 40px; padding-top: 20px; border-top: 2px solid #E5E5E5; }}
        hr {{ border: 0; border-top: 2px solid #E5E5E5; margin: 30px 0; }}
        .back-btn {{ color: #0071C2; text-decoration: underline; font-weight: 800; font-size: 16px; }}
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
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; background-color: #FFFFFF; margin: 0; padding: 20px; color: #111111; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 10px; }}
        h1 {{ text-align: center; font-size: 28px; font-weight: 900; color: #000000; margin-bottom: 5px; }}
        .subtitle {{ text-align: center; color: #444444; font-size: 16px; margin-bottom: 30px; font-weight: 600; }}
        .grid-container {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; }}
        .card-link {{ text-decoration: none; color: inherit; display: block; }}
        .card {{ background: #FFFFFF; border: 2px solid #E2E2E2; border-radius: 8px; padding: 15px; position: relative; box-shadow: 0 4px 6px rgba(0,0,0,0.05); transition: border-color 0.2s; }}
        .card:hover {{ border-color: #0071C2; }}
        .card h3 {{ margin: 5px 0; font-size: 18px; font-weight: 800; color: #0071C2; }}
        .card p {{ margin: 0; color: #333333; font-size: 14px; font-weight: 600; }}
        .badges-row {{ display: flex; gap: 8px; margin-bottom: 8px; }}
        .region-badge {{ padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 700; color: #FFFFFF; text-transform: uppercase; }}
        .trending-badge {{ background-color: #CC0000; color: #FFFFFF; padding: 3px 8px; border-radius: 4px; font-size: 12px; font-weight: 700; text-transform: uppercase; animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ transform: scale(1); }} 50% {{ transform: scale(1.05); }} 100% {{ transform: scale(1); }} }}
        @media (max-width: 600px) {{ .grid-container {{ grid-template-columns: 1fr; }} }}
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