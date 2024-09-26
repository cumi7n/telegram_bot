from datetime import datetime, timezone, timedelta  # Убраны лишние импорты
import telebot
import sqlite3

# УДАЛЕНО: Неправильный импорт из nltk и torchvision, они не нужны для вашего кода
# from nltk.twitter.twitter_demo import yesterday
# from torchvision import message

bot = telebot.TeleBot("7944494979:AAF4yl9JSAZKaaesXW5D1FFX1aAu07QA9HU")

con = sqlite3.connect('reports.db')

with con:
    # получаем количество таблиц с нужным нам именем
    data = con.execute("select count(*) from sqlite_master where type='table' and name='reports'")
    for row in data:
        # если таких таблиц нет
        if row[0] == 0:
            # создаём таблицу для отчётов
            with con:
                con.execute("""
                    CREATE TABLE reports (
                        datetime VARCHAR(40) PRIMARY KEY,
                        date VARCHAR(20),
                        id VARCHAR(200),
                        name VARCHAR(200),
                        text VARCHAR(500)
                    );
                """)

# обрабатываем входящий отчёт пользователя

@bot.message_handler(commands=['now'])  # Исправлено с "command" на "commands"
def start(message):
    with sqlite3.connect('reports.db') as con:
        now = datetime.now(timezone.utc)
        date = now.date()

        s = ''  # Переместили строку внутрь блока with

    data = con.execute('SELECT * FROM reports WHERE date = :DATE;', {"DATE": str(date)})

    for row in data:
        s = s + '*' + row[3] + '*' + '~' + row[4] + '\n\n'

    if s == '':
        s = 'За сегодня ещё нет записей'
    bot.send_message(message.from_user.id, s, parse_mode='Markdown')

@bot.message_handler(commands=['yesterday'])  # Исправлено с "command" на "commands"
def start(message):
    # УДАЛЕНО: Лишние закомментированные строки, содержащие неправильную логику
    # con = sqlite3.connect('reports.db')
    # yesterday = datetime.today()() - timedelta(days=1)
    # y_date =  yesterday.date()
    # s = ''

    with sqlite3.connect('reports.db') as con:  # Перенесли открытие соединения в блок with
        yesterday = datetime.now(timezone.utc) - timedelta(days=1)  # Исправлено: использование datetime.now
        y_date = yesterday.date()
        s = ''

        data = con.execute('SELECT * FROM reports WHERE date = :Date;', {'Date': str(y_date)})  # Исправлен SQL-запрос
        for row in data:
            # УДАЛЕНО: Лишний код проверки row[0] == 0, так как он некорректен
            # if row[0] == 0:
            #     pass
            # else:
            s = s + '*' + row[3] + '*' + '~' + row[4] + '\n\n'

    if s == '':
        s = 'За вчерашний день нет записей'

    bot.send_message(message.from_user.id, s, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def func(message):
    # подключаемся к базе
    con = sqlite3.connect('reports.db')
    # подготавливаем запрос
    sql = 'INSERT INTO reports (datetime, date, id, name, text) values(?, ?, ?, ?, ?)'
    # получаем дату и время
    now = datetime.now(timezone.utc)
    # и просто дату
    date = now.date()
    # формируем данные для запроса
    data = [
        (str(now), str(date), str(message.from_user.id), str(message.from_user.username), str(message.text[:500]))
    ]
    # добавляем с помощью запроса данные
    with con:
        con.executemany(sql, data)
    # отправляем пользователю сообщение о том, что отчёт принят
    bot.send_message(message.from_user.id, 'Принято, спасибо!', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)
