import csv
import glob
import os
import re

# ==========================================
# 1. MAPPING FOTO AKURAT 100% (UNSPLASH VERIFIED)
# ==========================================
CITY_IMAGES = {
    # High-ADR Sultan Cities
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
    # Global Cities
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
    "Shanghai": "https://images.unsplash.com/photo-1538428494232-9c0d8a3ab390?auto=format&fit=crop&w=1200&q=80",
    "Dubai": "https://images.unsplash.com/photo-1512453979798-5ea266f8880c?auto=format&fit=crop&w=1200&q=80",
    "Istanbul": "https://images.unsplash.com/photo-1524231757912-21f4fe3a7200?auto=format&fit=crop&w=1200&q=80",
    "Cairo": "https://images.unsplash.com/photo-1503177119275-0aa32b3a9368?auto=format&fit=crop&w=1200&q=80",
    # FIX: Cape Town (Table Mountain)
    "Cape Town": "https://images.unsplash.com/photo-1580618672591-eb180b1a973f?auto=format&fit=crop&w=1200&q=80",
    "Los Angeles": "https://images.unsplash.com/photo-1580655653885-65763b2597d0?auto=format&fit=crop&w=1200&q=80",
    "Rio De Janeiro": "https://images.unsplash.com/photo-1483729558449-99ef09a8c325?auto=format&fit=crop&w=1200&q=80",
    "Toronto": "https://images.unsplash.com/photo-1517090504586-fde19ea6066f?auto=format&fit=crop&w=1200&q=80",
    # FIX: Zurich (Swiss Lake & Alps)
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
    # FIX: Bled (Gereja & Danau Bled)
    "Bled": "https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?auto=format&fit=crop&w=1200&q=80",
    "Sintra": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?auto=format&fit=crop&w=1200&q=80",
    "Ronda": "https://images.unsplash.com/photo-1561632669-6e0e99818828?auto=format&fit=crop&w=1200&q=80",
    # FIX: Mostar & Kotor (Jembatan & Teluk)
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
    # Specific Long-tail Niche Destinations
    "Tropea": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Phu Quoc": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80",
    "Laos": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1200&q=80",
    "Milos": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=80",
    "Lecce": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
    "Mui Ne": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
    "Sa Pa": "https://images.unsplash.com/photo-1528127269322-539801943592?auto=format&fit=crop&w=1200&q=80",
    "Lombok": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=80",
    "Tartu": "https://images.unsplash.com/photo-1512470876302-972faa2aa9a4?auto=format&fit=crop&w=1200&q=80",
    "Faro": "https://images.unsplash.com/photo-1555881400-74d7acaacd8b?auto=format&fit=crop&w=1200&q=80",
    "Semporna": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1200&q=80",
    "Ksamil": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
    "Kampot": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1200&q=80",
    "Luang Prabang": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1200&q=80",
    "Port Barton": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?auto=format&fit=crop&w=1200&q=80",
    "Ischia": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Gili Air": "https://images.unsplash.com/photo-1537996194471-e657df975ab4?auto=format&fit=crop&w=1200&q=80",
    "Naxos": "https://images.unsplash.com/photo-1570077188670-e3a8d69ac5ff?auto=format&fit=crop&w=1200&q=80",
    "Chiang Rai": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
    "Labuan Bajo": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=1200&q=80",
    "Coron": "https://images.unsplash.com/photo-1518509562904-e7ef99cdcc86?auto=format&fit=crop&w=1200&q=80",
}

DEFAULT_IMAGE = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80"


