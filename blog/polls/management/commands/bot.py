from django.core.management.base import BaseCommand

from django.conf import settings

from telebot import TeleBot

from ...models import Post

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    posts = Post.objects.all()
    for post in posts:
        bot.send_message(message.chat.id,post.title)

    bot.reply_to(message, "Hi there, Please ask your question)")

class Command(BaseCommand):

    help = 'Just a command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        bot.enable_save_next_step_handlers(delay=2)
        bot.load_next_step_handlers()
        bot.infinity_polling()

