# config.py

URLS = {
    "dev": "https://www.saucedemo.com/",
    "staging": "https://staging.saucedemo.com/",
    "prod": "https://prod.saucedemo.com/"
}

DEFAULT_ENV = "dev"

def get_base_url(env=DEFAULT_ENV):
    return URLS.get(env.lower(), URLS[DEFAULT_ENV])