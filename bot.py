import os
from telegram.ext import Updater, CommandHandler

TOKEN = os.getenv("TOKEN")

def start(update, context): update.message.reply_text("🤖 Welcome to the Bot!")
def help_command(update, context): update.message.reply_text("""
/start - Start bot
/help - Show help
/info - Device info
/apps - Installed apps
/mic - Microphone
/selfie - Selfie camera
/maincam - Main camera
/record_selfie - Record selfie cam
/record_main - Record main cam
/show_notification - Popup notification
/get_location - Location
/show_toast - Show toast
/vibrate - Vibrate
/send_sms - Send SMS
/show_sms - Show SMS
/stop_sound - Stop sound
/play_sound - Play sound
/screenshot - Screenshot
/stop_flash - Stop flashlight
/start_flash - Turn on flashlight
/keylogger - Keylogger
/text_to_speech - Text to speech
/open_link - Open URL
/send_all - SMS to all contacts
""")

def info(update, context): update.message.reply_text("📱 Device info: Samsung SM-A2075")
def apps(update, context): update.message.reply_text("📦 Installed apps list...")
def mic(update, context): update.message.reply_text("🎙️ Microphone activated")
def selfie(update, context): update.message.reply_text("🤳 Selfie camera")
def maincam(update, context): update.message.reply_text("📷 Main camera")
def record_selfie(update, context): update.message.reply_text("🎥 Recording selfie camera...")
def record_main(update, context): update.message.reply_text("🎥 Recording main camera...")
def show_notification(update, context): update.message.reply_text("🔔 Showing popup notification")
def get_location(update, context): update.message.reply_text("📍 Getting location...")
def show_toast(update, context): update.message.reply_text("🔔 Showing toast message...")
def vibrate(update, context): update.message.reply_text("📳 Vibrating device...")
def send_sms(update, context): update.message.reply_text("📤 Sending SMS...")
def show_sms(update, context): update.message.reply_text("📩 Displaying SMS...")
def stop_sound(update, context): update.message.reply_text("🔇 Stopping sound...")
def play_sound(update, context): update.message.reply_text("🔊 Playing sound...")
def screenshot(update, context): update.message.reply_text("📸 Taking screenshot...")
def stop_flash(update, context): update.message.reply_text("💡 Flashlight off")
def start_flash(update, context): update.message.reply_text("🔦 Flashlight on")
def keylogger(update, context): update.message.reply_text("⌨️ Keylogger started...")
def text_to_speech(update, context): update.message.reply_text("🗣️ Converting text to speech...")
def open_link(update, context): update.message.reply_text("🌐 Opening link...")
def send_all(update, context): update.message.reply_text("📬 Sending SMS to all contacts...")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(CommandHandler("help", help_command))
dp.add_handler(CommandHandler("info", info))
dp.add_handler(CommandHandler("apps", apps))
dp.add_handler(CommandHandler("mic", mic))
dp.add_handler(CommandHandler("selfie", selfie))
dp.add_handler(CommandHandler("maincam", maincam))
dp.add_handler(CommandHandler("record_selfie", record_selfie))
dp.add_handler(CommandHandler("record_main", record_main))
dp.add_handler(CommandHandler("show_notification", show_notification))
dp.add_handler(CommandHandler("get_location", get_location))
dp.add_handler(CommandHandler("show_toast", show_toast))
dp.add_handler(CommandHandler("vibrate", vibrate))
dp.add_handler(CommandHandler("send_sms", send_sms))
dp.add_handler(CommandHandler("show_sms", show_sms))
dp.add_handler(CommandHandler("stop_sound", stop_sound))
dp.add_handler(CommandHandler("play_sound", play_sound))
dp.add_handler(CommandHandler("screenshot", screenshot))
dp.add_handler(CommandHandler("stop_flash", stop_flash))
dp.add_handler(CommandHandler("start_flash", start_flash))
dp.add_handler(CommandHandler("keylogger", keylogger))
dp.add_handler(CommandHandler("text_to_speech", text_to_speech))
dp.add_handler(CommandHandler("open_link", open_link))
dp.add_handler(CommandHandler("send_all", send_all))

print("✅ Bot is starting...")
updater.start_polling()
