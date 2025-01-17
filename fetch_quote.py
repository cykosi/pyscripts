import requests

def fetch_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()
            quote = data[0]["q"]
            author = data[0]["a"]
            return f'\033[1;34m"{quote}"\033[0m\n\033[1;32m  - {author}\033[0m'
        else:
            return "Could not fetch a quote at this time. Please try again later."
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print(fetch_quote())
