import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id


def write_msg(user_id, message,keyboard = None):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random.randint(0, 2048), 'keyboard':keyboard})

def create_keyboard(response):
    keyboard = VkKeyboard(one_time=True)

    if response == 'Заводи':
        keyboard.add_button('ДА!', VkKeyboardColor.POSITIVE)
        keyboard.add_button('НЕТ', VkKeyboardColor.NEGATIVE)
        keyboard = keyboard.get_keyboard()
        return keyboard

    elif response == 'ДА!' or response == 'НЕТ':
        keyboard.add_button('ПОГНАЛИ!', VkKeyboardColor.PRIMARY)
        keyboard = keyboard.get_keyboard()
        return keyboard
    elif response == 'ПОГНАЛИ!':
        keyboard.add_button('МУЖЧИНА', VkKeyboardColor.DEFAULT)
        keyboard.add_button('ЖЕНЩИНА', VkKeyboardColor.DEFAULT)
        keyboard = keyboard.get_keyboard()
        return keyboard
    elif response == "МУЖЧИНА" or "ЖЕНЩИНА":
        keyboard.add_button('Вот лодырь!', VkKeyboardColor.PRIMARY)
        keyboard = keyboard.get_keyboard()
        return keyboard
    elif response == 'Проверим':
        keyboard.add_button('МОГУ!', VkKeyboardColor.DEFAULT)
        keyboard.add_button('ТРУДНОВАТО', VkKeyboardColor.NEGATIVE)
        keyboard = keyboard.get_keyboard()
        return keyboard
    elif response == 'МОГУ!' or response == 'ТРУДНОВАТО':
        keyboard.add_button('ПОГНАЛИ', VkKeyboardColor.PRIMARY)
        keyboard = keyboard.get_keyboard()
        return keyboard


# API-ключ созданный ранее
token = "my actual token here"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

#
print("it's working!")
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        response = event.text
        keyboard = create_keyboard(response)

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
          # Сообщение от пользователя

            # Каменная логика ответа
            if response == "Заводи":
                write_msg(event.user_id, "Привет! \n Готов ли ты к изменению своего тела?", keyboard = keyboard)
            elif response == "ДА!":
                write_msg(event.user_id, "С помощью этого бота ты сможешь подобрать эффективную программу именно для себя. \n И так. Ты готов? Тогда поехали!", keyboard=keyboard)

            elif response == "НЕТ":
                write_msg(event.user_id, "НЕТ: НЕТ! Ты будешь заниматься, назад пути нет.", keyboard=keyboard)

            elif response == "ПОГНАЛИ!":
                write_msg(event.user_id, "Для начала укажи нам как ты себя определяешь? [МУЖЧИНА] ты ИЛИ [ЖЕНЩИНА]?",keyboard=keyboard)

            elif response == "Вот лодырь!":
                write_msg(event.user_id, "Да, знаю ¯\_(ツ)_/¯ ")
            elif response == "ты обновился?":
                write_msg(event.user_id, "да, версия 2.0")
            elif response == "МУЖЧИНА" or "ЖЕНЩИНА":
                write_msg(event.user_id, "Разработчик с радостью бы допилил оставшуюся часть, но хочет пойти спать"
                                         "Вот программа на сегодня:\n" "День 1: (акцент на грудь) \n""1) Отжимания; \n" 
                                         "2) Приседания;\n" "3) Отжимания узким хватом;\n" "4) Скручивания; \n" 
                                         "5) Медленные отжимания;\n" "6) Медленные отжимания узким хватом;\n", keyboard=keyboard)
            else:
                write_msg(event.user_id, "Нажимайте, пожалуйста на кнопки")