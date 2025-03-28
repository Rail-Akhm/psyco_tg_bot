# Telegram Bot for Psychologists - Client Data Collector 🧠🤖

Telegram-бот для сбора информации о клиентах и автоматического сохранения в Excel на Яндекс.Диске. Проект создан для психологов, чтобы упростить первичный прием клиентов.

## ✨ Особенности
- Диалоговый опрос клиента через Telegram
- Сбор контактных данных и ответов на вопросы
- Автоматическое создание Excel-таблиц
- Интеграция с Яндекс.Диском для хранения данных
- Простая настройка через конфигурационный файл

## ⚙️ Требования
- Python 3.9+
- Аккаунт Яндекс.Диска
- Telegram-бот (получить у [@BotFather](https://t.me/BotFather))

## 🛠️ Установка
1. Клонировать репозиторий:
```bash
git clone https://github.com/Rail-Akhm/psyco_tg_bot
cd psychologist-bot
Установить зависимости:

bash
Copy
pip install yadisk pandas python-telegram-bot
🔑 Настройка
Создать файл config.py в корне проекта:

python
Copy
BOT_TOKEN = "ваш_telegram_токен"
YANDEX_DISK_TOKEN = "ваш_яндекс_токен"
Получить API-ключи:

Telegram Bot Token: через @BotFather

Яндекс.Диск Token: инструкция

🚀 Запуск
bash
Copy
python main.py
📋 Пример использования
Бот задаст последовательность вопросов:

Как вас зовут?

Ваш контактный телефон?

Предпочитаемое время консультации?

Краткое описание проблемы...

Данные сохраняются в файл:
Яндекс.Диск:/psychology_clients/клиенты_дата.xlsx

📁 Структура проекта
Copy
psychologist-bot/
├── main.py          # Основная логика бота
├── config.py        # Конфигурация (токены)
├── requirements.txt # Зависимости
└── README.md        # Документация
⚠️ Важно
Не публикуйте config.py с токенами в открытом доступе

Проверьте права доступа к Яндекс.Диску

Рекомендуется использовать виртуальное окружение

📄 Лицензия
MIT License. Подробнее в файле LICENSE.

📧 Контакты
По вопросам сотрудничества: rail.ahm3tshin@yandex.ru, railakhmetshin@gmail.com