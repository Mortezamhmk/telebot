# telebot
import telebot
from telebot import types

API_TOKEN = ''
BOT_USERNAME = ""
CHANNEL_USERNAME = # یوزرنیم کانال شما بدون @
bot = telebot.TeleBot(API_TOKEN)

def check_user_subscription(user_id):
    """بررسی عضویت کاربر در کانال"""
    try:
        # بررسی وضعیت عضویت کاربر در کانال
        chat_member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if chat_member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f"Error checking subscription: {e}")
        return False

@bot.message_handler(commands=['start'])
def send_welcome(message):
    """دستور /start برای بررسی عضویت و ارسال فایل‌ها"""
    user_id = message.from_user.id

    # بررسی عضویت کاربر در کانال
    if check_user_subscription(user_id):
        bot.reply_to(message, "✅ شما به کانال پیوستید! حالا می‌توانید فایل‌ها را دریافت کنید.")
        # در اینجا می‌توانید کد ارسال فایل‌ها را قرار دهید
        # به عنوان مثال:
        # bot.send_document(message.chat.id, document_file_id)
    else:
        bot.reply_to(message, 
                     f"❌ برای دریافت فایل‌ها ابتدا باید به کانال ما بپیوندید. لطفاً از لینک زیر برای عضویت استفاده کنید:\n\n"
                     f"https://t.me/{CHANNEL_USERNAME}\n\n"
                     "پس از پیوستن به کانال، دوباره دستور /start را ارسال کنید تا فایل‌ها را دریافت کنید.")

bot.polling(none_stop=True)
