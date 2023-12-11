from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

btn = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📆 Darslar jadvali 📆"),
        KeyboardButton(text="Maktab haqida")],
        [ #KeyboardButton(text="📖 Elektron kitoblar 📖"),
        KeyboardButton(text="✳️ Foydali ✳️")
        ],
        [KeyboardButton(text="🧑🏻‍💻 Bot Yaratuvchisi 🧑🏻‍💻")]
    ]
)

dars_jadvali = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="1-sinf"),
         KeyboardButton(text="2-sinf")],
        [KeyboardButton(text="3-sinf"),
         KeyboardButton(text="4'A'-sinf")],
        [KeyboardButton(text="4'B'-sinf"),
         KeyboardButton(text="5-sinf")],
        [KeyboardButton(text="6-sinf"),
         KeyboardButton(text="7-sinf")],
        [KeyboardButton(text="8-sinf"),
         KeyboardButton(text="9-sinf")],
        [KeyboardButton(text="10-sinf"),
         KeyboardButton(text="11-sinf")],
        [KeyboardButton(text="🔙 Orqaga qaytish 🔙")]
    ]
)

maktab_about = ReplyKeyboardMarkup(resize_keyboard=True,
    keyboard=[
        [KeyboardButton(text="📍 Maktab joylashuvi 📍")],
        # [KeyboardButton(text="👩🏼‍🏫 O'qituvchilar 👩🏼‍🏫"),
        #  KeyboardButton(text="Ma'muriyat")],
        [KeyboardButton(text="🔙 Orqaga qaytish 🔙")]
    ]
)


# e_book = ReplyKeyboardMarkup(resize_keyboard=True,               
#     keyboard=[
#         [KeyboardButton(text="Maktab darsliklar"),
#          KeyboardButton(text="Turli xil kitoblar")],
#         [KeyboardButton(text="🔙 Orqaga qaytish 🔙")]
#     ]
# )

# maktab_book = ReplyKeyboardMarkup(resize_keyboard=True,
#     keyboard=[
#         [KeyboardButton(text="1-sinf darsliklar")],
#         [KeyboardButton(text="2-sinf darsliklar")],
#         [KeyboardButton(text="3-sinf darsliklar")],
#         [KeyboardButton(text="4-sinf darsliklar")],
#         [KeyboardButton(text="5-sinf darsliklar")],
#         [KeyboardButton(text="6-sinf darsliklar")],
#         [KeyboardButton(text="7-sinf darsliklar")],
#         [KeyboardButton(text="8-sinf darsliklar")],
#         [KeyboardButton(text="9-sinf darsliklar")],
#         [KeyboardButton(text="10-sinf darsliklar")],
#         [KeyboardButton(text="11-sinf darsliklar")],
#         [KeyboardButton(text="🔙 Orqaga qaytish 🔙")]
#     ]
#     )

# book_class_1 = ReplyKeyboardMarkup(resize_keyboard=True,
#     keyboard=[
#         [KeyboardButton(text="Alifbe"),
#          KeyboardButton(text="Matematika")],
#         [KeyboardButton(text="Ona tili va o'qish savodxonligi")],
#         [KeyboardButton(text="Tarbiya"),
#          KeyboardButton(text="Musiqa")],
#         [KeyboardButton(text="Tabiiy fanlar")],
#         [KeyboardButton(text="Ingliz tili"),
#          KeyboardButton(text="Nemis tili")]
#     ]
#     )

# book_class_2 = ReplyKeyboardMarkup(resize_keyboard=True,
#     keyboard=[
#         [KeyboardButton(text="Ona tili va o'qish savodxonligi 2-sinf")],
#         [KeyboardButton(text="Matematika"),
#          KeyboardButton(text="Tabiiy fanlar")],
#         [KeyboardButton(text="Musiqa"),
#          KeyboardButton(text="Texnologiya")],
#         [KeyboardButton(text="Ingliz tili"),
#          KeyboardButton(text="Rus tili")]
#     ]
#     )

