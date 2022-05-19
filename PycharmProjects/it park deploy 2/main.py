import telebot
from telebot import types

token = '5087464579:AAHEwQ1fA65mkJURLL6dN-yM-nXYkAV-GoQ'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("IT Talim📈"),
                         types.KeyboardButton("Rezidentlar📑"),
                         types.KeyboardButton("StartUp↗️"),
                         types.KeyboardButton("IT Park Universiteti💻"),
                         types.KeyboardButton("Savollarizga javoblar❓"),
                         types.KeyboardButton("Administrator bilan bog'lanish📞"),
                         types.KeyboardButton("Viloyat markazlarining joylashuvi🏠"))

    bot.send_message(message.chat.id,
                     text="""{0} botimizga xush kelibsiz bu yerda siz bizning IT Parkimiz haqida hamma narsani bilib olishingiz mumkin""".format(
                         message.from_user.first_name), reply_markup=buttons)


@bot.message_handler(regexp="StartUp↗️")
def startup(message):
    bot.message_handler(message.chat.id,
                        "Shuningdek, biz startaplarni rag'batlantirishni faol qo'llab-quvvatlaymiz. Ayni damda bizda Aloqabank va Aloqaventures homiyligida tanlov o'tkazilmoqda.🤯\nBiz AloqaTech Lab tanlovini boshlaymiz\n“AloqaTech Lab” – bu 3 oylik korporativ akselerator bo‘lib, \nu ekspertlar ko‘magi, hamda, loyihalarni ishga tushirish uchun texnik, \nmoliyaviy va marketing yordamini o‘z ichiga oladi.")


