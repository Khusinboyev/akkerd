from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

main_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
main_btn.add("📊Statistika", "🔧Kanallar", "📤Reklama", "👮‍♀️Admin", '🔘Tugmalar', "♻️ Tozalash")

channel_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
channel_btn.add("➕Kanal qo'shish", "❌Kanalni olib tashlash")
channel_btn.add("📋 Kanallar ro'yxati", "🔙Orqaga qaytish")

admin_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
admin_btn.add("➕👮‍♀️Admin qo'shish", "❌👮‍♀️Adminni olib tashlash")
admin_btn.add("📋 👮‍♀️Adminlar ro'yxati", "🔙Orqaga qaytish")

reklama_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
reklama_btn.add("📨Forward xabar yuborish", "📬Oddiy xabar yuborish", "🔙Orqaga qaytish")

tugma_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
tugma_btn.add("➕🔘 Tugma qo'shish", "❌🔘 Tugmani olib tashlash")
tugma_btn.add("📋🔘Tugmalar ro'yxati", "ℹ️Tugmaga ma'lumot qo'shish", "🔙Orqaga qaytish")

info_type_btn = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
info_type_btn.add("text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact")