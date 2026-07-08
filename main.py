# -*- coding: utf-8 -*-
print("VERSION NUEVA")
import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://wikipedia.org"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    for li in soup.select("div.div-col li"):
        nombre = li.get_text(strip=True)

        if nombre:
            resultados.append({
                "marca": nombre
            })

    return resultados


def main():
    marcas = buscar_marcas()

    print("Leads encontrados:\n")

    for m in marcas[:10]:
        print(m)


if __name__ == "__main__":
    main()
