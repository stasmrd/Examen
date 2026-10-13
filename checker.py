import requests

SITES = [
    # Pagini obișnuite (Părțile 2, 3 și 4)
    "https://example.com",
    "https://httpbin.org/html",
    "https://httpbin.org/json",
    "https://httpbin.org/status/200",
    "https://httpbin.org/redirect/1",
    "https://httpbin.org/delay/2",
    # Pagini care eșuează
    "https://httpbin.org/status/404",
    "https://httpbin.org/status/500",
    "https://httpbin.org/delay/10",
    "http://this-site-does-not-exist.invalid",
    # Anteturi de securitate (Partea 5)
    "https://httpbin.org/response-headers?X-Frame-Options=DENY&X-Content-Type-Options=nosniff",
    "https://httpbin.org/response-headers?x-frame-options=DENY",
    # Răspunde aleatoriu cu 200 sau 500 (Partea 6)
    "https://httpbin.org/status/200,500",
]

SECURITY_HEADERS = [
    "Strict-Transport-Security",
    "Content-Security-Policy",
    "X-Frame-Options",
    "X-Content-Type-Options",
]

def build_url(host, path):
    """Returnează o adresă completă, de exemplu https://example.com/login."""
    adresa = host + path
    return adresa

def is_https(url):
    """Returnează True dacă adresa începe cu https://, altfel False."""
    print(url, True)
    print(url, False)
    return url


def show_response(url):
    """Trimite un GET la url și afisează statusul și Content-Type."""
    response = requests.get(url)
    content_type = response.headers.get("content-type")
    print(f"Status: {response.status_code}")
    print(f"Content-Type: {response.headers.get('Content-Type')}")
    return response


def check_site(url):
    """Returnează un dicționar cu: status, content_type, length, server."""
    try:
        response = requests.get(url, timeout=5)
        return {
            "status": response.status_code,
            "content_type": response.headers.get("Content-Type"),
            "length": len(response.content),
            "server": response.headers.get("Server", "unknown")
        }
    except Exception as e:
        return {"status": None, "Eroare": str(e)}

def scan_sites():
    """Verifică toate site-urile din SITES, afișează-le pe cele care merg și un rezumat."""
    pass


def check_headers(url):
    """Returnează un dicționar cu: present, missing, score."""
    pass


def retry_check(url, attempts=3):
    """Încearcă de cel mult `attempts` ori; returnează un dicționar cu: status, attempts."""
    pass

print("--------------")
print(build_url("google.com", "/home"))
print("--------------")
is_https("google.com")
print("--------------")
print(show_response("https://cybercor.org"))
print("--------------")
print(check_site("https://cybercor.org"))
print("--------------")