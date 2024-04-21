Telegram bot starter
---
> Template for async Telegram bot in Python. With MongoDB and cloud logging under the hood.

## ⚙️ Deployment
1. Install requirements  
```buildoutcfg
pip install -r requirements.txt
```
2. Create `.env` file and add there Telegram bot API key
```buildoutcfg
TELEGRAM_BOT_TOKEN=YourToken
```
3. Start bot
```buildoutcfg
python main.py
```

---

## 🚀 Go even further

- Connect your MongoDB database by adding `MONGODB_CONNECTION_STRING` and `MONGODB_DATABASE_NAME` variables to 
  the `.env` file
  

- Enable cloud logging via [Loggram](https://loggram.me) by adding `LOGGRAM_API_KEY` and `LOGGRAM_CHANNEL_ID` variables 
  to the `.env` file
  
---
> Twitter: [@botpapa_](https://twitter.com/botpapa_)