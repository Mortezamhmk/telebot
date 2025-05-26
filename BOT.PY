# telebot
import telebot
from telebot import types

API_TOKEN = ""
BOT_USERNAME = ""
CHANNEL_USERNAME = ""  
bot = telebot.TeleBot(API_TOKEN)

def check_user_subscription(user_id):
     "عضویت"
    try:
        
        chat_member = bot.get_chat_member(f"@{CHANNEL_USERNAME}", user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """دستور /start برای بررسی عضویت و ارسال فایل‌ها"""
    user_id = message.from_user.id

    if check_user_subscription(user_id):
        bot.reply_to(message, "✅ شما به کانال پیوستید! حالا می‌توانید فایل‌ها را دریافت کنید.")
        # اینجا می‌توانید کد ارسال فایل را قرار دهید
        # مثال:
        # bot.send_document(message.chat.id, document_file_id)
    else:
        markup = types.InlineKeyboardMarkup()
        join_button = types.InlineKeyboardButton(
            text="📢 عضویت در کانال", url=f"https://t.me/{CHANNEL_USERNAME}"
        )
        markup.add(join_button)
        bot.send_message(
            message.chat.id,
            "❌ برای دریافت فایل‌ها ابتدا باید به کانال ما بپیوندید.",
            reply_markup=markup
        )

bot.polling(none_stop=True)
