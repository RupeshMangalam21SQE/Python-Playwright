import threading
import requests

urls = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/posts/1"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"{url[:30]}... => {len(response.text)} characters")

threads = []
for url in urls:
    t = threading.Thread(target=fetch_url, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
