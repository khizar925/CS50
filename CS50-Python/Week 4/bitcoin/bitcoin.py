import sys
import requests

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        price_per_btc = data["bpi"]["USD"]["rate_float"]
    except requests.RequestException:
        sys.exit("Error fetching data from API")

    total_cost = bitcoins * price_per_btc
    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
