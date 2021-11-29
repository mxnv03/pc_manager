import telebot, os, webbrowser, keyboa, pyautogui, getpass
from telebot import types

USER_NAME = getpass.getuser()
bot = telebot.TeleBot('1471686666:AAH9XoWWunmeJK_7BdtCShU4nN45aqFF4N0')

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
    elif 'скрин' in txt:
        pyautogui.hotkey('win', 'prntscrn')
        path = "C:\\Users\\user\\OneDrive\\Изображения\\Снимки экрана"
        dir_list = [os.path.join(path, x) for x in os.listdir(path)]
        if dir_list:
            date_list = [[x, os.path.getctime(x)] for x in dir_list]
            sort_date_list = sorted(date_list, key=lambda x: x[1], reverse=True)
            bot.send_photo(message.from_user.id, open(sort_date_list[0][0], 'rb'))
    elif 'вверх' in txt:
        pyautogui.hotkey('up')
    elif '/help' in txt:
        bot.send_message(message.from_user.id, 'скрин - сделает скрин экрана и отправит в чат \nпробел - нажмёт на пробел \nвыключи через ... минут/секунд выключит пк через заданное время  \nнайди (поисковой запрс) - найдет в браузере ваш запрос \nзакрыть ... - закроет приложение')
    else:
        bot.send_message(message.from_user.id, 'Упс, что-то пошло не так...');

bot.polling()
