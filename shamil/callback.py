

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram import Client, emoji
from utils import mp
from config import Config
playlist=Config.playlist

HELP = """

<b>I Can Play Music On VoiceChats 🤪</b>

**Common Commands**:

**/p**  Reply to an audio file or YouTube link to play it or use /p <song name>.
**/d** Play music from Deezer, Use /d <song name>
**/c**  Show current playing song.
**/help** Show help for commands
**/mwk** Shows the playlist.

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
**/update** Restarts the Bot.
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id not in Config.ADMINS:
        await query.answer(
            "Loading.....",
            show_alert=True
            )
        return
    else:
        await query.answer()
    if query.data == "rp":
        group_call = mp.group_call
        if not playlist:
            return
        group_call.restart_playout()
        if not playlist:
            pl = f"😖 Nothing On Que Ser"
        else:
            pl = f"📻 **Playlist**:\n" + "\n".join([
                f"**{i}**. **🎧{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(
                f"{pl}",
                parse_mode="Markdown",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄 Replay", callback_data="rp"),
                            InlineKeyboardButton("⏯ Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏩ Skip", callback_data="sk"),
                            InlineKeyboardButton("📻 Updates Channel", url="https://t.me/movizenx")
                        ]
                    ]
                )
            )

    elif query.data == "ps":
        if not playlist:
            return
        else:
            mp.group_call.pause_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Paused\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄 Replay", callback_data="rp"),
                            InlineKeyboardButton("⏯ Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏩ Skip", callback_data="sk"),
                            InlineKeyboardButton("📻 Movies Group", url='https://t.me/movizenix')
                        ],
                    ]
                )
            )

    
    elif query.data == "rs":   
        if not playlist:
            return
        else:
            mp.group_call.resume_playout()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Resumed\n\n{pl}",
        reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔄 Replay", callback_data="rp"),
                            InlineKeyboardButton("⏯ Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏩ Skip", callback_data="sk"),
                            InlineKeyboardButton("📻 Updates Channel", url="https://t.me/movizenx") 
                        ],
                    ]
                )
            )

    elif query.data=="sk":   
        if not playlist:
            return
        else:
            await mp.skip_current_playing()
            pl = f"🎧 **Playlist**:\n" + "\n".join([
                f"**{i}**. **📻{x[1]}**\n   👤**Requested by:** {x[4]}"
                for i, x in enumerate(playlist)
                ])
        try:
            await query.edit_message_text(f"{emoji.PLAY_OR_PAUSE_BUTTON} Skipped\n\n{pl}",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔄 Replay", callback_data="rp"),
                            InlineKeyboardButton("⏯ Pause", callback_data="ps")
                        ],[
                            InlineKeyboardButton("⏩ Skip", callback_data="sk"),
                            InlineKeyboardButton("📻 Updates Channel", url="https://t.me/movizenx")
                            
                    ],
                ]
            )
        )
        except:
            pass
    elif query.data=="help":
        buttons = [
            [
                InlineKeyboardButton('🎭 Developer 🎭️', url='https://t.me/AnnihilusOP'),
                ],[
                InlineKeyboardButton('🤖 Updates', url='https://t.me/movizenx'),
                InlineKeyboardButton('🎟️ Movies', url='https://t.me/mobizenix'),
                InlineKeyboardButton('📻 Songs', url='https://t.me/mzx_support'),
               ],[
                InlineKeyboardButton('🌎 Creator 🌎', url='https://t.me/AnnihilusOP'),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await query.edit_message_text(
            HELP,
            reply_markup=reply_markup

        )

