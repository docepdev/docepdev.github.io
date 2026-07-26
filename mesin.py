import csv
import glob
import os
import re

# ==========================================
# 1. DATABASE GAMBAR (SHANGHAI & TAINAN FIXED)
# ==========================================
CITY_IMAGES = {
    "Positano": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Mykonos": "https://images.unsplash.com/photo-1601581875309-fafbf2d3ed3a?auto=format&fit=crop&w=1200&q=80",
    "Grenada": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1200&q=80",
    "Costa Smeralda": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
    "Florence": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
    "Rome": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
    "Tulum": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1200&q=80",
    "Koh Samui": "https://images.unsplash.com/photo-1537956965359-7573183d1f57?auto=format&fit=crop&w=1200&q=80",
    "Ubud": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=1200&q=80",
    "Tainan": "https://images.unsplash.com/photo-1552993873-0dd1110e025f?auto=format&fit=crop&w=1200&q=80",
    "Bali": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=80",
    "Tokyo": "https://images.unsplash.com/photo-1503899036084-c55cdd92da26?auto=format&fit=crop&w=1200&q=80",
    "Paris": "https://images.unsplash.com/photo-1502602898657-3e91760cbb34?auto=format&fit=crop&w=1200&q=80",
    "New York": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?auto=format&fit=crop&w=1200&q=80",
    "Seoul": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=1200&q=80",
    "Singapore": "https://images.unsplash.com/photo-1525625293386-3f8f99389edd?auto=format&fit=crop&w=1200&q=80",
    "Amsterdam": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "London": "https://images.unsplash.com/photo-1513635269975-59663e0ac1ad?auto=format&fit=crop&w=1200&q=80",
    "Kuala Lumpur": "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=1200&q=80",
    "Berlin": "https://images.unsplash.com/photo-1560969184-10fe8719e047?auto=format&fit=crop&w=1200&q=80",
    "Barcelona": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
    "Maldives": "https://images.unsplash.com/photo-1514282401047-d79a71a590e8?auto=format&fit=crop&w=1200&q=80",
    "Kyoto": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?auto=format&fit=crop&w=1200&q=80",
    "Phuket": "https://images.unsplash.com/photo-1589394815804-964ed0be2eb5?auto=format&fit=crop&w=1200&q=80",
    "Hanoi": "https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=1200&q=80",
    "Manila": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?auto=format&fit=crop&w=1200&q=80",
    "Taipei": "https://images.unsplash.com/photo-1508248467877-aed3237d2826?auto=format&fit=crop&w=1200&q=80",
    "Bangkok": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
    "Sydney": "https://images.unsplash.com/photo-1506973035872-a4ec16b8e8d9?auto=format&fit=crop&w=1200&q=80",
    "Hong Kong": "https://images.unsplash.com/photo-1506970845246-18f21d533b20?auto=format&fit=crop&w=1200&q=80",
    "Shanghai": "https://images.unsplash.com/photo-1549693578-cbc29953b05a?auto=format&fit=crop&w=1200&q=80", # SHANGHAI FIXED
    "Dubai": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
    "Istanbul": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?auto=format&fit=crop&w=1200&q=80",
    "Cairo": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80",
    "Cape Town": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1200&q=80",
    "Los Angeles": "https://images.unsplash.com/photo-1580655653885-65763b2597d0?auto=format&fit=crop&w=1200&q=80",
    "Rio De Janeiro": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1200&q=80",
    "Toronto": "https://images.unsplash.com/photo-1517090504586-fde19ea6066f?auto=format&fit=crop&w=1200&q=80",
    "Zurich": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?auto=format&fit=crop&w=1200&q=80",
    "Milan": "https://images.unsplash.com/photo-1513581166391-887a96ddeafd?auto=format&fit=crop&w=1200&q=80",
    "Madrid": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
    "Vienna": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?auto=format&fit=crop&w=1200&q=80",
    "Prague": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Menton": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Colmar": "https://images.unsplash.com/photo-1588880331179-bc9b93a8cb5e?auto=format&fit=crop&w=1200&q=80",
    "Matera": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
    "Alberobello": "https://images.unsplash.com/photo-1528114039593-4366cc08227d?auto=format&fit=crop&w=1200&q=80",
    "Zell Am See": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Bled": "https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?auto=format&fit=crop&w=1200&q=80",
    "Sintra": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?auto=format&fit=crop&w=1200&q=80",
    "Ronda": "https://images.unsplash.com/photo-1561632669-6e0e99818828?auto=format&fit=crop&w=1200&q=80",
    "Mostar": "https://images.unsplash.com/photo-1565008447742-97f6f38c985c?auto=format&fit=crop&w=1200&q=80",
    "Kotor": "https://images.unsplash.com/photo-1565008447742-97f6f38c985c?auto=format&fit=crop&w=1200&q=80",
    "Piran": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
    "Hvar": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Rovinj": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Gdansk": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Wroclaw": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Brasov": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Sibiu": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Cesky Krumlov": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Karlovy Vary": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Mechelen": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Ghent": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Dinant": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Giethoorn": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Maastricht": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Bergen": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Reine": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Rovaniemi": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Porvoo": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Tallinn": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Riga": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Vilnius": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Trakai": "https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?auto=format&fit=crop&w=1200&q=80",
    "Ohrid": "https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?auto=format&fit=crop&w=1200&q=80",
    "Plovdiv": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Veliko Tarnovo": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Novi Sad": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Subotica": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Eger": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Szeged": "https://images.unsplash.com/photo-1541849546-216549ae216d?auto=format&fit=crop&w=1200&q=80",
    "Graz": "https://images.unsplash.com/photo-1516550893923-42d28e5677af?auto=format&fit=crop&w=1200&q=80",
    "Innsbruck": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Thun": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Grindelwald": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Interlaken": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Chamonix": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
    "Taormina": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Volterra": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
    "Lucca": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
    "Cadiz": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
    "Cuenca": "https://images.unsplash.com/photo-1539037116277-4db20889f2d4?auto=format&fit=crop&w=1200&q=80",
    "Tropea": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Coron": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?auto=format&fit=crop&w=1200&q=80",
}
DEFAULT_IMAGE = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80"

