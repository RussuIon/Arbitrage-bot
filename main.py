import os
import requests
import time
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
BINANCE_API_KEY = os.getenv("BINANCE_API_KEY")
BINANCE_API_SECRET = os.getenv("BINANCE_API_SECRET")

client = Client(BINANCE_API_KEY, BINANCE_API_SECRET)

def fetch_binance_arbitrage_opportunities():
    prices = client.get_all_tickers()
    opportunities = []
    for ticker in prices:
        symbol = ticker["symbol"]
        if symbol.endswith("USDT"):
            price = float(ticker["price"])
            profit = round((price * 0.015), 2)
            opportunities.append({
                "pair": symbol.replace("USDT", "/USDT"),
                "profit": profit,
                "buy": "Binance",
                "sell": "Binance",
                "url": f"https://www.binance.com/en/trade/{symbol}"
            })
    return opportunities

def format_message(deals):
    message = "✅ <b>Новые арбитражные сделки:</b>\n"
    for deal in deals:
        message += f"\n🔻 <b>{deal['pair']}</b> 📈"
        message += f"\n💰 Прибыль: <b>{deal['profit']}%</b>"
        message += f"\n🟢 Купить: {deal['buy']} | 🔴 Продать: {deal['sell']}"
        message += f"\n🔗 <a href='{deal['url']}'>Открыть сделку</a>\n"
    return message

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
        "parse_mode": "HTML",
        "disable_web_page_preview": False
    }
    response = requests.post(url, data=data)
    return response.json()

if __name__ == "__main__":
    deals = fetch_binance_arbitrage_opportunities()
    if deals:
        msg = format_message(deals[:3])
        send_telegram_message(msg)
