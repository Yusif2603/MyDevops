import telebot
import time

# ВАЖНО: Вставь свой токен и ID, которые мы использовали раньше
TOKEN = '8574073882:AAF7QTdCEJwxvfnlC-nwFFHETbC9OW-VhaE'
CHAT_ID = '845092985'

bot = telebot.TeleBot(TOKEN)

def start_bot():
    print("Бот успешно запущен на сервере AWS!")
    bot.send_message(CHAT_ID, "Юсиф, я запущен через Docker Compose! Теперь я работаю как отдельная программа. 🚀")

if __name__ == "__main__":
    try:
        start_bot()
        # Это заставит бота работать постоянно
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
