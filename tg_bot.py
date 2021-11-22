import telebot, os, webbrowser, keyboa, pyautogui, getpass
from telebot import types


USER_NAME = getpass.getuser()


def add_to_startup(file_path=""):
    if file_path == "":
        file_path = os.path.dirname(os.path.realpath(__file__))
    bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % user
    with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
        bat_file.write(r'start "" %s' % file_path)

bot = telebot.TeleBot('1471686666:AAH9XoWWunmeJK_7BdtCShU4nN45aqFF4N0')
pyautogui.hotkey('ctrl', 'c')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    txt = message.text.split()
    for i in range(len(txt)):
        txt[i] = txt[i].lower()
    if  'найди' in txt:
        txt.remove('найди')
        plus = '+'
        url = f'https://yandex.ru/search/?text={plus.join(txt)}&lr=213&clid=2358536'
        webbrowser.open_new_tab(url)
    elif 'закрыть' in txt:
        txt.remove('закрыть')
        os.system(f'taskkill /F /IM {txt[0]}.exe /T')
        bot.send_message(message.from_user.id, f'{txt[0]} закрыт')

    elif 'выключи' in txt:
        txt.remove('выключи')
        txt.remove('через')
        if txt[0] == 'секунд':
            os.system(f'shutdown /s /t {int(txt[0])}')
            bot.send_message(message.from_user.id, f'Компьютер выключится через {int(txt[0])} секунд')
        elif txt[0] == 'минут':
            os.system(f'shutdown /s /t {int(txt[0])*60}')
            bot.send_message(message.from_user.id, f'Компьютер выключится через {int(txt[0])} секунд')
        else:
            bot.send_message(message.from_user.id, 'Обнаружена ошибка')
    elif 'пробел' in txt:
        pyautogui.press('space')
    elif '/help' in txt:
        bot.send_message(message.from_user.id, 'напишите разработчику: @lilm')
    elif 'скрин' in txt:
        pyautogui.hotkey('win', 'prntscrn')
        bot.send_message(message.from_user.id, f'Скриншот находится в папке "снимки экрана"')
    elif 'вверх' in txt:
        pyautogui.hotkey('up')
    else:
        bot.send_message(message.from_user.id, 'Упс, что-то пошло не так...');

bot.polling()
