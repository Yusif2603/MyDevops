import telebot
import time

TOKEN = '8574073882:AAF7QTdCEJwxvfnlC-nwFFHETbC9OW-VhaE'
CHAT_ID = '845092985'

bot = telebot.TeleBot(TOKEN)

# 1. Ответ на команду /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Юсиф, я на связи! Теперь я не просто спамлю при запуске, а жду твоих команд. Напиши мне что-нибудь!")

# 2. Ответ на любое текстовое сообщение
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    text = message.text.lower()
    if "привет" in text:
        bot.reply_to(message, "Салам алейкум! Как дела на сервере?")
    elif "статус" in text:
        bot.reply_to(message, "Все системы работают нормально: Docker крутится, сайт мутится! 😎")
    else:
        bot.reply_to(message, f"Ты написал: '{message.text}'. Я пока только учусь, но я это запомнил!")

def start_notification():
    print("Бот успешно запущен на сервере AWS!")
    bot.send_message(CHAT_ID, "Система обновлена! Теперь я умею отвечать на сообщения. Попробуй написать мне 'привет' или 'статус'.")

if __name__ == "__main__":
    try:
        start_notification()
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Ошибка: {e}")
        time.sleep(5)
