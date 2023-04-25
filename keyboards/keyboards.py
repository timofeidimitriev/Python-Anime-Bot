import telebot
from telebot import types
from emoji import emojize

bot = telebot.TeleBot('YOUR TOKEN')

# Создаем клавиатуру с кнопками
menu_keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
wallpapers_button = types.KeyboardButton(emojize(":sunrise_over_mountains:Обои"))
anime_button = types.KeyboardButton("🔮Аниме")
pics_button = types.KeyboardButton(emojize(":cityscape_at_dusk:Пикчи"))
themes_button = types.KeyboardButton(emojize(":crescent_moon:Темки"))
stickers_button = types.KeyboardButton("😸Стикеры")


# Добавляем кнопки на клавиатуру
menu_keyboard.add(wallpapers_button, anime_button, pics_button, themes_button, stickers_button)
