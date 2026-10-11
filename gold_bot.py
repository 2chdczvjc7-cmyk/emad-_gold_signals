import os
import requests

TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

message = 'Emad Gold Signals: Bot test successful!'

response = requests.post(
    f'https://api.telegram.org/bot{TOKEN}/sendMessage',
    json={'chat_id': CHAT_ID, 'text': message},
    timeout=20
)
response.raise_for_status()
print('Message sent successfully')
