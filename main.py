import os
import requests
import feedparser

BOT_TOKEN = os.environ.get("BOT_TOKEN")
AMAZON_TAG = os.environ.get("AMAZON_TAG")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

def enviar_mensaje(texto):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID,
        "text": texto,
        "parse_mode": "HTML"
    }
    requests.post(url, json=payload)

def main():
    rss_url = "https://www.chollometro.com/rss"
    feed = feedparser.parse(rss_url)
    
    for entry in feed.entries[:3]:
        titulo = entry.title
        link = entry.link
        
        # Añadir etiqueta de afiliado de Amazon si aplica
        if "amazon" in link:
            link = f"{link}?tag={AMAZON_TAG}"
            
        mensaje = f"🔥 <b>{titulo}</b>\n\n🔗 <a href='{link}'>Ver Chollo</a>"
        enviar_mensaje(mensaje)

if __name__ == "__main__":
    main()