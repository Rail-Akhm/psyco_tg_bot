import yadisk


client = yadisk.Client(token="")
# или
# client = yadisk.Client("<id-приложения>", "<secret-приложения>", "<токен>")

# Вы можете использовать либо конструкцию with, либо вручную вызвать client.close() в конце
with client:
    # Проверяет, валиден ли токен
    print(client.check_token())

    # Получает общую информацию о диске
    # print(client.get_disk_info())

    # Выводит содержимое "/some/path"
    print(list(client.listdir("/")))