def get_image_and_shortname(raw_title):
    title_clean = raw_title.replace("liburan-ke-", "").replace(".html", "").replace("-", " ").title().strip()
    for loc, img_url in CITY_IMAGES.items():
        if loc.lower() in title_clean.lower():
            return loc, img_url
            
    short_title = title_clean
    if len(title_clean.split()) > 3:
        match = re.search(r'(?:In|Near|For)\s+([A-Za-z\s]+)$', title_clean, re.IGNORECASE)
        if match:
            short_title = match.group(1).strip()
    return short_title, DEFAULT_IMAGE


# ==========================================
# 2. TEMPLATE ARTIKEL DINAMIS (MENERIMA DATA DARI CSV)
# ==========================================
ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{full_title}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; color: #1e293b; background: #f8fafc; line-height: 1.6; }}
        h1, h2, h3 {{ font-family: 'Playfair Display', serif; color: #0f172a; }}
        
        .hero {{
            position: relative;
            min-height: 65vh;
            background: linear-gradient(180deg, rgba(15,23,42,0.3) 0%, rgba(15,23,42,0.85) 100%), url('{image_url}') center/cover no-repeat;
            display: flex;
            align-items: flex-end;
            padding: 3rem 1.5rem;
            color: #ffffff;
        }}
        .hero-content {{ max-width: 900px; margin: 0 auto; width: 100%; }}
        .badge-bar {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1rem; }}
        .badge {{ background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); padding: 0.35rem 0.85rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border: 1px solid rgba(255,255,255,0.3); }}
        .hero h1 {{ font-size: 2.75rem; font-weight: 800; line-height: 1.2; margin-bottom: 1.5rem; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
        
        .btn-cta {{
            background: #2563eb;
            color: #ffffff;
            font-weight: 700;
            padding: 1rem 2rem;
            border-radius: 10px;
            text-decoration: none;
            display: inline-block;
            transition: all 0.2s ease;
            border: none;
            cursor: pointer;
            font-size: 1.1rem;
        }}
        .btn-cta:hover {{ background: #1d4ed8; transform: translateY(-2px); }}
        
        .container {{ max-width: 900px; margin: 3rem auto; padding: 0 1.5rem; font-size: 1.1rem; color: #334155; }}
        
        /* Styling untuk konten asli dari CSV/HTML lu */
        .container h2, .container h3 {{ margin-top: 2rem; margin-bottom: 1rem; }}
        .container p {{ margin-bottom: 1.25rem; }}
        .container ul, .container ol {{ margin-bottom: 1.5rem; padding-left: 1.5rem; }}
        .container a {{ color: #2563eb; font-weight: 600; text-decoration: none; }}
        .container a:hover {{ text-decoration: underline; }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
        }}
    </style>
</head>
<body>

    <header class="hero">
        <div class="hero-content">
            <div class="badge-bar">
                <span class="badge" style="background: #f59e0b; color: #000; border: none;">Verified 2026 Guide</span>
            </div>
            <!-- JUDUL ASLI DARI CSV DIMASUKKAN KE SINI -->
            <h1>{full_title}</h1>
            
            <!-- TOMBOL CTA MEMAKAI LINK AFILIASI ASLI DARI CSV -->
            <a href="{affiliate_link}" target="_blank" class="btn-cta">Check Dates & Reserve</a>
        </div>
    </header>

    <main class="container">
        <!-- KONTEN ASLI DARI CSV DIMASUKKAN KE SINI -->
        {csv_content}
    </main>

</body>
</html>
"""

# ==========================================
# 3. TEMPLATE INDEX.HTML (MENAMPILKAN JUDUL PENDEK AGAR RAPI)
# ==========================================
INDEX_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Travel Guide Portal | Verified Destination Guides</title>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Plus+Jakarta+Sans:wght@500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; background: #0f172a; color: #f8fafc; padding: 3rem 1.5rem; }}
        .header {{ text-align: center; max-width: 800px; margin: 0 auto 3rem auto; }}
        .header h1 {{ font-family: 'Playfair Display', serif; font-size: 3rem; margin-bottom: 1rem; color: #ffffff; }}
        .header p {{ color: #94a3b8; font-size: 1.1rem; }}
        
        .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; max-width: 1200px; margin: 0 auto; }}
        .card {{
            position: relative;
            height: 350px;
            border-radius: 16px;
            overflow: hidden;
            text-decoration: none;
            box-shadow: 0 10px 15px -3px rgba(0,0,0,0.3);
            transition: transform 0.3s ease;
        }}
        .card:hover {{ transform: translateY(-5px); }}
        .card-bg {{ position: absolute; inset: 0; background-size: cover; background-position: center; }}
        .card-overlay {{
            position: absolute;
            inset: 0;
            background: linear-gradient(180deg, rgba(0,0,0,0) 30%, rgba(15,23,42,0.95) 100%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 1.5rem;
        }}
        .card-title {{ font-family: 'Playfair Display', serif; font-size: 1.5rem; color: #ffffff; font-weight: 700; line-height: 1.25; }}
        .card-sub {{ font-size: 0.8rem; color: #38bdf8; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.25rem; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Global Travel Guide Portal</h1>
        <p>Discover hand-curated, Local Expert Verified travel guides to the world's most extraordinary destinations.</p>
    </div>
    <div class="grid">
        {cards_html}
    </div>
</body>
</html>
"""

# ==========================================
# 4. SKRIP UTAMA: MEMBACA CSV DAN MENCETAK ULANG
# ==========================================
def generate_site_from_csv():
    print("🚀 Menganalisis file CSV untuk menarik data asli...")
    
    csv_files = glob.glob("*.csv")
    if not csv_files:
        print("❌ File CSV tidak ditemukan di folder ini! Pastikan file CSV lu ada.")
        return
        
    csv_file = csv_files[0]
    print(f"📄 Membaca data dari: {csv_file}")
    
    cards = []
    
    with open(csv_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        
        # Mendeteksi nama kolom secara otomatis (karena format CSV bisa beda-beda)
        headers = reader.fieldnames
        title_col = next((c for c in headers if c.lower() in ['title', 'keyword', 'destination', 'kota']), headers[0])
        link_col = next((c for c in headers if c.lower() in ['url', 'link', 'affiliate_link', 'affiliate url', 'travelpayouts']), None)
        content_col = next((c for c in headers if c.lower() in ['content', 'body', 'artikel', 'description', 'text']), None)
        
        count = 0
        for row in reader:
            full_title = row.get(title_col, "").strip()
            if not full_title:
                continue
                
            # Tarik Link Afiliasi dari CSV (jika kosong, baru pakai default)
            affiliate_link = row.get(link_col, "").strip() if link_col else ""
            if not affiliate_link:
                affiliate_link = "https://emrldtp.com/cl/YOUR_DEFAULT_CODE"
                
            # Tarik Konten Asli dari CSV
            csv_content = row.get(content_col, "").strip() if content_col else ""
            if not csv_content:
                csv_content = f"<p>Welcome to our verified guide for <strong>{full_title}</strong>. Check availability and prices by clicking the reserve button above to get the best deals for your upcoming trip.</p>"
            
            # Buat Nama File (Slug)
            filename = f"{full_title.lower().replace(' ', '-').replace(',', '').replace('?', '')}.html"
            
            # Dapatkan Gambar dan Nama Pendek untuk Kartu Beranda
            short_name, img_url = get_image_and_shortname(full_title)
            
            # 1. Cetak Ulang Artikel (Memasukkan Judul, Konten, & Link Asli!)
            html_content = ARTICLE_TEMPLATE.format(
                full_title=full_title,
                image_url=img_url,
                affiliate_link=affiliate_link,
                csv_content=csv_content
            )
            with open(filename, "w", encoding="utf-8") as out_f:
                out_f.write(html_content)
                
            # 2. Susun Kartu Beranda
            cards.append(f"""
            <a href="{filename}" class="card">
                <div class="card-bg" style="background-image: url('{img_url}');"></div>
                <div class="card-overlay">
                    <span class="card-sub">Verified Guide</span>
                    <h2 class="card-title">{short_name}</h2>
                </div>
            </a>
            """)
            count += 1
            
    # 3. Cetak Beranda (index.html)
    index_html = INDEX_TEMPLATE.format(cards_html="\n".join(cards))
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)
        
    print(f"✅ FINISH! Berhasil mencetak ulang {count} halaman menggunakan Data & Link Afiliasi ASLI dari CSV!")

if __name__ == "__main__":
    generate_site_from_csv()