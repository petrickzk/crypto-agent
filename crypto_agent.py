import os
import requests

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

data = requests.get(
    "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
).json()

btc = data["bitcoin"]["usd"]
eth = data["ethereum"]["usd"]

message = f"""
☀️ Morning Crypto Report

BTC: ${btc}
ETH: ${eth}

Top AI Coins:
• TAO
• FET
• VIRTUAL

Powered by GitHub Actions 🚀
"""

requests.post(
    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)
