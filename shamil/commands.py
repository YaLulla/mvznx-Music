
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters



HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\n• Iam A Bot Project ny MoviZenX\n• I Can Manage Group VC's\n\n• Hit /help to know about available commands.</b>"
HELP = """

<b>🤖 Read The Below Commands 🤖</b>

**Common Commands**:

**/p**  Reply to an audio file or YouTube link to play it or use /p <song name>.
**/d** Play music from Deezer, Use /d <song name>
**/c**  Show current playing song.
**/help** Show help for commands
**/q** Shows the playlist.

**Admin Commands**:
**/sk** [n] ...  Skip current or n where n >= 2
**/j**  Join voice chat.
**/l**  Leave current voice chat
**/mzx**  Check which VC is joined.
**/sp**  Stop playing.
**/r** Start Radio.
**/sr** Stops Radio Stream.
**/rp**  Play from the beginning.
**/cl** Remove unused RAW PCM files.
**/ps** Pause playing.
**/rs** Resume playing.
**/m**  Mute in VC.
**/um**  Unmute in VC.
**/update** Updates the Bot.
"""



@Client.on_message(filters.command('start'))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('🎭 Developer 🎭️', url='https://t.me/AnnihilusOP'),
                ],[
                InlineKeyboardButton('🤖 Updates', url='https://t.me/movizenx'),
                InlineKeyboardButton('🎟️ Movies', url='https://t.me/movizenix'),
                InlineKeyboardButton('📻 Songs', url='https://t.me/MZX_SUPPORT'),
               ],[
                InlineKeyboardButton('🌎 Developer 🌎', url='https://t.me/AnnihilusOP'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)



@Client.on_message(filters.command("help"))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton('🎭 Developer 🎭️', url='https://t.me/AnnihilusOP'),
                ],[
                InlineKeyboardButton('🤖 Updates', url='https://t.me/movizenx'),
                InlineKeyboardButton('🎟️ Movies', url='https://t.me/movizenix'),
                InlineKeyboardButton('📻 Songs', url='https://t.me/mzx_support'),
               ],[
                InlineKeyboardButton('🌎 Creator 🌎', url='https://t.me/AnnihilusOP'),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
