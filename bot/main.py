import telebot
from flask import Flask, request, jsonify
from flask_cors import CORS
import threading
import datetime  # Теперь импорт на месте

# Твои данные
TOKEN = '8574073882:AAF7QTdCEJwxvfnlC-nwFFHETbC9OW-VhaE'
CHAT_ID = '845092985'

bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)
CORS(app)

# --- 1. ПУТЬ ДЛЯ УВЕДОМЛЕНИЙ ---
@app.route('/api/web-notice', methods=['POST'])
def web_notice():
    data = request.json
    user_name = data.get('name', 'Аноним')
    bot.send_message(CHAT_ID, f"🔔 Юсиф, на сайте кто-то есть!\nИмя посетителя: {user_name}")
    return jsonify({"status": "success"}), 200

# --- 2. ПУТЬ ДЛЯ ВРЕМЕНИ ---
@app.route('/api/time', methods=['GET'])
def get_time():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    return jsonify({"time": now})

# --- 3. КОМАНДЫ ТЕЛЕГРАМ ---
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Я готов! Теперь я жду сигналов и от тебя, и от сайта.")

# --- 4. ЗАПУСК ---
def run_flask():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    # Запускаем Flask в отдельном потоке
    threading.Thread(target=run_flask, daemon=True).start()
    print("Бот и Веб-сервер запущены!")
    # Запускаем бота
    bot.polling(none_stop=True)
