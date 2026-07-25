import csv
import subprocess
import re
import json

cities = []
with open("destinasi.csv", mode="r", encoding="utf-8") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cities.append(row['city'])

city_dict = {}
for city in cities:
    keyword_query = f"{city} landmark travel".replace(" ", "-")
    cmd = ['curl', '-s', f'https://unsplash.com/s/photos/{keyword_query}']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        urls = re.findall(r'https://images.unsplash.com/photo-[a-zA-Z0-9-]+', result.stdout)
        if urls:
            city_dict[city] = urls[0]
        else:
            city_dict[city] = 'https://images.unsplash.com/photo-1488646953014-85cb44e25828'
        print(f"Fetched {city}")
    except Exception as e:
        city_dict[city] = 'https://images.unsplash.com/photo-1488646953014-85cb44e25828'

with open("city_dict.json", "w") as f:
    json.dump(city_dict, f, indent=4)
print("DONE")
