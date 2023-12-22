import telebot
import random 

token = '5462027421:AAFnAQh41qfUjz4x75sfNWGXy-LJA-5YM9M'

bot = telebot.TeleBot(token)

random_task = ["Начать читать книгу","Выйти на пробежку", "Посмотреть интересную лекцию", "Попробовать что-нибудь новое", "Прочитать интересную статью", "Приготовить супер вкусное блюдо", "Провести глобальную уборку"]

show = {}

HELP = """
/help - вывести список доступных задач
/add - добавить задачу в список(/add <дата> <задача>)
/show - напечатать все задачи на заданную дату(/show <дата>)
/random - добавить рандомную задачу на сегодня"""

def add_task(data, task):
  if data in show:
      show[data].append(task)
  else:
      show[data] = [task]

@bot.message_handler(commands = ["help", "start"])
def help(message):
    bot.send_message(message.chat.id, HELP)
    
@bot.message_handler(commands = ["add"])
def add(message):
    command = message.text.split(maxsplit = 2)
    data = command[1].lower()
    task = command[2]
    add_task(data, task)
    text = "Задача " + task + " добавлена на дату " + data
    bot.send_message(message.chat.id, text)
   
@bot.message_handler(commands = ["random"]) 
def rendom_add(message):
    data = "сегодня"
    task = random.choice(random_task)
    add_task(data, task)
    text = "Задача " + task + " добавлена на дату " + data
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands = ["show"]) 
def show_tasks(message):
    command = message.text.split(maxsplit = 1)
    data = command[1].lower()
    text = ""
    if data in show:
        text = data.upper() + "\n"
        for task in show[data]:
            text = text + "[]" + task +"\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)    
        
bot.polling(none_stop=True)
