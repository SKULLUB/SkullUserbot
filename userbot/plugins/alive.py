from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
SKULLBOT_IS_ALIVE = (
    "**𝙸 𝚊𝚖 𝙰𝚌𝚝𝚒𝚟𝚎 𝙼𝚊𝚜𝚝𝚎𝚛 {name}. 𝙰𝚕𝚕 𝚏𝚞𝚗𝚌𝚝𝚒𝚘𝚗𝚜 𝚊𝚛𝚎 𝚠𝚘𝚛𝚔𝚒𝚗𝚐 𝚙𝚛𝚘𝚙𝚎𝚛𝚕𝚢.** \n`𝙱𝙾𝚃 𝚂𝚃𝙰𝚃𝚄𝚂 ` \n\n
    f"`𝙼𝚊𝚜𝚝𝚎𝚛`: {name}\n\n"
    "`𝚂𝙺𝚄𝙻𝙻 𝚅𝙴𝚁.:` **3.8.7**\n`𝙿𝚈𝚃𝙷𝙾𝙽:` **3.8.5**\n"
    "`𝙳𝙰𝚃𝙰𝙱𝙰𝚂𝙴 𝚂𝚃𝙰𝚃𝚄𝚂:` **✔️ALL OK**\n\n`Always with you, my master!\n`"
    "**𝚂𝚄𝙿𝙿𝙾𝚁𝚃:** [𝚂𝙺𝚄𝙻𝙻](t.me/skulluserbot)\n"
    "**𝙳𝙴𝙿𝙻𝙾𝚈:** [𝙳𝙴𝙿𝙻𝙾𝚈](github.com/SKULLUB/SkullUserbot)\n\n"
)


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, SKULLBOT_IS_ALIVE, link_preview=False)
