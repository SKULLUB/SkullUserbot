from userbot import ALIVE_NAME
from userbot.utils import admin_cmd

name = str(ALIVE_NAME)
SKULLBOT_IS_ALIVE = (
    "**�3�4 �3�2�3�4 �3�6�3�4�3�1�3�0�3�3�3�6 �3�8�3�2�3�0�3�1�3�6�3�9 {name}. �3�6�3�3�3�3 �3�7�3�2�3�5�3�4�3�1�3�0�3�6�3�5�3�0 �3�2�3�9�3�6 �3�4�3�6�3�9�3�2�3�0�3�5�3�8 �3�7�3�9�3�6�3�7�3�6�3�9�3�3�3�6.** \n`�3�7�3�0�3�5 �3�4�3�5�3�6�3�5�3�6�3�4 ` \n\n
    f"`�3�8�3�2�3�0�3�1�3�6�3�9`: {name}\n\n"
    "`�3�4�3�6�3�6�3�7�3�7 �3�7�3�0�3�3.:` **3.8.7**\n`�3�1�3�0�3�5�3�3�3�0�3�9:` **3.8.5**\n"
    "`�3�9�3�6�3�5�3�6�3�7�3�6�3�4�3�0 �3�4�3�5�3�6�3�5�3�6�3�4:` **�7�8�1�5ALL OK**\n\n`Always with you, my master!\n`"
    "**�3�4�3�6�3�1�3�1�3�0�3�3�3�5:** [�3�4�3�6�3�6�3�7�3�7](t.me/skulluserbot)\n"
    "**�3�9�3�0�3�1�3�7�3�0�3�0:** [�3�9�3�0�3�1�3�7�3�0�3�0](github.com/SKULLUB/SkullUserbot)\n\n"
)


@borg.on(admin_cmd(pattern="alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    await borg.send_message(chat, SKULLBOT_IS_ALIVE, link_preview=False)
