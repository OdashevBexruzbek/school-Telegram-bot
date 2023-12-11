#19-maktab uchun bot. 27.09.2023/15:35 da kod yozishni boshlandi
#buttonlar->dars jadvali, maktab haqida, o'qituvchilar, o'quvchilar->sinflar->1,2,3,4,5,6,7,8,9,10,11, 
#lokatsiya, sinflarni elektron kitoblari, foydali, admin, talim yangiliklari

from aiogram import Router, Bot, Dispatcher, F, types, html
from aiogram.types import Message, FSInputFile, keyboard_button, InlineKeyboardButton, InlineKeyboardMarkup,InputFile
from aiogram.filters.command import Command
from aiogram.utils.keyboard import KeyboardBuilder, InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types.dice import DiceEmoji
from asyncio import run
from time import sleep
from random import choice
from buttons import btn, dars_jadvali, maktab_about #e_book "uquvchilar" malumot add bo'lgandan keyin ishlatiladi
# from random import choice   #bu kerak bo'lishi mumkin

token = "6685488260:AAGzrPL6-r6mayXpZe3kREq-BIjHcVfwXU8"
bot  = Bot(token=token)
dp = Dispatcher(bot=bot)

class Maktab:
    def __init__(self, token=token) -> None:
        self.dp = Dispatcher()
        self.bt = Bot(token)

    async def start_massage(self, msg: Message):
        name = msg.from_user.full_name
        await msg.answer(f"Assalomu alaykum {name} Andijon viloyati Ulug'nor tumani 19-umumiy o'rta ta'lim maktabi botiga xush kelibsiz. \n \n Quyida menulardan birini tanlang 👇", reply_markup=btn)

    async def button_message(self, msg:Message):
        if msg.text == "📆 Darslar jadvali 📆":
            await msg.answer(f"Sinfingizni tanlang ", reply_markup=dars_jadvali)

    async def dars_jadaval1(self, msg:Message):    
        if msg.text == "1-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHE2VbXCPFiK--8K_GKILq26uV0e8AA_PYMRu49eBKd8IoTybTNYQBAAMCAAN5AAMzBA", reply_markup=dars_jadvali, caption="1-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval2(self, msg:Message):
        if msg.text == "2-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHFWVbXHAiKKULm0HLY6oWMWpyMps0AAL12DEbuPXgSq37GWP13-jVAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="2-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval3(self, msg:Message):
        if msg.text == "3-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHF2VbXJS9vXVq6XX76yVRgPC0yxqNAAL62DEbuPXgStNobMCNNK4XAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="3-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval4a(self, msg:Message):
        if msg.text == "4'A'-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHGWVbXLtCReVbIk-6hHmg8hBxD--HAAL92DEbuPXgSoq5YykXBsL6AQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="4'A'-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval4b(self, msg:Message):
        if msg.text == "4'B'-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHG2VbXNY81yO0GDGJoTEkM9bb8GTUAAIB2TEbuPXgSsRU1Ns77loGAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="4'B'-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval5(self, msg:Message):
        if msg.text == "5-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHHWVbXP7OpQop2RxJkVqb8LdHumLIAAID2TEbuPXgSvkpJdOCWtdoAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="5-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval6(self, msg:Message):
        if msg.text == "6-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHH2VbXRpbdGYdEipPWK_gHSq7w0zdAAIP2TEbuPXgShb95GhSUNrlAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="6-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval7(self, msg:Message):
        if msg.text == "7-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHIWVbXWBzCJmMeN5UjbACPUiXDruZAAI12TEbuPXgSkOl8UZ7_JCHAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="7-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval8(self, msg:Message):
        if msg.text == "8-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHI2VbXZfIxvovF462rq8IHypyDJ49AAI52TEbuPXgSo8jFJu7R6H8AQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="8-sinf uchun haftalik dars jadvali") 
    
    async def dars_jadaval9(self, msg:Message):
        if msg.text == "9-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHJWVbXnEFhjMBi847lpLUytNERqIfAAJG2TEbuPXgSuJ9b4hcwiooAQADAgADeAADMwQ", reply_markup=dars_jadvali, caption="9-sinf uchun haftalik dars jadvali")
    
    async def dars_jadaval10(self, msg:Message):
        if msg.text == "10-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHJ2VbXoZB3uoSE08jQcE0u719bz4NAAJH2TEbuPXgSkSEt88FxFrVAQADAgADeQADMwQ", reply_markup=dars_jadvali, caption="10-sinf uchun haftalik dars jadvali") 
    
    async def dars_jadaval11(self, msg:Message):
        if msg.text == "11-sinf":
            await msg.answer_photo(photo="AgACAgIAAxkBAAIHKWVbXp2mAAEweCXO_-Qr2sR3_Th3KgACSNkxG7j14Er9bBDJhSRv2gEAAwIAA3kAAzME", reply_markup=dars_jadvali, caption="11-sinf uchun haftalik dars jadvali")
            msg.answer.__repr__
        if msg.text == "🔙 Orqaga qaytish 🔙":
            await msg.answer(f"Quyidagi menulardan birini tanlang 👇", reply_markup=btn)
        

    async def about_school(self, msg:Message):
        print("ishladi")
        if msg.text == "Maktab haqida":
            await msg.answer("Hozircha quyidagi menular mavjud 👇", reply_markup=maktab_about)
        if msg.text == " 🔙 Orqaga qaytish 🔙 ":
            await msg.answer(reply_markup=btn)

    async def mk_loc(self, msg:Message):
        if msg.text == "📍 Maktab joylashuvi 📍":
            await msg.answer_location(latitude=40.8568767, longitude=71.6881783)

    #o'qituvchilar
    # async def teacher(self, msg:Message):
    #     txt = "👩🏼‍🏫 O'qituvchilar 👩🏼‍🏫"
    #     if msg.text == txt:
    #         text = f"Teshaboyea Durdona-Ona tili va adabiyot fani o'qituvchisi. \n Tojiboyeva Mohidil - Algebra fani o'qituvchisi. \n Bo'stonova Gulnora - nemis tili va ingliz tili fani o'qituvchisi. \n Qayumova Umida - informatika fani o'qituvchisi. \n Bozorova Munojat - biologiya va kimyo fani o'qituvchisi.\n Ismoilova Soraxon - ona tili va adabiyot fani o'qituvchisi. \n Boyqo'ziyeva Oysuluv - fizika, texnologiya va astronomiya fani o'qituvchisi \n\n Bu bo'limga o'qituvchilar haqida ma'lumotlar kiritiladi!"
    #         await msg.answer(text)
   
    #elektron kitiblar
    # async def e_books(self, msg:Message):
    #     if msg.text == "📖 Elektron kitoblar 📖":
    #         await msg.answer(f"Sinfingizni tanlang ",reply_markup=e_book)

    async def send_book(self, msg:Message):
        if msg.text == "1-sinflar  ":
            await msg.answer_document(document="", caption="1-sinf uchun kitoblar")
            await msg.answer("Habar keldimi")
        if msg.text == "2-sinflar":
            await msg.answer_document(document="", caption="2-sinf uchun kitoblar")
        if msg.text == "3-sinflar":
            await msg.answer_document(document="", caption="3-sinf uchun kitoblar")
        if msg.text == "4-sinflar":
            await msg.answer_document(document="", caption="4-sinf uchun kitoblar")
        if msg.text == "5-sinflar":
            await msg.answer_document(document="", caption="5-sinf uchun kitoblar")
       

        if msg.text == "🔙 Orqaga qaytish 🔙":
            await msg.answer(f"Quyidagi menulardan birini tanlang 👇", reply_markup=btn)

  
    #foydali
    async def foydali(self, msg:Message):
        await msg.answer("O'quvchilar uchun foydali saytlar\n\n 1. kitob.uz -> Bu saytda 3200 ortiq elektron, 1000 dan oshiq audio kitoblar mavjud.\n\n 2. Codecademy.com — dasturlashni interaktiv usulda o’rganish. \n\n 3. Stuk.io — boshlang’ich bosqichdan boshlab dasturlashni o’rganish. \n\n4. Udacity.com — Google, Facebook, mongoDB, AT&T va boshqa kompaniyalar kurslari. \n\n5. duolingo.com   Xorijiy tillarni bepul o'rgatadigan web-sayti, Bu saytni telefonlar uchun ilovasi ham mavjud.\n\n6. coursera.com dunyo oliygohlarining eng yaxshi o'qituvchilarining bepul kurslari.\n\n7. w3schools.com bu sayt orqali ko'plab dasturlash tillarini o'rganishiz mumkin.\n\n8. memrise.com 11ta tilda so'z boyligingizni oshiruvchi ajoyib sayt.")
    #yangiliklar
    async def edu_news(self, msg:Message):
        if msg.text == "🆕 Ta'lim yangiliklar 🆕":
            davomi = "https://m.facebook.com/story.php?story_fbid=pfbid06WZXqRzeL6v2ru5j8jaDkpYX8N2qqJUBiJfi6B8ZeGJXudE4jJtoxxEuvyDTzdqvl&id=100022449543403&eav=Afas1jUmN58qGZEWBQNkSraAAbrB7H-KYBGgBOCSNq8yzgDV6oo-38zx7rUVphb--Ks&m_entstream_source=permalink&paipv=0"
            await msg.answer("1. Talabaning 80 daqiqa maruza tinglashi samarasiz — professor. \n Professor Baxtiyor Mengliyev oliy ta’lim vaziri Ibrohim Abdurahmonovga murojaat qildi. \n\n 2.Коллеж ва техникумларда ўқиётган хотин-қизлар давлат гранти асосида ўқишлари мумкин. Вазирлар Маҳкамасининг тегишли қарори (29.09.2023-йилдаги 516-сон)га мувофиқ, коллеж ва техникумларда қурилиш, транспорт, коммунал қишлоқ хўжалиги соҳаларида таълим олаётган қизлар тўлиқ давлат гранти асосида таълим олишлари мумкин.")

    async def admin(self, msg:Message):
        # if msg.text == " 🧑🏻‍💻 Bot Yaratuvchisi 🧑🏻‍💻 ":
            await msg.answer("Bot haqida fikr va takliflar bo'lsa @tme_admins ga yozishingiz mumkin.")

    async def add_photo(self, msg:Message):
        await msg.answer_photo(photo=f'{msg.photo[-1].file_id}')
        print(msg.photo[-1].file_id)

    async def orqaga(self, msg:Message):
        if msg.text == "🔙 Orqaga qaytish 🔙":
            await msg.answer(f"Quyidagi menulardan birini tanlang 👇", reply_markup=btn)

    def register(self):
        self.dp.message.register(self.start_massage,
                             Command(commands="start"))
        self.dp.message.register(self.button_message, F.text == "📆 Darslar jadvali 📆")
        self.dp.message.register(self.add_photo, F.content_type == "photo")
        self.dp.message.register(self.orqaga, F.text == "🔙 Orqaga qaytish 🔙")
        self.dp.message.register(self.dars_jadaval1, F.text == "1-sinf")
        self.dp.message.register(self.dars_jadaval2, F.text == "2-sinf")
        self.dp.message.register(self.dars_jadaval3, F.text == "3-sinf")
        self.dp.message.register(self.dars_jadaval4a, F.text == "4'A'-sinf")
        self.dp.message.register(self.dars_jadaval4b, F.text == "4'B'-sinf")
        self.dp.message.register(self.dars_jadaval5, F.text == "5-sinf")
        self.dp.message.register(self.dars_jadaval6, F.text == "6-sinf")
        self.dp.message.register(self.dars_jadaval7, F.text == "7-sinf")
        self.dp.message.register(self.dars_jadaval8, F.text == "8-sinf")
        self.dp.message.register(self.dars_jadaval9, F.text == "9-sinf")
        self.dp.message.register(self.dars_jadaval10, F.text == "10-sinf")
        self.dp.message.register(self.dars_jadaval11, F.text == "11-sinf")
        self.dp.message.register(self.about_school, F.text == "Maktab haqida")
        self.dp.message.register(self.mk_loc, F.text=="📍 Maktab joylashuvi 📍")
        # self.dp.message.register(self.teacher, F.text=="👩🏼‍🏫 O'qituvchilar 👩🏼‍🏫")
        self.dp.message.register(self.e_books, F.text=="📖 Elektron kitoblar 📖")
        self.dp.message.register(self.edu_news, F.text=="🆕 Ta'lim yangiliklar 🆕")
        self.dp.message.register(self.foydali, F.text=="✳️ Foydali ✳️")
        self.dp.message.register(self.admin, F.text=="🧑🏻‍💻 Bot Yaratuvchisi 🧑🏻‍💻")
        self.dp.message.register(self.button_message)
        # self.dp.message.register(self.teacher)


    async def start(self):
        self.register()
        try:
            await self.dp.start_polling(self.bt)
        except:
            await self.bt.session.close()

if __name__ == "__main__":
    mn = Maktab()
    run(mn.start())