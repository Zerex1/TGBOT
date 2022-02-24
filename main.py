import telebot
from settings import TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def get_text_massage(message):
    filename = 'Stolica.csv'
    open(filename).readline().split('\n')
    portfolio = []
    for line in open(filename):
        fields = line.split(",")
        country = fields[0]
        capital = fields[1]
        capital = capital.rstrip("\n")
        stock = (country, capital)
        portfolio.append(stock)

    for i in range(0, len(portfolio)):
        for j in range(0, len(portfolio[i])):
            if message.text == portfolio[i][0]:
                bot.send_message(message.from_user.id, portfolio[i][1])
                bot.send_message(message.from_user.id, "Введите страну")
                return
            else:
                if i == len(portfolio)-1:
                    bot.send_message(message.from_user.id, "Нет такой страны, попробуйте заново")
                    return



bot.polling()
