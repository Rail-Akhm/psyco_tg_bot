import yadisk
from yadisk import YaDisk
from config import yadis_token
import pandas as pd


y = YaDisk(token=yadis_token)
client = yadisk.Client(token=yadis_token)

# Вы можете использовать либо конструкцию with, либо вручную вызвать client.close() в конце
with client:
    # Проверяет, валиден ли токен
    print(client.check_token())

    y.download("/Телеграм Бот Психология/tg_bot_psycho.xlsx", "tg_bot_psycho.xlsx")

    # 2. Читаем Excel-файл
    df = pd.read_excel("tg_bot_psycho.xlsx")

    # 3. Добавляем новую строку
    new_row = {"Имя": "Алсу", "Возраст": 27, "Номер телефона": 89271484857}  # Новая строка
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

    # 4. Сохраняем обновленный файл
    df.to_excel("tg_bot_psycho.xlsx", index=False)

    y.upload("tg_bot_psycho.xlsx", "/Телеграм Бот Психология/tg_bot_psycho.xlsx", overwrite=True)
