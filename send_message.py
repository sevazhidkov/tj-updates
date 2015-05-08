from vk_api import VkApi
from config import VK_LOGIN, VK_PASSWORD

vk = VkApi(VK_LOGIN, VK_PASSWORD)

def send_telegram_message():
    #TODO: Реализовать работу с Telegram
    return None


def send_vk_message(messages, user_id):
    for message in messages:
        vk.method('messages.send', {
            'message': message,
            'user_id': user_id
        })
    return None
