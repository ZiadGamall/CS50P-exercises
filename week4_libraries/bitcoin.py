# Bitcoin Price Checker — Fetches real-time Bitcoin price and calculates the total for a given amount.

import sys
import requests

if len(sys.argv) < 2:
    print("Missing command-line argument")
    sys.exit()

try:
    num = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
    sys.exit()

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=c8d0f03a3942351f7ce1531822a78c6fb5651fd70cdfba4a7dee6c8d01fb6dba").json()
    price = float(response["data"]["priceUsd"])
except requests.RequestException:
    sys.exit()

print(f"${price * num:,.4f}")