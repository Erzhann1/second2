
from operator import indexOf
import re
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,

)

from telegram.ext import (
    CallbackContext,
    Updater,
    CommandHandler,
    PicklePersistence,
    Filters,
    MessageHandler,
    updater,
    CallbackQueryHandler
)
from menu import course_menu_keyboard, main_menu_keyboard
from key_button import tele_button, course_menu
from message import info_fg, ogogo_info, zapis_ogogo
from bot import TOKEN

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Добро пожаловать, {username}. Выберите опцию: ".format(
        username = update.effective_user.first_name\
            if update.effective_user.first_name is not None \
                else update.effective_user.username
    ),
    reply_markup=main_menu_keyboard()


    )


COURSE_REGEX1 = r"(?=("+(tele_button[1]) + r"))"
INFO_REGEX1 = r"(?=("+(tele_button[2]) + r"))"
METAP_REGEX1 = r"(?=("+(tele_button[0]) + r"))"
ZAPIS_REGEX = r"(?=("+(tele_button[3]) + r"))"

PYTHON_REGEX = r"(?=("+(course_menu[0]) + r"))"

JS_REGEX = r"(?=("+(course_menu[1]) + r"))"

UXUI_REGEX = r"(?=("+(course_menu[2]) + r"))"

BACK_REGEX = r"(?=("+(course_menu[3]) + r"))"



def receive_course_menu(update: Update, context: CallbackContext):
    info = re.match(COURSE_REGEX1, update.message.text)
    update.message.reply_text(
        "Выберите курс",
        reply_markup=course_menu_keyboard()
    )



def python_inline_menu(update: Update, context: CallbackContext):
    info = re.match(PYTHON_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Mentor", callback_data='mentor')],
        [InlineKeyboardButton("Lesson", callback_data='lesson')],
        [InlineKeyboardButton("Price", callback_data='price')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Что вас интересует",
        reply_markup=reply_markup1
    )
def zapis(update: Update, context: CallbackContext):
    info=re.match(ZAPIS_REGEX, update.message.text)
    update.message.reply_text(
        zapis_ogogo
    )

def zapisat(update: Update, context: CallbackContext):  
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
           chat_id = '@ogogo00',
           text = z
        ) 





def mitap_inline(update: Update, context: CallbackContext):
    info = re.match(METAP_REGEX1, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Sobytia", callback_data='sobytia')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Что вас интересует",
        reply_markup=reply_markup1
    )
def def_back_inline(update: Update, context: CallbackContext):
    info = re.match(BACK_REGEX, update.message.text)
    update.message.reply_text(
        "вы вернулись назад",
         reply_markup=main_menu_keyboard()
    )

def java_script_inline_menu(update: Update, context: CallbackContext):
    info = re.match(JS_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Mentor", callback_data='jsmentor')],
        [InlineKeyboardButton("Lesson", callback_data='jslesson')],
        [InlineKeyboardButton("Price", callback_data='jsprice')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Что вас интересует",
        reply_markup=reply_markup1
    )

def ux_ui_inline_menu(update: Update, context: CallbackContext):
    info = re.match(UXUI_REGEX, update.message.text)
    keyboard = [
        [InlineKeyboardButton("Mentor", callback_data='uumentor')],
        [InlineKeyboardButton("Lesson", callback_data='uulesson')],
        [InlineKeyboardButton("Price", callback_data='uuprice')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Что вас интересует",
        reply_markup=reply_markup1
    )

def info_inline_menu(update: Update, context: CallbackContext):
    info = re.match(INFO_REGEX1, update.message.text)
    keyboard = [
        [InlineKeyboardButton("OgogoPhoto", callback_data='ogogo_photo')],
        [InlineKeyboardButton("Ogogo_info", callback_data='ogogo_info')],
        [InlineKeyboardButton("Ogogo_location", callback_data='ogogo_location')],
    ]
    reply_markup1 = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Что вас интересует",
        reply_markup=reply_markup1
    )


def inline_buttons(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Mentor", callback_data='mentor')],
        [InlineKeyboardButton("Lesson", callback_data='lesson')],
        [InlineKeyboardButton("Price", callback_data='price')],
    ]
    reply_markup1=InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
 


    if query.data =='mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/mentor.jpg', 'rb'),
            caption ="""
            name: Человек паук,
            exep: 5 year,
            kompany: google
            """,
            reply_markup = reply_markup1   
        )
    
    if query.data =='lesson':
        query.edit_message_text(
            text="""
            5 раз в неделю по 3 часа
            """,
        reply_markup=reply_markup1
        )
    if query.data =='price':
        query.edit_message_text(
            text="""
            Стоимость полного курса 16000 сом
            """,
        reply_markup=reply_markup1
        )


    if query.data =='jsmentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/mentor2.jpg', 'rb'),
            caption ="""
            name: Доктор стрендж,
            exep: 5 year,
            kompany: google
            """,
            reply_markup=reply_markup1   
        )
    
    if query.data =='jslesson':
        query.edit_message_text(
            text="""
            5 раз в неделю по 3 часа
            """,
        reply_markup=reply_markup1
        )
    if query.data =='jsprice':
        query.edit_message_text(
            text="""
            Стоимость полного курса 16000 сом
            """,
        reply_markup=reply_markup1
        )


    if query.data =='uumentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/mentor3.jpg', 'rb'),
            caption ="""
            name: Желеезный человек,
            exep: 7 year,
            kompany: google
            """,
            reply_markup=reply_markup1   
        )
    
    if query.data =='uulesson':
        query.edit_message_text(
            text="""
            5 раз в неделю по 3 часа
            """,
        reply_markup=reply_markup1
        )
    if query.data =='uuprice':
        query.edit_message_text(
            text="""
            Стоимость полного курса 16000 сом
            """,
    reply_markup=reply_markup1
        )

    if query.data == 'ogogo_photo':
        query.message.reply_photo(
        'https://ogogo.kg/academy-banner.png'
        )


    if query.data =='ogogo_info':
        query.message.reply_text(
           ogogo_info
        )
# 42.8736143207455, 74.61981136310733
    if query.data =='ogogo_location':
        query.message.reply_location(
            longitude=74.61981136310733,
            latitude=42.8736143207455
        
        )    


    if query.data =='sobytia':
        query.message.reply_text(
            info_fg
        ) 
    

updater = Updater(TOKEN, persistence=PicklePersistence(filename='bot_data'))
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX1),
    receive_course_menu

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON_REGEX),
    python_inline_menu

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS_REGEX),
    java_script_inline_menu

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(UXUI_REGEX),
    ux_ui_inline_menu

))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(INFO_REGEX1),
    info_inline_menu

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(METAP_REGEX1),
    mitap_inline

))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_REGEX),
    def_back_inline

))    
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS_REGEX),
    zapis   

))


updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
    ))






updater.dispatcher.add_handler(CallbackQueryHandler(inline_buttons))

updater.start_polling()
updater.idle()



