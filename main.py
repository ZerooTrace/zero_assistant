import telebot
import config
import agent
import font_change
import tools

bot = telebot.TeleBot(config.TELEGRAM_BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    wlcm_msg = """
    ⚡ 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝚃𝙾 𝚉𝙴𝚁𝙾𝚃𝚁𝙰𝙲𝙴 ⚡ 
𝚈𝚘𝚞’𝚟𝚎 𝚓𝚞𝚜𝚝 𝚜𝚝𝚎𝚙𝚙𝚎𝚍 𝚒𝚗𝚝𝚘 𝚜𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 𝚍𝚒𝚏𝚏𝚎𝚛𝚎𝚗𝚝. 👀  
🤖 𝚃𝚑𝚒𝚜 𝚋𝚘𝚝 𝚒𝚜 𝚙𝚘𝚠𝚎𝚛𝚎𝚍 𝚋𝚢 𝚉𝚎𝚛𝚘𝚃𝚛𝚊𝚌𝚎 — 
𝚋𝚞𝚒𝚕𝚝 𝚝𝚘 𝚖𝚊𝚔𝚎 𝚢𝚘𝚞𝚛 𝚎𝚡𝚙𝚎𝚛𝚒𝚎𝚗𝚌𝚎 𝚜𝚖𝚊𝚛𝚝𝚎𝚛, 𝚜𝚖𝚘𝚘𝚝𝚑𝚎𝚛, 𝚊𝚗𝚍 𝚖𝚘𝚛𝚎 𝚎𝚡𝚌𝚒𝚝𝚒𝚗𝚐.  
✨ 𝙳𝚒𝚜𝚌𝚘𝚟𝚎𝚛. 𝙴𝚡𝚙𝚕𝚘𝚛𝚎. 𝙸𝚗𝚝𝚎𝚛𝚊𝚌𝚝. 
🔥 𝚃𝚑𝚎𝚛𝚎’𝚜 𝚊𝚕𝚠𝚊𝚢𝚜 𝚜𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 𝚗𝚎𝚠 𝚠𝚊𝚒𝚝𝚒𝚗𝚐 𝚏𝚘𝚛 𝚢𝚘𝚞.  
𝙲𝚘𝚖𝚎 𝚘𝚗𝚌𝚎 𝚏𝚘𝚛 𝚝𝚑𝚎 𝚎𝚡𝚙𝚎𝚛𝚒𝚎𝚗𝚌𝚎… 𝙲𝚘𝚖𝚎 𝚋𝚊𝚌𝚔 𝚋𝚎𝚌𝚊𝚞𝚜𝚎 𝚢𝚘𝚞’𝚕𝚕 𝚠𝚊𝚗𝚝 𝚝𝚘 𝚜𝚎𝚎 𝚠𝚑𝚊𝚝’𝚜 𝚗𝚎𝚡𝚝. 🚀  
🖤 𝚉𝚎𝚛𝚘𝚃𝚛𝚊𝚌𝚎 — 𝚆𝚑𝚎𝚛𝚎 𝚌𝚞𝚛𝚒𝚘𝚜𝚒𝚝𝚢 𝚖𝚎𝚎𝚝𝚜 𝚜𝚘𝚖𝚎𝚝𝚑𝚒𝚗𝚐 𝚎𝚡𝚝𝚛𝚊𝚘𝚛𝚍𝚒𝚗𝚊𝚛𝚢.  
🌟 𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚉𝚎𝚛𝚘𝚃𝚛𝚊𝚌𝚎. 𝚈𝚘𝚞𝚛 𝚓𝚘𝚞𝚛𝚗𝚎𝚢 𝚜𝚝𝚊𝚛𝚝𝚜 𝚑𝚎𝚛𝚎.
    """
    bot.send_message(message.chat.id,
        wlcm_msg,
        message_effect_id='5104841245755180586')


@bot.message_handler(commands=['social_media'])
def give_social(message):
    social_link = """<blockquote>
<b>🌐 Connect with tech_by_niteshh</b>

Stay connected with the latest updates, projects, AI stuff and community activities 🚀

</blockquote>

<blockquote>
<b>YouTube</b><a href="https://www.youtube.com/@ZeroTraceRoot">Watch & Subscribe</a>

<b>Instagram</b> <a href="https://www.instagram.com/tech_by_niteshh/">Follow on Instagram</a>

<b>Discord</b> <a href="https://discord.gg/zerotrace">Join the Community</a>

<b>Facebook</b> <a href="https://www.facebook.com/Zerotraceroot">Follow on Facebook</a>

<b>Telegram Channel</b> <a href="YOUR_TELEGRAM_CHANNEL_URL">Join the Channel</a>

<b>X-Account</b> <a href="https://x.com/tech_by_niteshh">Join with us.</a>

</blockquote>

<blockquote>
🤖 <b>Nittuubot</b>

Your AI-powered assistant by tech_by_niteshh.

</blockquote>

<blockquote>
❤️ <b>Follow • Join • Connect</b>
</blockquote>

"""
    bot.send_message(message.chat.id,
                     social_link, 
                     parse_mode='html',
                     message_effect_id='5104841245755180586'
                     )
    

@bot.message_handler(commands=['contact_us'])
def conatact_us(message):
    contact_link = """<blockquote>
<b>🌐 Connect with tech_by_niteshh</b>

Stay connected with the latest updates, projects, AI stuff and community activities 🚀

</blockquote>

<blockquote>
<b>Discord : </b><a href="https://discord.gg/Zerotrace">Join Discord</a>
</blockquote>

<blockquote>
<b>join  connect  grow</b>
</blockquote>
"""
    bot.send_message(message.chat.id,
                 contact_link,
                 parse_mode='html',
                 message_effect_id='5104841245755180586')

@bot.message_handler(commands=["shortner"])
def shortne_url(message):
    bot.reply_to(message, "Just send me the long URL.")
    bot.register_next_step_handler(message, shortner)


def shortner(message):
    long_url = message.text.strip()

    if not long_url.startswith(("http://", "https://")):
        bot.reply_to(message, "Please send a valid URL starting with http:// or https://")
        return

    try:
        short_url = tools.shorten_url(long_url)

        bot.send_message(
            message.chat.id,
            f"Shortened URL:\n{short_url}"
        )

    except Exception as e:
        bot.reply_to(
            message,
            "Sorry, I couldn't shorten that URL. Please try again."
        )

def shortner(message):
    long_url = message.text.strip()

    if not long_url.startswith(("http://", "https://")):
        bot.reply_to(
            message,
            "❌ <b>Invalid URL</b>\n\nPlease send a valid URL starting with http:// or https://",
            parse_mode="HTML"
        )
        return

    try:
        short_url = tools.shorten_url(long_url)

        response = (
            "🔗 <b>URL Shortened Successfully</b>\n\n"
            f"🌐 <a href=\"{short_url}\">Open Short URL</a>\n\n"
            f"📎 {short_url}"
        )

        bot.send_message(
            message.chat.id,
            response,
            parse_mode="HTML",
            disable_web_page_preview=True
        )

    except Exception:
        bot.reply_to(
            message,
            "⚠️ <b>Something went wrong.</b>\n\nPlease try again later.",
            parse_mode="HTML"
        )

@bot.message_handler(func = lambda message: True)
def echo_all(message):
    response = agent.explain_ai(message.text)
    response = font_change.transform_text(response)
    response_msg=f"""You : {message.text}
    

Response : {response}
    """
    bot.send_message(message.chat.id, response_msg, message_effect_id='5104841245755180586')



bot.polling()