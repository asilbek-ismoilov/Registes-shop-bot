from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


# 1 - usul 
menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💻 Laptop"),KeyboardButton(text="📱 Phones")],
        [KeyboardButton(text="💁🏻‍♂️ About us"),KeyboardButton(text="📍 Location")],
        [KeyboardButton(text="☎️ Contact admin")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Tugmalardan birini tanlang ..."
)

# 2 - usul

computers = [
    "Mackbook",
    "Lenovo",
    "HP",
    "ASUS",
    "Victus",
    "ACER",
    "Samsung"
]

computer_button = ReplyKeyboardBuilder()

for computer in computers:
    computer_button.add(KeyboardButton(text=computer))

computer_button.adjust(2,repeat=True)

computer_button = computer_button.as_markup(
    resize_keyboard=True,
    input_field_placeholder="Choise computer..."
)



