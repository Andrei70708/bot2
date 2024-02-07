from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
TOKEN = '6752366715:AAHhnE8qgHTsdd9RfgmDj4bAxa-IEiLIC_w'
# Замените 'TARGET_GROUP_ID' на ID группы, в которую нужно перенаправлять сообщения
TARGET_GROUP_ID = '-1002007363503'
# Замените 'YOUR_TELEGRAM_USER_ID' на ваш ID в Telegram
YOUR_TELEGRAM_USER_ID = '6142747706'

def handle_photo(update, context):
    chat_id = update.message.chat_id
    user = update.message.from_user
    file_id = update.message.photo[-1].file_id

    # Отправляем фото на ваш аккаунт
    context.bot.send_photo(
        chat_id=int(TARGET_GROUP_ID),
        photo=file_id,
        caption=f"Привет, {user.first_name}! Боту отправили скриншот отзыва."
    )

    # Отвечаем пользователю определенным текстом
    context.bot.send_message(
        chat_id=chat_id,
        text="Спасибо за скриншот! Я его получил и отправил оператору. Теперь отправьте номер телефона и название банка Вам отправят 50р. после проверки скриншота оператором"
    )

    context.bot.send_photo(
        chat_id=int(TARGET_GROUP_ID),
        photo=file_id,
        caption=f"Привет, {user.first_name}! Боту отправили скриншот отзыва:"
    )

def handle_user_message(update, context):
    chat_id = update.message.chat_id
    user_message = update.message.text

    # Отвечаем определенным текстом на сообщение от пользователя
    context.bot.send_message(
        chat_id=chat_id,
        text="Спасибо за ваше сообщение! Я получил его."
    )

def handle_menu(update, context):
    chat_id = update.message.chat_id
    context.bot.send_message(
        chat_id=chat_id,
        text='Здравствуйте, уважаемый покупатель!. Благодарим Вас за покупку стелек TM MUVUTER. Предлагаем Вам кэшбек 50руб. за покупку на Вашу карту.Для этого, просим Вас:'
        '\n1. Оставьте, пожалуйста, отзыв на том маркетплейсе, где Вы покупали наш товар. Прикрепите к отзыву фотографии этого товара.'
        '\n2. Как Ваш отзыв будет опубликован, сделайте скриншот Вашего отзыва и прикрепите в этот чат-бот.'
    )

def forward_messages(update, context):
    chat_id = update.message.chat_id
    user = update.message.from_user
    message_text = update.message.text

    # Замените 'TARGET_GROUP_ID' на фактический ID группы, в которую нужно перенаправлять сообщения
    context.bot.forward_message(chat_id=int(TARGET_GROUP_ID), from_chat_id=chat_id, message_id=update.message.message_id)

# Создаем обработчик сообщений с фильтром на фотографии
photo_handler = MessageHandler(Filters.photo, handle_photo)

# Создаем обработчик команды "меню"
menu_handler = CommandHandler('menu', handle_menu)

# Создаем обработчик текстовых сообщений для перенаправления
forward_handler = MessageHandler(Filters.text & ~Filters.command, forward_messages)

# Создаем и запускаем бота
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(photo_handler)
dispatcher.add_handler(menu_handler)
dispatcher.add_handler(forward_handler)

updater.start_polling()
updater.idle()

