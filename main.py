from telegram.ext import *
import sqlite3

# 1. Инициализация БД
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, 
             name TEXT, 
             phone TEXT, 
             date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

# 2. Создание состояний для диалога
QUESTION1, QUESTION2, PHONE, USER_DATA = range(4)

# 3. Обработчики сообщений
async def start(update, context):
    await update.message.reply_text("Первый вопрос?")
    return QUESTION1

async def question1(update, context):
    if update.message.text.lower() == "правильный ответ":
        await update.message.reply_text("Верно! Введите ваше имя:")
        return USER_DATA
    else:
        await update.message.reply_text("Неверно. Попробуйте еще раз")
        return QUESTION1

async def get_user_data(update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Теперь введите ваш телефон:")
    return PHONE

async def get_phone(update, context):
    # Сохранение в БД
    cursor.execute("INSERT INTO users (name, phone) VALUES (?, ?)",
                  (context.user_data['name'], update.message.text))
    conn.commit()
    await update.message.reply_text("Данные сохранены!")
    return ConversationHandler.END

# 4. Настройка обработчиков
application = ApplicationBuilder().token("TOKEN").build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        QUESTION1: [MessageHandler(filters.TEXT, question1)],
        USER_DATA: [MessageHandler(filters.TEXT, get_user_data)],
        PHONE: [MessageHandler(filters.TEXT, get_phone)]
    },
    fallbacks=[]
)

application.add_handler(conv_handler)
application.run_polling()