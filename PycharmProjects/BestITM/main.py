import telebot
from telebot import types

token = '5376494178:AAEaLwmPkEHeJKu0g18laNtA0PDR4Rs3Uf4'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Ta'lim📈"),
                         types.KeyboardButton("Savollarizga javoblar❓"),
                         types.KeyboardButton("Administrator bilan bog'lanish📞"))

    bot.send_message(message.chat.id,
                     text="""{0} botimizga xush kelibsiz bu yerda siz bizning Best ITM haqida hamma narsani bilib olishingiz mumkin""".format(
                         message.from_user.first_name), reply_markup=buttons)
# ======================================TALIM=============================================
@bot.message_handler(regexp="Ta'lim📈")
def about(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Bizning kurslarimiz📚"),
                         types.KeyboardButton("Bizning joylanishuvimiz🏢"),
                         types.KeyboardButton('Orqaga qaytish⬅')
                         )
    bot.send_message(message.chat.id, "Siz Ta'lim menyusiga o'tdingiz", reply_markup=buttons)


@bot.message_handler(regexp='Bizning kurslarimiz📚')
def courses(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Ingliz tili🏆"),
                         types.KeyboardButton("Ona tili va Adabiyot⛺"),
                         types.KeyboardButton("Matematika🔢"),
                         types.KeyboardButton("Rus tili🎀"),
                         types.KeyboardButton("Kimyo🔍"),
                         types.KeyboardButton("Biologiya🌿"),
                         types.KeyboardButton("Orqaga qaytish"))
    bot.send_message(message.chat.id, "Siz kurslar menyusiga o'tdingiz", reply_markup=buttons)

@bot.message_handler(regexp='Ingliz tili🏆')
def english(message):
    markup = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Beginner📖"),
                         types.KeyboardButton("Elementary📚"),
                         types.KeyboardButton("Pre-intermediate💪"),
                         types.KeyboardButton("Intermediate🔥"),
                         types.KeyboardButton("Pre-ielts💥"),
                         types.KeyboardButton("Ielts🤩"),
                         types.KeyboardButton("Orqaga qaytish👈"))
    bot.send_message(message.chat.id, "Siz Ingliz tili menyusiga o'tdingiz", reply_markup=buttons)


@bot.message_handler(regexp='Bizning joylanishuvimiz🏢')
def location(message):
    bot.send_location(message.chat.id, longitude=float(67.824177), latitude=float(40.130387))
    bot.send_message(message.chat.id, "Best ITM o'quv markazi shu yerda joylanishadi😁")
# ======================================================================================================================

