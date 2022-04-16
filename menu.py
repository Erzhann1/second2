import telegram
from key_button import tele_button, course_menu

def main_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(tele_button[0])
    ],
    [    
        telegram.KeyboardButton(tele_button[1]),
        telegram.KeyboardButton(tele_button[3])
    ],
    [       
        telegram.KeyboardButton(tele_button[2])
    ]
    
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )


def course_menu_keyboard():
    keyboard=([
    [
        telegram.KeyboardButton(course_menu[0]),
        telegram.KeyboardButton(course_menu[1])
    
    ],
    [    
        telegram.KeyboardButton(course_menu[2]),
        telegram.KeyboardButton(course_menu[3])

    ],       
         
    ])
    return telegram.ReplyKeyboardMarkup(
        keyboard, resize_keyboard=True, one_time_keyboard=False
    )

