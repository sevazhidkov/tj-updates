from time import sleep
from datetime import datetime
from vk_api import VkApi
from config import VK_LOGIN, VK_PASSWORD

vk = VkApi(VK_LOGIN, VK_PASSWORD)


def create_welcome_message():
    now_hour = datetime.timetuple(datetime.now())[3]
    if now_hour in range(4, 13):
        welcome_message = 'Доброе утро'
    elif now_hour in range(14, 18):
        welcome_message = 'Добрый день'
    else:
        welcome_message = 'Добрый вечер'
    return welcome_message


def send_telegram_message(messages, user_id, user_name):
    #TODO: Реализовать работу с Telegram
    return None


def send_vk_message(messages, user_id, user_name):
    welcome_message = create_welcome_message()
    vk.method('messages.send', {
            'message': '{welcome_message}, {name}'.format(
                welcome_message=welcome_message,
                name=user_name
            ),
            'user_id': user_id
    })
    sleep(2)
    vk.method('messages.send', {
            'message': 'Я курьер TJ, меня зовут Сева.',
            'user_id': user_id
    })
    sleep(2)
    for message in messages:
        vk.method('messages.send', {
            'message': message,
            'user_id': user_id
        })
        # Anti-captcha timeout
        sleep(2)

    return None