# =========================================FAQ==========================================================================
@bot.message_handler(regexp="Savollarizga javoblar❓")
def faq(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Best ITM dars jadvali⏲️"),
                         types.KeyboardButton("Bizning ijtimoiy tarmoqlarimiz🌐"),
                         types.KeyboardButton("Best ITM o'quv markazi haqida🤔"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Bu yerda, ehtimol, savollaringizga javob topishingiz mumkin", reply_markup=buttons)


@bot.message_handler(regexp="Best ITM dars jadvali⏲️")
def time_table(message):
    img = open('time table best.jpg', 'rb')
    bot.send_photo(message.chat.id, img)
    img.close()

@bot.message_handler(regexp="Bizning ijtimoiy tarmoqlarimiz🌐")
def social(message):
    instagram = "[Best ITM instagram akkaunti✨](https://www.instagram.com/best_education_center_/)"
    kanal = "[Bizning asosiy telegram kanalimiz, bu yerda siz eng so'nggi yangiliklarni kuzatishingiz mumkin📰](t.me/BestITM)"
    site = "[Best ITMni rasmiy sayti🔍](www.bestedu.uz)"
    bot.send_message(message.chat.id, """BEST INNAVATSION TA'LIM MARKAZI
Ingli tili va rus tili kurslari
Abituriyentlar uchun kurslar
Bolalar uchun kurslar
Maktabga tayyorlov\n"""+'\n'+instagram+'\n\n'+kanal+'\n\n'+site, parse_mode='MarkdownV2')

@bot.message_handler(regexp="Best ITM o'quv markazi haqida🤔")
def about(message):
    bot.send_message(message.chat.id, """<b>Best ta'lim markazi 2011-yilda Muhitdinova Nazira Baxtirxanovna tomonidan ochilgan bo'lib, xozirda Jizzax shahrimizda 3 ta filliali mavjud.</b>🤯\n 📌Asosiy markaz Jizzax shahar Sayiljoyi mahallasi Nurbek restorani oldida joylashgan🏠.\n Best ta'lim markazida asosan ingliz tili kurslari mavjud bo'lib bundan tashqari rus tili, matematika, va \n<b>maktabgacha ta'lim (4 yoshdan 7 yoshgacha) guruhlarimiz mavjud.</b>\n Ikkinchi fillial 2020-yil Best Academy abituriyentlar markaziga asos solindi. \n<b> 📌Manzil Sayiljoyi mahallasi Simple cafe ro'parasi📌.</b>\n Va 3-fillial esa Zargarlik mahallasi Toshkent market yonida ochildi. <b>❗Eng asosiysi bizning o'quv markazda talim sifati yuqori darajada hisoblanadi.❗</b>""", parse_mode="HTML")
# ====================================================================================================================

# ================================================ADMIN=================================================================
@bot.message_handler(regexp="Administrator bilan bog'lanish📞")
def admin(message):
    bot.send_message(message.chat.id, "Murojat uchun va kurslarga yozilish uchun raqam telefon nomer☎⬇ \n❗ +998995560046 ❗\n❗ +998985710046 ❗\n❗ +998333600046 ❗️")
# =====================================================================================================================


# ============================================TEXT======================================================================
@bot.message_handler(content_types=['text'])
def text(message):
    # ==================================back buttons===========================================
    if message.text == 'Orqaga qaytish⬅':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        buttons = markup.add(types.KeyboardButton("Ta'lim📈"),
                             types.KeyboardButton("Savollarizga javoblar❓"),
                             types.KeyboardButton("Administrator bilan bog'lanish📞"))
        bot.send_message(message.chat.id, "Siz bosh menyuga o'tdingiz", reply_markup=buttons)

    if message.text == 'Orqaga qaytish':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        buttons = markup.add(types.KeyboardButton("Bizning kurslarimiz📚"),
                             types.KeyboardButton("Bizning joylanishuvimiz🏢"),
                             types.KeyboardButton('Orqaga qaytish⬅')
                             )
        bot.send_message(message.chat.id, 'Siz orqaga qaytdingiz', reply_markup=buttons)

    if message.text == 'Orqaga qaytish👈':
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        buttons = markup.add(types.KeyboardButton("Ingliz tili🏆"),
                             types.KeyboardButton("Ona tili va Adabiyot⛺"),
                             types.KeyboardButton("Matematika🔢"),
                             types.KeyboardButton("Rus tili🎀"),
                             types.KeyboardButton("Kimyo🔍"),
                             types.KeyboardButton("Biologiya🌿"),
                             types.KeyboardButton("Orqaga qaytish"))
        bot.send_message(message.chat.id, "Siz kurslar menyusiga qaytdingiz", reply_markup=buttons)
    # ========================================courses============================================
    if message.text == 'Ona tili va Adabiyot⛺':
        bot.send_message(message.chat.id, "❗ Ona tili va Adabiyot o'rganish kerak bo'lgan eng muhim fanlardir ❗, \nchunki Ona tili va Adabiyot siz, biz ona tilimizda gapira olmaymiz biz qarindoshlar, do'stlar bilan to'g'ri gaplasha olmaymiz.🤯\n<b>Narxi:190.000 so'm</b>", parse_mode='HTML')
    if message.text == "Matematika🔢":
        bot.send_message(message.chat.id, "Matematika eng zarur va ayni paytda eng qiyin fan😐, ammo bizning o'quv markazimizda u sizga osonlik bilan beriladi.😁\n<b>Narxi:190.000 so'm</b>", parse_mode="HTML")
    if message.text == "Rus tili🎀":
        bot.send_message(message.chat.id, "<b>Rus tili ham eng zarur til</b>,\n chunki O‘zbekiston aholisining deyarli yarmi rus tilida so‘zlashadi\n<b>Narxi:160.000 so'm</b>", parse_mode="HTML")
    if message.text == "Kimyo🔍":
        bot.send_message(message.chat.id, "Kimyo aniq fanlar sohasidagi eng qiyin fanlardan biridir📌. \nAgar siz kimyoni bilsangiz, o'zingizni allaqachon boy deb hisoblang, chunki kimyo muvaffaqiyat kalitidir\n <b>Narxi:190.000 so'm</b>", parse_mode="HTML")
    if message.text == "Biologiya🌿":
        bot.send_message(message.chat.id, "Biologiya eng qiziqarli fan, chunki o'simliklarni, inson tanasining tuzilishini o'rganish juda qiziq🤔\n<b>Narxi: 190.000 so'm</b>", parse_mode="HTML")
    if message.text == "Beginner📖":
        bot.send_message(message.chat.id, "Bu kirish darajasi bo'lib, ingliz tilini o'rganishga ingliz tilini umuman bilmaydigan odamlar tashrif buyurishadi😁\n<b>Narxi:160.000 so'm</b>", parse_mode="HTML")
    if message.text == "Elementary📚":
        bot.send_message(message.chat.id, "Bu ingliz tilini o'rganishning 2-bosqichi. Ushbu bosqichni tugatganingizdan so'ng siz kitoblarni to'liq o'qish imkoniyatiga ega bo'lasiz.🤯\n<b>Narxi:170.000 so'm</b>", parse_mode="HTML")
    if message.text == "Pre-intermediate💪":
        bot.send_message(message.chat.id, "Ushbu bosqichda siz allaqachon ingliz tilining yarmini bilasiz. Siz kitoblarni erkin o'qiy olasiz, podkastlarni tinglaysiz va matnni to'liq tushunasiz, shuningdek, qisman insho yozishingiz mumkin bo'ladi.😎\n<b>Narxi:180.000 so'm</b>", parse_mode="HTML")
    if message.text == "Intermediate🔥":
        bot.send_message(message.chat.id, "Siz allaqachon IELTS imtihonini topshirish uchun yo'ldasiz. Ushbu bosqichda siz o'rganishingiz va o'rganishingiz kerak, chunki bu eng qiyin bosqich.🤗\n,<b>Narxi:190.000 so'm</b>", parse_mode="HTML")
    if message.text == "Pre-ielts💥":
        bot.send_message(message.chat.id, "Tabriklaymiz, siz allaqachon barcha ingliz tili kurslarini tugatdingiz. Ushbu bosqichda siz avval o'tgan barcha narsalarni birlashtirasiz va ingliz tilini to'liq bilasiz. <b>📌Ammo unutmangki, hamma narsa o'qituvchilarga bog'liq emas, shuning uchun siz ham o'zingiz o'rganishingiz kerak.\nNarxi:190.000 so'm</b>", parse_mode="HTML")
    if message.text == "Ielts🤩":
        bot.send_message(message.chat.id, "Siz ushbu kursni tamomlaganingizdan so'ng ingliz tilini o'rganishning so'nggi bosqichiga yetib keldingiz, \nsiz IELTS imtihonidan kamida 6,0 ball to'plash imkoniyatiga ega bo'lasiz. Bu erda siz imtihondan o'tishning barcha tafsilotlarini muhokama qilasiz.😎\n<b>Narxi:200.000 so'm</b>", parse_mode="HTML")

if __name__ == '__main__':
    bot.polling(none_stop=True)
