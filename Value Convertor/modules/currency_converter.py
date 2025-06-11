import requests

def convert_currency(amount, from_currency, to_currency):
    try:
        api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        data = response.json()

        rate = data["rates"].get(to_currency.upper())
        if rate:
            return round(amount * rate, 2)
        else:
            return "❌ Invalid target currency code."

    except requests.RequestException:
        return "❌ API request failed. Check your internet connection."
    except ValueError:
        return "❌ Invalid response received from the server."

