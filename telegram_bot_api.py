import telegram
import dust_api
import weather_api
import get_key
import requests
import map_coordinate_api
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters

my_token = get_key.get_telegram_token()

bot = telegram.Bot(token=my_token)  # bot을 선언합니다.

updates = bot.getUpdates()  # 업데이트 내역을 받아옵니다.


def bot_start(bot, update):
    send2telegram = "weather notie telegram bot\n" \
                    "send location, reply weather\n" \
                    "source code : https://github.com/Bill-Park/pycon2017_tutorial"

    update.message.reply_text(send2telegram)


def help(bot, update):
    send2telegram = "weather notie telegram bot\n" \
                    "send location, reply weather\n" \
                    "source code : https://github.com/Bill-Park/pycon2017_tutorial"

    update.message.reply_text(send2telegram)


def get_location(bot, update):
    print(update.message.location.latitude)
    print(update.message.location.longitude)
    target_latitude = update.message.location.latitude
    target_longitude = update.message.location.longitude

    address_1, address_2, address_3 = map_coordinate_api.get_map_address(target_longitude, target_latitude)
    weather_coordinate = map_coordinate_api.get_weather_map_coordinate(address_1, address_2, address_3)

    weather_data = weather_api.get_weather_api(weather_coordinate['x'], weather_coordinate['y'])

    weather_SKY = weather_data['SKY']
    weather_REH = weather_data['REH']
    weather_T3H = weather_data['T3H']
    weather_POP = weather_data['POP']

    send2telegram_weather = "현재 기온 : {}\n" \
                            "현재 습도 : {}\n" \
                            "강수확률 : {}%\n" \
                            "내일 날씨 : {}".format(weather_T3H, weather_REH, weather_POP, weather_SKY)

    update.message.reply_text(send2telegram_weather)


updater = Updater(my_token)

start_handler = CommandHandler('start', bot_start)
updater.dispatcher.add_handler(start_handler)

get_location_handler = MessageHandler(Filters.location, get_location)
updater.dispatcher.add_handler(get_location_handler)

help_handler = CommandHandler('help', help)
updater.dispatcher.add_handler(help_handler)

updater.start_polling(timeout=3, clean=True)
print("bot start")
updater.idle()