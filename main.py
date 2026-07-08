import requests

def main():
    url = "https://en.wikipedia.org/wiki/List_of_cosmetics_brands"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)
    print("HTML length:", len(response.text))

    print("\n--- INICIO HTML ---\n")
    print(response.text[:2000])
    print("\n--- FIN HTML ---\n")


if __name__ == "__main__":
    main()
