# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://www.shopify.com/blog/skincare-brands"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    for link in soup.find_all("a"):
        texto = link.get_text(strip=True)
        href = link.get("href")

        if texto and href and "http" in href:
            resultados.append({
                "marca": texto,
                "web": href
            })

    return resultados


def main():
    marcas = buscar_marcas()

    print("Leads encontrados:\n")

    for m in marcas[:10]:
        print(m)


if __name__ == "__main__":
    main()
