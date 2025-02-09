import logging
from telegram import Update
from telegram.ext import (
    Application,
    ContextTypes,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)
from config import bot_token

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Определяем состояния диалога
QUESTION_1, QUESTION_2, QUESTION_3 = range(3)

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Ответь на пару вопросов.")
    await update.message.reply_text("Вопрос 1: Как тебя зовут?")
    return QUESTION_1  # Переходим к первому вопросу

# Обработчик первого вопроса
async def handle_question_1(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.message.text  # Сохраняем ответ

    # Проверяем, что имя состоит только из букв (и, возможно, пробелов)
    if not user_name.replace(" ", "").isalpha():  # Убираем пробелы и проверяем, что остальное — буквы
        await update.message.reply_text("Ошибка: имя может содержать только буквы и пробелы. Попробуйте еще раз.")
        return QUESTION_1  # Возвращаемся к первому вопросу
    else:
        context.user_data['name'] = user_name  # Сохраняем имя в контексте
        await update.message.reply_text(f"Приятно познакомиться, {user_name}!")
        await update.message.reply_text("Вопрос 2: Сколько тебе лет?")
        return QUESTION_2  # Переходим ко второму вопросу

async def handle_question_2(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_age = update.message.text  # Сохраняем ответ
    context.user_data['user_age'] = user_age  # Сохраняем имя в контексте
    await update.message.reply_text(f"Ок, {context.user_data['name']}!")
    await update.message.reply_text("Вопрос 3: Напиши номер телефона?")
    return QUESTION_3  # Переходим ко второму вопросу

# Обработчик второго вопроса
async def handle_question_3(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_number = update.message.text  # Сохраняем ответ
    context.user_data['user_number'] = user_number  # Сохраняем возраст в контексте

    # Получаем сохраненные данные из контекста
    name = context.user_data.get('name', 'неизвестно')
    user_age = context.user_data.get('user_age', 'неизвестно')
    user_number = context.user_data.get('user_number', 'неизвестно')

    await update.message.reply_text(f"Спасибо за ответы!\n"
                                   f"Твое имя: {name}\n"
                                   f"Тебе {user_age} лет.\n"
                                   f"Твой номер {user_number}")
    return ConversationHandler.END  # Завершаем диалог

# Обработчик отмены диалога
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Диалог прерван.")
    return ConversationHandler.END

# Основной блок
if __name__ == '__main__':
    # Создаем объект приложения
    app = Application.builder().token(bot_token).build()

    # Настройка ConversationHandler
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],  # Точка входа
        states={
            QUESTION_1: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question_1)],
            QUESTION_2: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question_2)],
            QUESTION_3: [MessageHandler(filters.TEXT & ~filters.COMMAND, handle_question_3)],            
        },
        fallbacks=[CommandHandler('cancel', cancel)]  # Обработчик отмены
    )

    # Добавляем ConversationHandler в приложение
    app.add_handler(conv_handler)

    # Запускаем бота
    print("Бот запущен...")
    app.run_polling()