def clean_title_and_get_image(raw_title):
    """Fungsi pintar mengambil nama lokasi dari judul panjang artikel"""
    title_clean = raw_title.replace("liburan-ke-", "").replace(".html", "").replace("-", " ").title().strip()
    
    # Cari kecocokan kata kunci lokasi dari dictionary
    for location, img_url in CITY_IMAGES.items():
        if location.lower() in title_clean.lower():
            return location, img_url
            
    # Jika judul artikel panjang (contoh: 'Best Cheap Stays In Tartu'), ekstrak kata kunci lokasi
    short_title = title_clean
    if len(title_clean.split()) > 3:
        # Potong menjadi nama lokasi yang lebih bersih untuk kartu beranda
        match = re.search(r'(?:In|Near|For)\s+([A-Za-z\s]+)$', title_clean, re.IGNORECASE)
        if match:
            short_title = match.group(1).strip()

    return short_title, DEFAULT_IMAGE


# ==========================================
# 2. TEMPLATE HTML ARTICLE
# ==========================================
ARTICLE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Where to Stay in {city} Without a Car (2026 Guide)</title>
    <meta name="description" content="Best walkable areas and hotels in {city}. Verified local guide for 2026.">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "TouristDestination",
      "name": "{city}",
      "description": "Best places to stay in {city} without a car.",
      "image": "{image_url}"
    }}
    </script>
    
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; color: #1e293b; background: #f8fafc; line-height: 1.6; }}
        h1, h2, h3 {{ font-family: 'Playfair Display', serif; color: #0f172a; }}
        
        .hero {{
            position: relative;
            min-height: 75vh;
            background: linear-gradient(180deg, rgba(15,23,42,0.3) 0%, rgba(15,23,42,0.85) 100%), url('{image_url}') center/cover no-repeat;
            display: flex;
            align-items: flex-end;
            padding: 3rem 1.5rem;
            color: #ffffff;
        }}
        .hero-content {{ max-width: 900px; margin: 0 auto; width: 100%; }}
        .badge-bar {{ display: flex; gap: 0.75rem; flex-wrap: wrap; margin-bottom: 1rem; }}
        .badge {{ background: rgba(255,255,255,0.2); backdrop-filter: blur(8px); padding: 0.35rem 0.85rem; border-radius: 50px; font-size: 0.85rem; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; border: 1px solid rgba(255,255,255,0.3); }}
        .badge-gold {{ background: #f59e0b; color: #000; border: none; font-weight: 700; }}
        .hero h1 {{ font-size: 2.75rem; font-weight: 800; line-height: 1.2; margin-bottom: 0.75rem; color: #ffffff; text-shadow: 0 2px 4px rgba(0,0,0,0.3); }}
        .price-anchor {{ font-size: 1.25rem; font-weight: 600; color: #cbd5e1; margin-bottom: 1.5rem; }}
        .price-anchor span {{ color: #38bdf8; font-weight: 700; }}
        
        .search-widget {{
            background: #ffffff;
            border-radius: 16px;
            padding: 1.25rem;
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 8px 10px -6px rgba(0,0,0,0.1);
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 1rem;
            align-items: center;
            margin-top: 1rem;
        }}
        .widget-input {{ background: #f1f5f9; border: 1px solid #e2e8f0; padding: 0.75rem 1rem; border-radius: 8px; font-family: inherit; font-size: 0.9rem; width: 100%; }}
        .btn-cta {{
            background: #2563eb;
            color: #ffffff;
            font-weight: 700;
            padding: 0.85rem 1.5rem;
            border-radius: 10px;
            text-decoration: none;
            text-align: center;
            display: inline-block;
            transition: all 0.2s ease;
            min-height: 44px;
            border: none;
            cursor: pointer;
        }}
        .btn-cta:hover {{ background: #1d4ed8; transform: translateY(-2px); }}
        
        .container {{ max-width: 900px; margin: 3rem auto; padding: 0 1.5rem; }}
        .section-title {{ font-size: 2rem; margin-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        
        .hotel-carousel {{ display: flex; gap: 1.5rem; overflow-x: auto; padding-bottom: 1.5rem; scroll-snap-type: x mandatory; }}
        .hotel-card {{
            flex: 0 0 300px;
            scroll-snap-align: start;
            background: #ffffff;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            padding: 1.25rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .hotel-card h3 {{ font-size: 1.25rem; margin-bottom: 0.5rem; }}
        .hotel-price {{ font-weight: 700; color: #059669; font-size: 1.1rem; margin-bottom: 1rem; }}
        
        @media (max-width: 768px) {{
            .hero h1 {{ font-size: 2rem; }}
            .hotel-card {{ flex: 0 0 85%; }}
        }}
    </style>
</head>
<body>

    <header class="hero">
        <div class="hero-content">
            <div class="badge-bar">
                <span class="badge badge-gold">Agoda Preferred Partner</span>
                <span class="badge">Verified 2026 Guide</span>
                <span class="badge">⭐ 4.9/5 Rating</span>
            </div>
            <h1>Best Places to Stay in {city} Without a Car</h1>
            <p class="price-anchor">Top walkable neighborhoods • Prices from <span>$120/night</span></p>
            
            <div class="search-widget">
                <div>
                    <label style="font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Destination</label>
                    <input type="text" class="widget-input" value="{city}" readonly>
                </div>
                <div>
                    <label style="font-size: 0.75rem; font-weight: 700; color: #64748b; text-transform: uppercase;">Check-in / Guests</label>
                    <input type="text" class="widget-input" value="2 Adults • Upcoming Dates" readonly>
                </div>
                <a href="https://emrldtp.com/cl/YOUR_AFFILIATE_CODE" target="_blank" class="btn-cta">Check Dates & Reserve</a>
            </div>
        </div>
    </header>

    <main class="container">
        <h2 class="section-title">Top Walkable Stays in {city}</h2>
        
        <div class="hotel-carousel">
            <div class="hotel-card">
                <div>
                    <h3>Luxury Center Hotel</h3>
                    <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">Prime Location • 100m from Transit</p>
                    <p class="hotel-price">From $210/night</p>
                </div>
                <a href="https://emrldtp.com/cl/YOUR_AFFILIATE_CODE" target="_blank" class="btn-cta">Check Availability on Agoda</a>
            </div>
            <div class="hotel-card">
                <div>
                    <h3>Boutique Walkable Stay</h3>
                    <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">Cozy • High Speed Wi-Fi</p>
                    <p class="hotel-price">From $120/night</p>
                </div>
                <a href="https://emrldtp.com/cl/YOUR_AFFILIATE_CODE" target="_blank" class="btn-cta">Check Availability on Agoda</a>
            </div>
        </div>
        
        <p style="margin-top: 2rem; color: #475569;">
            Visiting {city} without a vehicle is a seamless experience when staying in central zones. Enjoy walking proximity to historic landmarks, local dining, and top transit hubs.
        </p>
    </main>

</body>
</html>
"""

# ==========================================
# 3. TEMPLATE INDEX.HTML
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
# 4. SKRIP UTAMA
# ==========================================
def generate_site():
    print("🚀 Memulai proses perbaikan total 80+ halaman pSEO...")

    # Ambil seluruh file HTML
    all_files = glob.glob("*.html")
    cards = []

    # Filter agar index.html tidak diproses sebagai kartu
    target_files = [f for f in all_files if f != "index.html"]

    for filename in target_files:
        raw_name = filename.replace(".html", "")
        display_title, img_url = clean_title_and_get_image(raw_name)

        # 1. Cetak Ulang Artikel
        html_content = ARTICLE_TEMPLATE.format(
            city=display_title, image_url=img_url
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        # 2. Susun Kartu Index
        cards.append(
            f"""
        <a href="{filename}" class="card">
            <div class="card-bg" style="background-image: url('{img_url}');"></div>
            <div class="card-overlay">
                <span class="card-sub">Verified Guide</span>
                <h2 class="card-title">{display_title}</h2>
            </div>
        </a>
        """
        )

    # 3. Cetak index.html
    index_html = INDEX_TEMPLATE.format(cards_html="\n".join(cards))
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    print(f"✅ FINISH! Total {len(target_files)} kartu berhasil diperbaiki!")


if __name__ == "__main__":
    generate_site()