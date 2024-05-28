import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('введите ваш токен')

@bot.message_handler(commands= ['start'])
def start_message(message):
       bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить воду в определенное время!')
       reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))

       reminder_thread.start()

@bot.message_handler(commands= ['fact'])
def fact_message(message):
       list = ["**Вода помогает поддерживать оптимальный уровень жидкости в организме. Она играет ключевую роль во многих биологических процессах, включая терморегуляцию, пищеварение, кровообращение и выведение токсинов.",
               "**Питьевая вода помогает поддерживать здоровую кожу. Увлажненная кожа выглядит более свежей, упругой и здоровой. Питьевая вода помогает уменьшить появление морщин и сухости кожи.",
               "**Вода улучшает общее самочувствие и работу мозга. Достаточное употребление воды помогает бороться с усталостью, повышает концентрацию и улучшает память. Вода также помогает предотвратить головные боли, связанные с обезвоживанием."]
       random_fact = random.choice(list)
       bot.reply_to(message, f'Лови факт о полезности воды!{random_fact}')


@bot.message_handler(commands= ['help'])
def start_message(message):
       bot.reply_to(message, 'Список доступных команд:\n/start - начать работу, \n/help - получить помощь, \n/fact - факты о воде, \n/stats - количество стаканов воды, выпитых за день')


total_water_consumed = 0

@bot.message_handler(commands=['stats'])
def stats_message(message):
    bot.reply_to(message, f'Количество выпитых стаканов воды за день: {total_water_consumed}')

@bot.message_handler(func=lambda message: True)
def count_water(message):
    global total_water_consumed  # Объявляем переменную как глобальную
    if message.text.isdigit():
        amount = int(message.text)
        total_water_consumed += amount
        bot.reply_to(message, f'Выпито {amount} стаканов воды. Общее количество стаканов за день: {total_water_consumed}')
    else:
        bot.reply_to(message, 'Пожалуйста, введите число.')



def send_reminders(chat_id):
    first_rem = "09:00"
    second_rem = "12:00"
    third_rem = "15:00"
    fourth_rem = "17:00"
    end_rem = "19:00"

    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == third_rem or now == fourth_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)

time.sleep(1)



bot.polling(none_stop=True)

