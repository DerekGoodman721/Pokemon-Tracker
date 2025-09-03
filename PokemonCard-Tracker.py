# app.py
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = []  # This will hold the card info
    if request.method == "POST":
        cardNameInput = request.form.get("card_name", "")
        setNameInput = request.form.get("set_name", "")
        
        url = "https://api.pokemontcg.io/v2/cards"
        params = {
            "q": "name:" + cardNameInput + " AND set.name:\"" + setNameInput + "\""
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                for card in data["data"]:
                    card_name = card.get("name", "Unknown")
                    card_set = card.get("set", {}).get("name", "Unknown")
                    tcg_url = card.get("tcgplayer", {}).get("url", "N/A")
                    lowest_listing_url = tcg_url + "?sortBy=price&sortDirection=asc" if tcg_url else ""
                    price_info = {}
                    if "tcgplayer" in card and card["tcgplayer"] and "prices" in card["tcgplayer"]:
                        prices = card["tcgplayer"]["prices"]
                        if "holofoil" in prices:
                            holo = prices["holofoil"]
                            price_info = {
                                "avg": holo.get("mid", "N/A"),
                                "low": holo.get("low", "N/A"),
                                "high": holo.get("high", "N/A"),
                                "market": holo.get("market", "N/A")
                            }
                    results.append({"name": card_name, "set": card_set, "prices": price_info, "lowest_listing_url":lowest_listing_url})
    return render_template("index.html", results=results)
    
if __name__ == "__main__":
    app.run(debug=True)
