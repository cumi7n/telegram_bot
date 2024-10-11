import telebot

TOKEN = telebot.TeleBot('')

@TOKEN.message_handler(commands=['start'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Здравствуйте! С удовольствием помогу вам разобраться с вопросами, которые часто возникают у игроков нашего клуба.

Чтобы мы могли вам помочь, пожалуйста, укажите команду, к которой относится ваш вопрос:
Team1 - Кто ваш командир?
Team2 - Кто отвечает за компетенции и управляет клубом?
Team3 - Какое расписание тренировок?
Team4 - Какие игры доступны в клубе?
Team5 - Сколько стоит посещение клуба?
Team6 - Есть ли у вас специальные акции или скидки для новых игроков?
Team7 - Каковы правила поведения в клубе?
Team8 - Обеспечен ли у вас высокоскоростной интернет и мощные компьютеры?
Team9 - Могу ли я принести свою периферию (мышь, клавиатуру, гарнитуру)?
Team10 - Проводятся ли в клубе турниры или лиги?
Team11 - Какое время работы клуба?
Team12 - Предоставляете ли вы игровые консоли (например, PlayStation, Xbox)?
Team13 -  Если у вас остались вопросы, которые не удалось решить через менеджеров, вы можете обратиться к заместителю руководителя клуба Гусеву Андрею Вячеславовичу.
''')

@TOKEN.message_handler(commands=['Team2'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team2 — Кто отвечает за компетенции и управляет клубом?
    
Менеджеры:
Рома — отвечает за 1-2 команду по CS
Рустам — отвечает за 3-4 состав по CS
Соня — отвечает за все команды по Dota
''')


@TOKEN.message_handler(commands=['Team3'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team3 — Какое расписание тренировок?
    
Расписание тренировок можно узнать после распределения в команду у командира или менеджера компетенции
''')


@TOKEN.message_handler(commands=['Team4'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team4 — Какие игры доступны в клубе?
    
CS, Dota, Fifa, Дроны, Валорант
''')


@TOKEN.message_handler(commands=['Team5'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team5 — Сколько стоит посещение клуба?
    
На данный момент у нас есть несколько вариантов, главное — посещайте тренировки и проявляйте интерес.

''')


@TOKEN.message_handler(commands=['Team6'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team6 — Есть ли у вас специальные акции или скидки для новых игроков?
    
В планах есть, сейчас ведутся переговоры.

''')


@TOKEN.message_handler(commands=['Team7'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team7 — Каковы правила поведения в клубе?
    
Проявляйте уважение к участникам клуба и соперникам, не делайте ничего, что может испортить имидж клуба.

''')


@TOKEN.message_handler(commands=['Team8'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team8 — Обеспечен ли у вас высокоскоростной интернет и мощные компьютеры?
    
С интернетом у нас все в порядке, а компьютеры подходят для небольших мероприятий. На данный момент мы играем дома, но скоро должны привезти новые ПК.

''')


@TOKEN.message_handler(commands=['Team9'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team9 — Могу ли я принести свою периферию (мышь, клавиатуру, гарнитуру)?
    
Конечно, в этом нет никаких проблем
''')


@TOKEN.message_handler(commands=['Team10'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team10 — Проводятся ли в клубе турниры или лиги?
    
У нас проходят как дружеские матчи, так и соревнования от федераций.

''')


@TOKEN.message_handler(commands=['Team11'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team11 — Какое время работы клуба?
    
Если речь идет о колледже, то мы работаем до 5 часов, но вы также можете играть дома.
''')


@TOKEN.message_handler(commands=['Team12'])
def start(message):
    TOKEN.send_message(message.chat.id, '''Team12 — Предоставляете ли вы игровые консоли (например, PlayStation, Xbox)?
    
Да, у нас есть Xbox, а в ближайшее время должна появиться PlayStation 5.
ta
''')

@TOKEN.message_handler(commands=['Team13'])
def start(message):
    TOKEN.send_message(message.chat.id,  '''Team13 – Если у вас остались вопросы, которые не удалось решить через менеджеров, вы можете обратиться к заместителю руководителя клуба Гусеву Андрею Вячеславовичу.
    
@Ubisoft5051''')


TOKEN.polling(none_stop=True, interval=0)

