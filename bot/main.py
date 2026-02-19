import telebot
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import time

# Твои данные
TOKEN = '8574073882:AAF7QTdCEJwxvfnlC-nwFFHETbC9OW-VhaE'
CHAT_ID = '845092985'

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app) # Это разрешает сайту присылать данные

# --- ЧАСТЬ 1: Слушаем сайт (Backend API) ---

@app.route('/web-notice', methods=['POST'])
def web_notice():
    data = request.json
    user_name = data.get('name', 'Аноним')
    
    # Бот отправляет сообщение тебе в Telegram
    bot.send_message(CHAT_ID, f"🔔 Юсиф, на сайте кто-то есть!\nИмя посетителя: {user_name}")
    
    return jsonify({"status": "success", "message": "Notice sent to Telegram"}), 200

# --- ЧАСТЬ 2: Слушаем Telegram (Твои команды) ---

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Я готов! Теперь я жду сигналов и от тебя, и от сайта.")

# --- ЧАСТЬ 3: Запуск всего вместе ---

def run_flask():
    # Запускаем веб-сервер на порту 5000
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Чтобы Flask и Telegram не мешали друг другу, запускаем их в разных "потоках"
    threading.Thread(target=run_flask).start()
    
    print("Бот и Веб-сервер запущены!")
    bot.polling(none_stop=True)
