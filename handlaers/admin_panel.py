from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import *
from Statess.statess import From
from buttons.mButtons import *
from handlaers.functions import *

@dp.message_handler(commands = ["coder", "developer", "programmer"])
async def coder(msg: types.Message):
	await msg.reply("<b>Bot dasturchisi @egam_haq\n\nPowered by @egam_haq</b>", parse_mode='html')


markup = ReplyKeyboardMarkup(resize_keyboard=True)
markup.add("🔙Orqaga qaytish")

main_admin = 619839487


@dp.message_handler(commands=['admin', 'panel'])
async def new(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.answer("Assalomu alaykum admin janoblari", reply_markup=main_btn)


@dp.message_handler(text = "🔙Orqaga qaytish")
async def backs(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("Bosh menyu", reply_markup=main_btn)

############################          STATISTIKA            """"""""""""""""""""""

@dp.message_handler( text = "📊Statistika")
async def new(msg: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if msg.from_user.id in Admin:
		sql.execute("SELECT COUNT(*) FROM users WHERE lang = ?", ('uz',))
		followersuz = sql.fetchone()[0]
		sql.execute("SELECT COUNT(*) FROM users WHERE lang = ?", ('ru',))
		followersru = sql.fetchone()[0]
		sql.execute("SELECT COUNT(*) FROM users WHERE lang = ?", ('en',))
		followersen = sql.fetchone()[0]
		sql.execute("SELECT COUNT(*) FROM users")
		followersall = sql.fetchone()[0]
		await msg.answer(f"👥Botdagi jami azolar soni👇👇\n\n🇺🇿O'zbeklar soni {followersuz}\n\n🇷🇺Ruslar soni - {followersru}\n\n🇺🇸Ingilizlar soni - {followersen}\n\n👤Jami azolar soni: > {followersall}")

###########################           KANALLAR              """""""""""""""""""""

@dp.message_handler(text = '🔧Kanallar')
async def new(msg: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if msg.from_user.id in Admin:
		await msg.answer("Tanlang", reply_markup=channel_btn)


@dp.message_handler(text = "➕Kanal qo'shish")
async def channel_add(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		await message.reply("Kanal qo'shish uchun kanalning userini yuboring.\nMisol uchun @coder_admin", reply_markup=markup)
		await From.channelAdd.set()


@dp.message_handler(state=From.channelAdd)
async def channelAdd1(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		channel_id = [message.text.upper()]
		data = sql.execute(f"SELECT id FROM channels WHERE id = '{message.text.upper()}'").fetchone()
		if data is None:
			if message.text[0]=='@':
				await panel_func.channel_add(channel_id)
				await state.finish()
				await message.reply("Kanal qo'shildi🎉🎉", reply_markup=channel_btn)
			else:
				await message.reply("Kanal useri xato kiritildi\nIltimos userni @coder_admin ko'rinishida kiriting", reply_markup=channel_btn)
		else:
			await message.reply("Bu kanal avvaldan bor", reply_markup=channel_btn)
		await state.finish()


@dp.message_handler(text = "❌Kanalni olib tashlash")
async def channelD(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("O'chiriladigan kanalning userini yuboring.\nMisol uchun @coder_admin", reply_markup=markup)
		await From.channelDelete.set()

@dp.message_handler(state=From.channelDelete)
async def ChannelDel(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		channel_id = message.text.upper()
		data = sql.execute(f"""SELECT id FROM channels WHERE id = '{channel_id}'""").fetchone()
		if data is None:
			await message.reply("Bunday kanal yo'q", reply_markup=channel_btn)
		else:
			if message.text[0]=='@':
				await panel_func.channel_delete(channel_id)
				await state.finish()
				await message.reply("Kanal muvaffaqiyatli o'chirildi", reply_markup=channel_btn)
			else:
				await message.reply("Kanal useri xato kiritildi\nIltimos userni @coder_admin ko'rinishida kiriting", reply_markup=channel_btn)

		await state.finish()

@dp.message_handler(text = "📋 Kanallar ro'yxati")
async def channelList(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		if len(await panel_func.channel_list()) > 3:
			await message.reply(await panel_func.channel_list())
		else:
			await message.reply("Hozircha kanallar yo'q")

################################            REKLAMA          """"""""""""""""""""""

@dp.message_handler(text = "📤Reklama")
async def all_send(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("Foydalanuvchilarga xabar yuborish bo'limi", reply_markup=reklama_btn)

@dp.message_handler(lambda message: message.text == "📨Forward xabar yuborish")
async def all_users(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		await message.answer("Forward yuboriladigan xabarni yuboring", reply_markup=markup)
		await From.forward_msg.set()


@dp.message_handler(state=From.forward_msg, content_types=ContentType.ANY)
async def all_users2(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await state.finish()
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		rows = sql.execute(f"SELECT user_id FROM users ").fetchall()
		for row in rows:
			id = row[0]
			await forward_send_msg(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

		await message.answer("Xabar yuborish yakunlandi", reply_markup=reklama_btn)


@dp.message_handler(lambda message: message.text == "📬Oddiy xabar yuborish")
async def all_users(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		await message.answer("Yuborilishi kerak bo'lgan xabarni yuboring", reply_markup=markup)
		await From.send_msg.set()


@dp.message_handler(state=From.send_msg, content_types=ContentType.ANY)
async def all_users2(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await state.finish()
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		rows = sql.execute(f"SELECT user_id FROM users ").fetchall()
		for row in rows:
			id = row[0]
			await send_message_chats(from_chat_id=message.chat.id, message_id=message.message_id, chat_id=id)

		await message.answer("Xabar yuborish yakunlandi", reply_markup=reklama_btn)


################################              Tozalash           """"""""""""""""""""""

@dp.message_handler(text = "♻️ Tozalash")
async def clear(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("Tozalash kodini kiriting: ", reply_markup=markup)
		await From.clear_msg.set()

@dp.message_handler(state=From.clear_msg, text = "🔙Orqaga qaytish", content_types=ContentType.ANY)
async def all_users2(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await state.finish()
		await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.clear_msg)
async def clear1(message:types.Message, state:FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		if message.text=='0000':
			sql.execute("SELECT COUNT(*) FROM users")
			followers = sql.fetchone()[0]
			check_time = followers / 60 / 10
			text = "Tozalash boshlandi\nTomom bo'linchaya {} daqiqa bor\n{} ta odam tekshiriladi\n\nTozalash tamom bo'lincha hech novino tegmang❗️"
			text = text.format(check_time, followers)
			await message.reply(text)

			rows = sql.execute(f"SELECT user_id FROM users ").fetchall()
			for row in rows:
				id = row[0]
				try:
					await dp.bot.send_message(chat_id=id, text = "Biz bilan qolganingiz uchun raxmat 🎉")
				except BotBlocked:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
				except ChatNotFound:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
				except RetryAfter:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
				except UserDeactivated:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
				except MigrateToChat:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
				except TelegramAPIError:
					sql.execute(f"DELETE FROM users WHERE user_id ='{id}'")
					db.commit()
			await message.answer("Tozalash yakunlandi  ✅", reply_markup=main_btn)
			await state.finish()
		else:
			await message.answer("Xavfsizlik kodi noto'g'ri", reply_markup=main_btn)
			await state.finish()


################################              Adminlar           """"""""""""""""""""""

@dp.message_handler(text = "👮‍♀️Admin")
async def clear1(message:types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		if message.from_user.id == main_admin:
			if message.from_user.id == main_admin:
				await message.reply("Tanlang", reply_markup=admin_btn)
			else:
				await message.reply("bu bo'lim siz uchun emas")
		else:
			await message.reply("siz bu bo'limni ishlata olmaysiz")


@dp.message_handler(text = "➕👮‍♀️Admin qo'shish", user_id = main_admin)
async def channel_add(message: types.Message):
	markup = ReplyKeyboardMarkup(resize_keyboard=True)
	markup.add("🔙Orqaga qaytish")
	await message.reply("Admin qo'shish uchun adminning id sini yuboring", reply_markup=markup)
	await From.admin.set()

@dp.message_handler(state=From.admin, text = "🔙Orqaga qaytish", content_types=ContentType.ANY, user_id=main_admin)
async def all_users2(message: types.Message, state: FSMContext):
	await state.finish()
	await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.admin, user_id=main_admin)
async def all_users2(message: types.Message, state: FSMContext):
	# sql.execute(
	# 	f"""INSERT INTO admin (user_id, date) VALUES ("{message.text}", 'face')""")
	# db.commit()
	data = sql.execute(f"SELECT user_id FROM admin WHERE user_id = '{message.text.upper()}'").fetchone()
	if data is None:
		if message.text.isdigit() == True:
			sql.execute(
				f"""INSERT INTO admin (user_id, date) VALUES ("{message.text}", 'face')""")
			db.commit()
			await state.finish()
			await message.reply("Yangi admin qo'shildi🎉🎉", reply_markup=admin_btn)
		else:
			await message.reply("Yangi admin id sida xatolik bor, qaytadan kiriting",
								reply_markup=admin_btn)
	else:
		await message.reply("Bu admin avvaldan bor", reply_markup=admin_btn)
	await state.finish()


@dp.message_handler(text = "❌👮‍♀️Adminni olib tashlash", user_id = main_admin)
async def channelD(message: types.Message):
	await message.reply("O'chiriladigan adminning id sini yuboring", reply_markup=markup)
	await From.admindelete.set()

@dp.message_handler(state=From.admindelete, user_id = main_admin)
async def ChannelDel(message: types.Message, state: FSMContext):
	channel_id = message.text.upper()
	data = sql.execute(f"""SELECT user_id FROM admin WHERE user_id = '{channel_id}'""").fetchone()
	if data is None:
		await message.reply("Bunday admin yo'q", reply_markup=admin_btn)
	else:
		if message.text.isdigit()==True:
			sql.execute(f'DELETE FROM admin WHERE user_id = "{message.text}"')
			db.commit()
			await state.finish()
			await message.reply("Admin muvaffaqiyatli o'chirildi", reply_markup=admin_btn)
		else:
			await message.reply("Admin id si noto'gri kiritildi, iltimos qaytadan kiriting", reply_markup=admin_btn)

	await state.finish()

@dp.message_handler(text = "📋 👮‍♀️Adminlar ro'yxati", user_id = main_admin)
async def channelList(message: types.Message):
	list_admin = sql.execute("SELECT user_id from admin").fetchall()
	admins = ''
	if len(list_admin) > 0:
		try:
			for admin in list_admin:
				aaaaaa = admin[0]
				all_details = await dp.bot.get_chat(chat_id=aaaaaa)
				admins += f"\n<b>{all_details['first_name']}\n{aaaaaa}\n@{all_details['username']}</b>\n----------------------------"
			await message.reply(admins, reply_markup=admin_btn)
		except:
			await message.reply(list_admin, reply_markup=admin_btn)
	else:
		await message.reply("Hozircha adminlar yo'q", reply_markup=admin_btn)



#############################         Tugmalar                #################################################################################

@dp.message_handler(text = "🔘Tugmalar")
async def clear1(message:types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("Tugmalar bo'limiga kirdingiz", reply_markup=tugma_btn)
	else:
		await message.reply("Bu bo'lim siz uchun emas")

@dp.message_handler(text = "➕🔘 Tugma qo'shish")
async def channel_add(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		markup = ReplyKeyboardMarkup(resize_keyboard=True)
		markup.add("🔙Orqaga qaytish")
		await message.reply("Tugma qo'shish uchun tugmaning nomini yuboring \n\n Masalan:  🔊Music", reply_markup=markup)
		await From.tugmaadd.set()

@dp.message_handler(state=From.tugmaadd, text = "🔙Orqaga qaytish")
async def all_u(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await state.finish()
		await message.reply("Orqaga qaytildi", reply_markup=main_btn)

@dp.message_handler(state=From.tugmaadd)
async def all_users2(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		data = sql.execute(f"SELECT b_name FROM tugma WHERE b_name = '{message.text}'").fetchone()
		if data is None:
			try:
				sql.execute(
					f"""INSERT INTO tugma (b_name, face) VALUES ("{message.text}", 'face')""")
				db.commit()
				await state.finish()
				await message.reply("Yangi tugma qo'shildi🎉🎉", reply_markup=tugma_btn)
			except:
				await message.reply("Yangi tugma nomida xatolik bor, qaytadan kiriting",
									reply_markup=tugma_btn)
		else:
			await message.reply("Bu tugma avvaldan bor, boshqacharoq nom kiriting", reply_markup=tugma_btn)
		await state.finish()

@dp.message_handler(text = "❌🔘 Tugmani olib tashlash")
async def channelD(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await message.reply("O'chiriladigan tugmaning nomini yuboring", reply_markup=markup)
		await From.tugmaDelete.set()

@dp.message_handler(state=From.tugmaDelete)
async def ChannelDel(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		data = sql.execute(f"""SELECT b_name FROM tugma WHERE b_name = '{message.text}'""").fetchone()
		print(message.text)
		if data is None:
			await message.reply("Bunday tugma yo'q", reply_markup=tugma_btn)
		else:
			try :
				sql.execute(f'DELETE FROM tugma WHERE b_name = "{message.text}"')
				db.commit()
				await state.finish()
				await message.reply("Tugma muvaffaqiyatli o'chirildi", reply_markup=tugma_btn)
			except:
				await message.reply("Tugma nomi noto'gri kiritildi, iltimos qaytadan kiriting", reply_markup=tugma_btn)

		await state.finish()

@dp.message_handler(text = "📋🔘Tugmalar ro'yxati")
async def channelList(message: types.Message):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		list_admin = sql.execute("SELECT b_name from tugma").fetchall()
		admins = ''
		if len(list_admin) > 0:
			try:
				n = 0
				for admin in list_admin:
					n+=1
					admins += f"\n<b>{n}. <code>{admin[0]}</code></b>\n----------------------------"
				await message.reply(admins, reply_markup=tugma_btn)
			except:
				await message.reply(list_admin, reply_markup=tugma_btn)
		else:
			await message.reply("Hozircha tugmalar yo'q", reply_markup=tugma_btn)




############################                 info button       #####


@dp.message_handler(text = "ℹ️Tugmaga ma'lumot qo'shish")
async def clear1(message:types.Message, state: FSMContext):
	if message.from_user.id == main_admin:
		liss = sql.execute("SELECT user_id from admin").fetchall()
		Admin = [main_admin, ]
		for admin in liss:
			Admin.append(admin[0])
		if message.from_user.id in Admin:
			list_admin = sql.execute("SELECT b_name from tugma").fetchall()
			admins = ''
			if len(list_admin) > 0:
				try:
					n = 0
					for admin in list_admin:
						n += 1
						admins += f"\n<b>{n}. <code>{admin[0]}</code></b>\n----------------------------"
					await message.reply(f"Ma'lumot qo'shmoqchi bo'lgan tugmani nomini yuboring\n\n\nMavjud tugmalar:\n{admins}",
										reply_markup=markup)
					await From.btn_info.set()
				except:
					await message.reply("xato", reply_markup=tugma_btn)
					await state.finish()
			else:
				await message.reply("Sizda hozircha tugma yo'q, oldin tugma yarating", reply_markup=tugma_btn)
				await state.finish()

	else:
		await message.reply("Tugmaga faqatgina bot egasi ma'lumot kkiritishi mumkin")


@dp.message_handler(state=From.btn_info, text = "🔙Orqaga qaytish")
async def all_u(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		await state.finish()
		await message.reply("Orqaga qaytildi", reply_markup=tugma_btn)

@dp.message_handler(state=From.btn_info, content_types = "text")
async def channel_add(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		data = sql.execute(f"""SELECT b_name FROM tugma WHERE b_name = '{message.text}'""").fetchone()
		if data is None:
			await message.reply("Bunday tugma yo'q. oldin tugmani yarating", reply_markup=tugma_btn)
			await state.finish()
		else:
			await message.reply(
				"Tugmaga qo'shiladigan ma'lumotni yuboring\n\nDiqqat❗❗  Tugmaga faqat quyidagi malumot turlarini qo'shishingiz mumkin\n\n<b>• text\n• audio\n• document\n• photo\n• sticker\n• video\n• video_note\n• voice\n• location\n• contact</b>",
				reply_markup=markup)
			From.onesave = message.text
			await state.finish()
			await From.btn_nf.set()


@dp.message_handler(state=From.btn_nf, content_types = 'any')
async def channel_add(message: types.Message, state: FSMContext):
	liss = sql.execute("SELECT user_id from admin").fetchall()
	Admin = [main_admin, ]
	for admin in liss:
		Admin.append(admin[0])
	if message.from_user.id in Admin:
		sql.execute(
			f"""UPDATE tugma SET file_id = ? WHERE b_name = ? """, (message.message_id, From.onesave))
		db.commit()
		await message.reply("qo'shildi", reply_markup=tugma_btn)
		await state.finish()