@bot.message_handler(regexp="IT Park Universiteti💻")
def university(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Universitet haqida🤔"),
                         types.KeyboardButton("Fakultetlar⛺"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Siz IT Park unversiteti menyusiga o'tdingiz", reply_markup=buttons)


@bot.message_handler(regexp="Universitet haqida🤔")
def about_univ(message):
    bot.send_message(message.chat.id,
                     "Universitetimizda o'qish orqali siz quyidagilarni olasiz:\n<b>1) Ingliz tilini to'liq bilish🤯2) Mutaxassisligingizni to'liq bilish🕹️</b>\nDarslar ham onlayn tarzda olib boriladi.O'qishni tugatgandan so'ng siz bakalavr darajasini olasiz🏆""",
                     parse_mode="HTML")


@bot.message_handler(regexp="Fakultetlar⛺")
def fakultet(message):
    bot.send_message(message.chat.id,
                     "Bizda juda yuqori sifatli kurslar va darajasi Junior+ yoki Middledan past bo'lmagan o'qituvchilar mavjud. Bizda quyidagi fakultetlar mavjud\n<b>EPAM dan📙:</b>\n1) Back End Development💪\n2) Big Data🥇\n3) Front End Development💥\n4) Mobile Development📱\n5) Dasturiy ta'minotda QA🤯\n<b>IT Parkdan📗</b>:\n1) Web-ishlab chiqish⚡\n2) Software Testing🚀\n3) Tarmoqlar va virtual muhitlar🏆\n""",
                     parse_mode="HTML")


@bot.message_handler(regexp="Viloyat markazlarining joylashuvi🏠")
def rayonniy(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Zarbdor tumani"),
                         types.KeyboardButton("Sharof Rashidov tumani"),
                         types.KeyboardButton("Baxmal tumani"),
                         types.KeyboardButton("Paxtakor tumani"),
                         types.KeyboardButton("Forish tumani"),
                         types.KeyboardButton("Mirzacho'l tumani"),
                         types.KeyboardButton("G'allaorol tumani"),
                         types.KeyboardButton("Zomin tumani"),
                         types.KeyboardButton("Yangiobod tumani"),
                         types.KeyboardButton("Do'stlik tumani"),
                         types.KeyboardButton("Zafarobod tumani"),
                         types.KeyboardButton("Arnasoy tumani"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Siz viloyat markazlarning joylashuvi menyusiga o'tdingiz", reply_markup=buttons)


########################################### IT TALIM ###################################################################
@bot.message_handler(regexp="IT Talim📈")
# courses
def IT_talim(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Bizning kurslarimiz📚"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Siz IT Talim menyusiga o'tdingiz", reply_markup=buttons)


@bot.message_handler(regexp="Administrator bilan bog'lanish📞")
def social(message):
    inst = "[Bu bizning instagram akkauntimiz bu yerda siz It Parkdagi yangiliklarni kuzatib borishingiz mumkin✔](https://www.instagram.com/itpark_jizzax)"
    global_chat = "[Bu esa telegram kanalimiz bu yerda siz talabalarning taraqqiyotini kuzatishingiz mumkin😄](https://t.me/itpark_uz)"
    chat = "[Biz bilan muloqot qilmoqchi bo'lsangiz bu yerga kiring, bu yerda juda qiziqarli va ajoyib😊](https://t.me/joinchat/TxRYfFWJN0vP4UHs)"
    facebook = "[Bizni facebookda kuzating🖥](https://www.facebook.com/IT-Park-Jizzax-103116884984808)"
    site = "[Rasmiy saytimiz🔎](http://www.it-park.uz)"
    bot.send_message(message.chat.id, inst + '\n\n' + global_chat + '\n\n' + chat + '\n\n' + facebook + '\n\n' + site,
                     parse_mode="MarkdownV2")
    bot.send_message(message.chat.id,
                     "Murojat uchun va kurslarga yozilish uchun raqam telefon nomer☎⬇\n  <b>❗+998(99)0451199❗</b>",
                     parse_mode="HTML")


@bot.message_handler(regexp="Bizning kurslarimiz📚")
def courses(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Kompyuter savodxonligi💻"),
                         types.KeyboardButton("Front End Dasturlash💪"), types.KeyboardButton("Back End Dasturlash🧨"),
                         types.KeyboardButton("Python🐍"), types.KeyboardButton("IT matematika👩‍🔬"),
                         types.KeyboardButton("IT English📚"), types.KeyboardButton("Full stack🗻"),
                         types.KeyboardButton("3Ds Max🎓"), types.KeyboardButton("Grafik Dizayn🖌"),
                         types.KeyboardButton("Robototexnika🤖"), types.KeyboardButton("Unityda o'yin yaratish🎮"),
                         types.KeyboardButton("Orqaga qaytish🔙"))
    bot.send_message(message.chat.id, "Siz kurslar menyusiga o'tdingiz", reply_markup=buttons)


@bot.message_handler(regexp="Kompyuter savodxonligi💻")
def komp(message):
    bot.send_message(message.chat.id,
                     "Bu yerda siz Word, Excel, Power Point, Google sheets to'liq o'rganishingiz mumkin📑\nNarxi: 200.000 so'm\nDavomiyligi: 2 oy!")


@bot.message_handler(regexp="Front End Dasturlash💪")
def frontend(message):
    bot.send_message(message.chat.id,
                     "Front End-da siz HTML, CSS, Bootstrap, jQuery, JavaScript kabi tillarni o'rganishingiz mumkin🌪\nNarxi: 300.000 so'm\nDavomiyligi: 3 oy")


@bot.message_handler(regexp="Back End Dasturlash🧨")
def backend(message):
    bot.send_message(message.chat.id,
                     "Back End-da siz PHP va Python tillarini o'rganishingiz mumkin👌\nNarxi: 350.000 so'm\nDavomiyligi: 3-4 oy")


@bot.message_handler(regexp="IT matematika👩‍🔬")
def math(message):
    bot.send_message(message.chat.id,
                     "IT Matematika kursi sizga dasturlash uchun yaxshi matematikani o'rganishga yordam beradi📒\nNarxi: 150.000 so'm\nDavomiyligi: 4 oy")


@bot.message_handler(regexp="Python🐍")
def python(message):
    bot.send_message(message.chat.id,
                     "Python kursi juda tez rivojlanayotgan tildir. Uning afzalliklari shundaki, u juda tez va o'rganish oson🐍\nNarxi: 350.000 so'm\nDavomiyligi: 3-4 oy")


@bot.message_handler(regexp="Full stack🗻")
def fullstack(message):
    bot.send_message(message.chat.id,
                     "📌FullStack - bu har qanday tilni to'liq o'rgatish, ya'ni markazimizda ba'zi tillar FullStack ko'rinishida o'rgatiladi, ya'ni:\nHTML, CSS, Bootstrap, Python (mySQL, Django), JavaScript🖥\nNarxi: 300.000 so'm\nDavomiyligi: 5-6 oy")


@bot.message_handler(regexp="3Ds Max🎓")
def threed(message):
    bot.send_message(message.chat.id,
                     "3Ds max - bu 3D dunyosida grafik dizaynni o'rganishingiz mumkin bo'lgan kurs, ya'ni siz 3D ob'ektlar bilan ishlashingiz mumkin🚩\nNarxi: 400.000so'm\nDavomiyligi: 4-5 oy")


@bot.message_handler(regexp="IT English📚")
def eng(message):
    bot.send_message(message.chat.id,
                     "IT English kursi sizga dasturlash uchun kerak bo'ladigan ingliz tilini o'rganishga yordam beradi\nNarxi: 200.000 so'm\nDavomiyligi: 1,5 yil")


@bot.message_handler(regexp="Grafik Dizayn🖌")
def dizayn(message):
    bot.send_message(message.chat.id,
                     "Grafik dizayn kursi sizga 2D ob'ektlar bilan ishlashni yaxshiroq o'rganishga yordam beradi va IT o'yinlari sohasida sizga yordam beradi🤯\nNarxi: 300.000 so'm\nDavomiyligi: 3 oy")


@bot.message_handler(regexp="Robototexnika🤖")
def robototexnika(message):
    bot.send_message(message.chat.id,
                     "Robototexnika sizga mashinasozlikda yordam beradi, siz robotlarni ko'chirishingiz, sun'iy intellekt yaratishingiz va robotga qo'shishingiz mumkin, siz o'zingizning robotingizni yaratishingiz mumkin🛸\nNarxi: 300.000 so'm\nDavomiyligi: 3 oy")


@bot.message_handler(regexp="Unityda o'yin yaratish🎮")
def unity(message):
    bot.send_message(message.chat.id,
                     "Unityda o'yin - bu juda zarur kurs bo'lib, unda siz haqiqatan ham o'yinlar yaratish va ularni turli platformalarda sotish orqali pul ishlashingiz mumkin, Unity eng yaxshi platforma ekanligini va eng yaxshi o'yinlar unda yaratilganligini unutmasligimiz kerak🕹️\nNarxi:300.000 so'm\nDavomiyligi: 5 oy")


################################################################### END OF COURSES ##########################################################################3

@bot.message_handler(regexp="Orqaga qaytish🔙")
def back_it_talim(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("Bizning kurslarimiz📚"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Siz IT Talim menyusiga o'tdingiz", reply_markup=buttons)


########################################### IT TALIM ###################################################################

########################################### FAQ ###################################################################
@bot.message_handler(regexp="Savollarizga javoblar❓")
def question(message):
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("IT Park bu nima?🤔"),
                         types.KeyboardButton("Nima uchun bizni markazimiz?🤩"),
                         types.KeyboardButton("Dasturchi bu o'zi kim?🧑‍💻"),
                         types.KeyboardButton("Bizning o'quvchilar kurslarni tugatib nimaga qodir b'oladi?✔"),
                         types.KeyboardButton("Farzandingiz bizning markazda qanday imkoniyatlarga ega bo'ladi?🤔"),
                         types.KeyboardButton("Bizning joylanishuvimiz🏢"),
                         types.KeyboardButton('Orqaga qaytish⬅'))
    bot.send_message(message.chat.id, "Bu yerda, ehtimol, savollaringizga javob topishingiz mumkin",
                     reply_markup=buttons)


########################################### REZIDENT ###################################################################

@bot.message_handler(regexp="Rezidentlar📑")
def rezidents(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("AliTech"),
                         types.KeyboardButton("Code Vision"),
                         types.KeyboardButton("UzTan Media"),
                         types.KeyboardButton("UniTech IT business"),
                         types.KeyboardButton("Orqaga qaytish⬅"))
    bot.send_message(message.chat.id, "Siz rezidentlar menyusiga o'tdingiz", reply_markup=buttons)


########################################### REZIDENT ###################################################################

@bot.message_handler(content_types=['text'])
def answers(message):
    # rezidents
    if message.text == "AliTech":
        markup = types.InlineKeyboardMarkup()
        buttons = markup.add(types.InlineKeyboardButton(text='Saytiga tashrif buyurish', url="https://alitech.uz/"))
        bot.send_message(message.chat.id,
                         "Barch turdagi dasturlash xizmatlari ko'rsatuvchi hamda IT sohasiga o'qituvchi korxona",
                         reply_markup=buttons)

    if message.text == "Code Vision":
        markup = types.InlineKeyboardMarkup()
        buttons = markup.add(types.InlineKeyboardButton(text='Saytiga tashrif buyurish', url='https://codevision.uz/'))
        bot.send_message(message.chat.id,
                         "CRM tizimlari va web-saytlar ishlab chiqaruvchi korxona\n<b>P.S. CRM - bu mijozlar bilan munosabatlarni boshqarish va biznes jarayonlarini optimallashtirish usulidir. Ushbu yondashuvning asosiy komponenti CRM tizimi - etakchilar bilan ishlashni tashkil etish, mijozlar harakatlarini kuzatish va aloqalarni avtomatlashtirish uchun maxsus dastur hisoblanadi.</b>",
                         reply_markup=buttons, parse_mode="HTML")

    if message.text == "UzTan Media":
        markup = types.InlineKeyboardMarkup()
        buttons = markup.add(types.InlineKeyboardButton(text='Saytiga tashrif buyurish', url='https://uztan.uz/'))
        bot.send_message(message.chat.id,
                         "UzTan Media - Web-saytlar yaratuvchi va hosting yoki server ijarasi xizmatlarini taklif qiluvchi kompaniya.",
                         reply_markup=buttons)

    if message.text == "UniTech IT business":
        markup = types.InlineKeyboardMarkup()
        buttons = markup.add(
            types.InlineKeyboardButton(text='Saytiga tashrif buyurish', url='http://www.unitech.it/en/'))
        bot.send_message(message.chat.id,
                         "Web-platforma, web-saytlar chiqaruvchi korxona.", reply_markup=buttons)
    # rezidents

    if message.text == "Nima uchun bizni markazimiz?🤩":
        bot.send_message(message.chat.id,
                         """Bu savolga javob oddiy:\n1.🥇Bizda arzon narxlar bor\n2. ⭐Bizda sifatli treninglar mavjud\nBiz barcha markazlarning narxi haqida so'radik, \n<b>minimal 1.200.000 ediva maksimal 8.000.000 bizning markazda esa 200.000 so'mdan 500.000 so'mgacha turadi😉</b>""",
                         parse_mode="HTML")
    elif message.text == "Dasturchi bu o'zi kim?🧑‍💻":
        bot.send_message(message.chat.id,
                         """Ba'zi odamlar dasturchi so'zini eshitib, semiz va landovur odamni tasavvur qilishadi🤨. \nLekin dasturchilar aql bilan ishlashni yaxshi ko'radigan - o'qimishli va aqlli odamlar🧐. \nMening do'stim bor, bir dasturchi, uyda o'tirib kuniga atigi 3-4 soat ishlaydi va 2000 dollar topadi💵. \nU shunchaki aqlli uylarni programmalashtiradi xolos.\n❗Lekin faqatgina aqlli uylarni yaratishda to'xtab qolmaslik kerak, ahir butun dunyo raqamli texnologiyaga o`tmoqda❗\n. Dasturchilarga talab juda katta - oddiy yoritish tizimini dasturlashtan boshlab🔦 samolyotning murakkab  programmasini tuzishgacha. Kelajakda asosiy ishni dasturchi bajaradi, shuning uchun farzandingiz dasturchi bo'lsa afsuslanmaysiz💻""")
    elif message.text == "Bizning o'quvchilar kurslarni tugatib nimaga qodir b'oladi?✔":
        bot.send_message(message.chat.id,
                         """Bizning kurslarimizni tugatgandan so'ng, farzandingiz yoshidan qat'i nazar, mustaqil ravishda pul ishlash imkoniyatiga ega bo'ladi. U shaxsiy komissiyalarni bajarishi, mustaqil ishlarni bajarishi va boshqalarni bajarishi mumkin. Ya'ni, dasturlash yoshga qaramaydi. Asosiysi, mahorat. Python dasturlash tili juda tez rivojlanmoqda. Ushbu tilda siz mashinasozlik bilan shug'ullanishingiz mumkin, siz mobil ilovalar, shuningdek, o'yinlar va hatto telegram botlarini yaratishingiz mumkin. Bu farzandingiz egallaydigan daslabki bilim va qobiliyatlar, keyngi bosqichlarda oladigan bilimlari cheksiz qobilyatga ega bo'lishni taminlaydi📈""")
    elif message.text == "Farzandingiz bizning markazda qanday imkoniyatlarga ega bo'ladi?🤔":
        bot.send_message(message.chat.id,
                         """Bizning markazimizda pul mukofotlari bilan ko'plab musobaqalar o'tkaziladi, ular ham farzandingizning rivojlanishini oshiradi, chunki u qaysi joyni kutayotgani va qancha pul olishiga bog'liq bo'ladi. \n<b>❗Shuningdek, farzandingiz birinchi ish tajribasiga ega bo'lishi mumkin❗</b>, \nbiz bilan farzandingiz o'qituvchimizning yordamchisiga aylanishi mumkin, ya'ni kelajakda u o'qituvchi o'rnini egallashi mumkin, umuman olganda, IT Parkda biz sizga martaba o'sishini va'da qilamiz☺️💻""",
                         parse_mode="HTML")
    elif message.text == "Bizning joylanishuvimiz🏢":
        # bot.send_location(chat_id=message.chat.id, latitude=float(40.132368), longitude=float(67.823))
        bot.send_message(message.chat.id,
                         text="IT Park Jizzax filiali - Jizzax shahri, Sharof Rashidov shox ko'chasi, 63 uyda joylanishadi🤠\n<b>Jizzax hokimiyatni 2 qavati🏢</b>",
                         parse_mode="HTML")

    if message.text == "Zarbdor tumani":
        bot.send_message(message.chat.id, "Zarbdor tumani, Tinchlik MFY, Mustaqillik ko'chasi")
    if message.text == "Sharof Rashidov tumani":
        bot.send_message(message.chat.id,
                         "harof Rashidov tumani, Uchtepa dahasi, Yangiobod MFY, Mustaqillik ko'chasi, 2 uy")
    if message.text == "Baxmal tumani":
        bot.send_message(message.chat.id, "Baxmal tumani, O'smat shahar, Do'stlik MFY, Archazor ko'chasi, 9 uy")
    if message.text == "Paxtakor tumani":
        bot.send_message(message.chat.id, "Paxtakor tumani, Do'stlik MFY, Yunus Rajabiy ko'chasi, 9 uy")
    if message.text == "Forish tumani":
        bot.send_message(message.chat.id, "Forish tumani, O'zbekiston mahallasi, Do'stlik ko'chasi, 1 uy")
    if message.text == "Mirzacho'l tumani":
        bot.send_message(message.chat.id,
                         "Mirzachoʻl tumani, Gagarin shaharchasi, G'alaba MFY, Taraqqiyot ko'chasi, Yoshlar bog'i")
    if message.text == "G'allaorol tumani":
        bot.send_message(message.chat.id, "G'allaorol tumani, G'ofur G'ulom mahallasi, Mustaqillik ko'chasi, 38 uy")
    if message.text == "Zomin tumani":
        bot.send_message(message.chat.id, "Zomin tumani, Mustaqillik ko'chasi, 74 uy")
    if message.text == "Yangiobod tumani":
        bot.send_message(message.chat.id,
                         "Yangiobod tumani, Yangiobod shaharchasi, Yangiobod ShFY, Barkamol avlod koʻchasi")
    if message.text == "Do'stlik tumani":
        bot.send_message(message.chat.id, "Do'stlik tuman Chinobod MFY Do'stlik ko'chasi kinoteatr binosi.")
    if message.text == "Zafarobod tumani":
        bot.send_message(message.chat.id,
                         "Zafarobod tumani, Bo'ston MFY, Mustaqillik ko'chasi, Tuman pochta bo'limi binosi")
    if message.text == "Arnasoy tumani":
        bot.send_message(message.chat.id, "Arnasoy tuman, G'oliblar MFY kasb-hunar maktabi (kollleji) binosi")
    elif message.text == "Orqaga qaytish⬅":
        markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    buttons = markup.add(types.KeyboardButton("IT Talim📈"),
                         types.KeyboardButton("Rezidentlar📑"),
                         types.KeyboardButton("StartUp↗️"),
                         types.KeyboardButton("IT Park Universiteti💻"),
                         types.KeyboardButton("Savollarizga javoblar❓"),
                         types.KeyboardButton("Administrator bilan bog'lanish📞"),
                         types.KeyboardButton("Viloyat markazlarining joylashuvi🏠"))
    bot.send_message(message.chat.id, "Siz menyuga qaytdngiiz", reply_markup=buttons)


########################################## FAQ ###################################################################

if __name__ == '__main__':
    bot.polling(none_stop=True)