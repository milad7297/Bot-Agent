from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import random

# تنظیمات اولیه
OWNER_ID = 123456789  # @RobinnooB (از @userinfobot بگیرید)

# خواندن جملات از فایل
with open('sentences.txt', 'r', encoding='utf-8') as file:
    sentences = file.readlines()

# دستور استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    
    if user_id == OWNER_ID:
        # اگر صاحب ربات استارت کند
        random_sentence = random.choice(sentences).strip()
        await update.message.reply_text(random_sentence)
    else:
        # اگر فرد دیگری استارت کند
        await update.message.reply_text("تو که میلاد نیستی!")

# تابع اصلی
def main():
    app = ApplicationBuilder().token("7829341794:AAF5SbkmMiTSaMKjmJATR1sG869-cV7m2Fo").build()
    
    app.add_handler(CommandHandler("start", start))
    
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == '__main__':
    main()
