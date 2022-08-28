from handlaers.startFor import *
from handlaers.admin_panel import *


@dp.message_handler(commands='toshiqoy')
async def helper(message: types.Message):
    await message.reply('hoz')
    import shutil
    shutil.make_archive("../AKKREDITATSIYA", 'zip', "../AKKREDITATSIYA")
    await message.reply_document(document=open("../AKKREDITATSIYA.zip", 'rb'))



@dp.callback_query_handler(text = "🗂Kirish")
async def entered(call: CallbackQuery):
	await call.answer()
	B_names = sql.execute("SELECT b_name from tugma").fetchall()
	if len(B_names) > 0:
		buttons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		for name in B_names:
			buttons.insert(name[0])
		await call.message.reply("Xush kelibsiz! Kerakli bo'limni tanlang", reply_markup=buttons)
	else:
		await call.message.reply("Xush kelibsiz! Kerakli bo'limni tanlang")


@dp.message_handler()
async def entered(message: types.Message):
	if await functions.check_on_start(message.chat.id):
		try:
			check = sql.execute(f"""SELECT b_name FROM tugma WHERE b_name = '{message.text}'""").fetchone()
			if check == None:
				await message.reply("Bunday tugma yo'q hali kiritilmadi")
			else:
				level = sql.execute(f"""SELECT level FROM tugma WHERE b_name = '{message.text}'""").fetchone()
				if level[0] == None:
					info = sql.execute(f"""SELECT file_id FROM tugma WHERE b_name = '{message.text}'""").fetchone()
					if info[0] == None:
						await message.reply("Bo'mbo'sh")
					else:
						infosent = sql.execute(f"""SELECT file_id FROM tugma WHERE b_name = '{message.text}'""").fetchone()
						try:
							print(infosent[0])
							await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=main_admin, message_id=infosent[0])
						except:
							await message.reply("Biriktirilgan ma'lumotda xatolik")
				else:
					buttons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
					b_names = sql.execute(f"""SELECT b_name FROM tugma WHERE b_name = '{message.text}'""").fetchall()
					for name in b_names:
						buttons.insert(name[0])
					await message.reply("Tanlang", reply_markup=buttons)
		except:
			enter_btn = types.InlineKeyboardMarkup(row_width=1)
			enter_btn.add(InlineKeyboardButton('🗂Kirish', callback_data='🗂Kirish'))
			await message.reply("tanlang", reply_markup=enter_btn)
	else:
		sql.execute("SELECT id FROM channels")
		rows = sql.fetchall()

		join_inline = types.InlineKeyboardMarkup(row_width=1)
		for row in rows:
			all_details = await dp.bot.get_chat(chat_id=row[0])
			url = all_details['username']
			join_inline.insert(InlineKeyboardButton(text="Kanalga o'tish", url=f"https://t.me/{url}"))
		join_inline.add(InlineKeyboardButton("✅ Aʼzo boʻldim", callback_data='check'))
		await message.reply("Botimizdan foydalanish uchun kanalimizga azo bo'ling", reply_markup=join_inline)



if __name__=="__main__":
	executor.start_polling(dp)
