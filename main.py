import requests
from bs4 import BeautifulSoup

def buscar_marcas():
    url = "https://www.beautypackaging.com/contents/view_online-exclusives/2023-05-01/top-100-beauty-companies/"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "es-ES,es;q=0.9,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print("STATUS:", response.status_code)

        if response.status_code != 200:
            print("Bloqueado o error:", response.status_code)
            return []

    except requests.exceptions.Timeout:
        print("⏱️ Timeout: la web tardó demasiado")
        return []

    except requests.exceptions.RequestException as e:
        print("❌ Error en la petición:", e)
        return []

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
