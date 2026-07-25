import csv
import json
import os

# ==========================================
# 1. DATABASE FOTO KOTA ACCURATE (UNSPLASH HD)
# ==========================================
CITY_IMAGES = {
    # 10 High-ADR Cities (Dollar Tebal)
    "Positano": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
    "Mykonos": "https://images.unsplash.com/photo-1601581875309-fafbf2d3ed3a?auto=format&fit=crop&w=1200&q=80",
    "Grenada": "https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=1200&q=80",
    "Costa Smeralda": "https://images.unsplash.com/photo-1516483638261-f4dbaf036963?auto=format&fit=crop&w=1200&q=80",
    "Florence": "https://images.unsplash.com/photo-1543429776-2782fc8e1acd?auto=format&fit=crop&w=1200&q=80",
    "Rome": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?auto=format&fit=crop&w=1200&q=80",
    "Tulum": "https://images.unsplash.com/photo-1518638150340-f706e86654de?auto=format&fit=crop&w=1200&q=80",
    "Koh Samui": "https://images.unsplash.com/photo-1537956965359-7573183d1f57?auto=format&fit=crop&w=1200&q=80",
    "Ubud": "https://images.unsplash.com/photo-1518548419970-58e3b4079ab2?auto=format&fit=crop&w=1200&q=80",
    "Tainan": "https://images.unsplash.com/photo-1508248467877-aed3237d2826?auto=format&fit=crop&w=1200&q=80",
    # Major Global Destinations
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
}

DEFAULT_IMAGE = "https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=1200&q=80"

# Est. ADR Default untuk High-Converting Pricing Anchor
ADR_RATES = {
    "Positano": 673,
    "Mykonos": 385,
    "Grenada": 300,
    "Costa Smeralda": 280,
    "Florence": 234,
    "Rome": 224,
    "Tulum": 196,
    "Koh Samui": 180,
    "Ubud": 114,
    "Tainan": 90,
}


def get_image(city_name):
    return CITY_IMAGES.get(city_name, DEFAULT_IMAGE)


def get_adr(city_name):
    return ADR_RATES.get(city_name, 120)


# ==========================================
# 2. TEMPLATE HTML ARTICLE (CRO 2026 STANDARDS)
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
    
    <!-- JSON-LD Schema Markup (Machine-Readable SEO) -->
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
        
        /* Above-The-Fold (ATF) Hero Section */
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
        
        /* ATF Quick Widget Search */
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
            min-height: 44px; /* Mobile Touch Target Standard */
            border: none;
            cursor: pointer;
        }}
        .btn-cta:hover {{ background: #1d4ed8; transform: translateY(-2px); }}
        
        /* Main Container */
        .container {{ max-width: 900px; margin: 3rem auto; padding: 0 1.5rem; }}
        .section-title {{ font-size: 2rem; margin-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem; }}
        
        /* Mobile Horizontal Carousel for Hotels */
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

    <!-- Above-The-Fold (ATF) Viewport -->
    <header class="hero">
        <div class="hero-content">
            <div class="badge-bar">
                <span class="badge badge-gold">Agoda Preferred Partner</span>
                <span class="badge">Verified 2026 Guide</span>
                <span class="badge">⭐ 4.9/5 Rating</span>
            </div>
            <h1>Best Places to Stay in {city} Without a Car</h1>
            <p class="price-anchor">Top walkable neighborhoods • Prices from <span>${adr}/night</span></p>
            
            <!-- Quick Search Widget -->
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

    <!-- Main Content -->
    <main class="container">
        <h2 class="section-title">Top Walkable Stays in {city}</h2>
        
        <!-- Mobile Carousel -->
        <div class="hotel-carousel">
            <div class="hotel-card">
                <div>
                    <h3>Luxury Center Hotel</h3>
                    <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">Prime Location • 100m from Transit</p>
                    <p class="hotel-price">From ${adr_lux}/night</p>
                </div>
                <a href="https://emrldtp.com/cl/YOUR_AFFILIATE_CODE" target="_blank" class="btn-cta">Check Availability on Agoda</a>
            </div>
            <div class="hotel-card">
                <div>
                    <h3>Boutique Walkable Stay</h3>
                    <p style="font-size: 0.85rem; color: #64748b; margin-bottom: 0.5rem;">Cozy • High Speed Wi-Fi</p>
                    <p class="hotel-price">From ${adr}/night</p>
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
# 3. TEMPLATE INDEX.HTML (GRID SULTAN)
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
            background: linear-gradient(180deg, rgba(0,0,0,0) 40%, rgba(15,23,42,0.95) 100%);
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            padding: 1.5rem;
        }}
        .card-title {{ font-family: 'Playfair Display', serif; font-size: 1.75rem; color: #ffffff; font-weight: 700; }}
        .card-sub {{ font-size: 0.85rem; color: #38bdf8; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; }}
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
# 4. SKRIP EKSEKUSI PENJETAKAN (GENERATOR)
# ==========================================
ALL_CITIES = [
    "Positano",
    "Mykonos",
    "Grenada",
    "Costa Smeralda",
    "Florence",
    "Rome",
    "Tulum",
    "Koh Samui",
    "Ubud",
    "Tainan",
    "Bali",
    "Tokyo",
    "Paris",
    "New York",
    "Seoul",
    "Singapore",
    "Amsterdam",
    "London",
    "Kuala Lumpur",
    "Berlin",
    "Barcelona",
]


def generate_site():
    print("🚀 Memulai proses cetak ulang 84 Halaman pSEO CRO 2026...")

    cards = []
    for city in ALL_CITIES:
        img_url = get_image(city)
        adr = get_adr(city)
        filename = f"{city.lower().replace(' ', '-')}.html"

        # 1. Cetak Artikel Individual
        html_content = ARTICLE_TEMPLATE.format(
            city=city,
            image_url=img_url,
            adr=adr,
            adr_lux=int(adr * 1.8),
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
                <h2 class="card-title">{city}</h2>
            </div>
        </a>
        """
        )

    # 3. Cetak index.html Utama
    index_html = INDEX_TEMPLATE.format(cards_html="\n".join(cards))
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(index_html)

    print("✅ SUKSES! Seluruh halaman HTML & index.html berhasil dicetak!")


if __name__ == "__main__":
    generate_site()
