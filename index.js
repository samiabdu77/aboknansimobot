const TelegramBot = require('node-telegram-bot-api');

const bot = new TelegramBot(process.env.bot_token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, "مرحبًا، أنا Aboknansimobot!");
});
