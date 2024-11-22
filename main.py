import requests

def main():
    r = requests.get("https://google.com")
    print(f"statuss {r.status_code}")

if __name__ == "__main__":
    main()
