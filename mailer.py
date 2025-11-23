import os
import requests
from dotenv import load_dotenv

load_dotenv()

def send_alert(subject, body):
    webhook = os.getenv("DISCORD_WEBHOOK")

    if not webhook:
        print("❌ No Discord webhook found in .env")
        return

    # Discord max message length is ~2000 chars
    safe_body = body[:1900]

    payload = {
        "content": f"📢 **{subject}**\n\n{safe_body}"
    }

    try:
        res = requests.post(webhook, json=payload)
        if res.status_code == 204:
            print("✅ Discord alert sent!")
        else:
            print("⚠️ Discord response:", res.status_code, res.text)
    except Exception as e:
        print("❌ Failed to send Discord alert:", e)
