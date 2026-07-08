import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://en.wikipedia.org/w/index.php?title=List_of_cosmetics_brands&printable=yes"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    elementos = soup.select("li")

    print("Elementos encontrados:", len(elementos))

    for li in elementos:
        texto = li.get_text(strip=True)

        # filtro básico para evitar basura
        if texto and len(texto) < 50:
            resultados.append({
                "marca": texto
            })

    return resultados


def main():
    marcas = buscar_marcas()

    print("\nLeads encontrados:\n")

    for m in marcas[:15]:
        print(m)


if __name__ == "__main__":
    main()
