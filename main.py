import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://www.beautypackaging.com/contents/view_online-exclusives/2023-05-01/top-100-beauty-companies/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)

    soup = BeautifulSoup(response.text, "html.parser")

    resultados = []

    filas = soup.select("table tr")

    print("Filas:", len(filas))

    for fila in filas:
        columnas = fila.find_all("td")

        if len(columnas) >= 2:
            marca = columnas[1].get_text(strip=True)

            resultados.append({
                "marca": marca
            })

    return resultados


def main():
    marcas = buscar_marcas()

    print("\nLeads encontrados:\n")

    for m in marcas[:20]:
        print(m)


if __name__ == "__main__":
    main()
