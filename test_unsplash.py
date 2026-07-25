import subprocess
import re

def get_unsplash_image(keyword):
    cmd = ['curl', '-s', f'https://unsplash.com/s/photos/{keyword.replace(" ", "-")}']
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        urls = re.findall(r'https://images.unsplash.com/photo-[a-zA-Z0-9-]+', result.stdout)
        unique_urls = list(dict.fromkeys(urls))
        return unique_urls[:2]
    except Exception as e:
        return str(e)

print(get_unsplash_image("tokyo landmark"))
