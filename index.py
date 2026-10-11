from urllib.parse import quote
from pathlib import Path

html = Path("index2.html").read_text(encoding="utf-8")
url = "data:text/html," + quote(html, safe="")

print(url)
print("URL length:", len(url))
print("HTML size:", len(html.encode("utf-8")))