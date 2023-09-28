from aiogram.types import Message
import time
from Token import admin_id

def check_user(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    f = open("data\logs.txt", "a", encoding="UTF-8")
    f.write(f"{time.strftime('%d%m%Y %H:%M')} {user_id} {user_name};\n")
    f.close()


def is_admin(message):
    if str(message.from_user.id) == str(admin_id):
        return True
    return False