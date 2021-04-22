# SKULLUSERBOT
A Simple Cool Telethon Userbot for Telegram users made with fun and Hardwork. Made by @mayank1rajput and for support join @skulluserbot .

# FORK AT YOUR OWN RISK

# Installing

### The Easy Way to deploy the bot
Get APP ID and API HASH from [HERE](https://my.telegram.org) or [HERE](https://t.me/Tg_Scrap_Bot) and BOT TOKEN from [Bot Father](https://t.me/botfather) and then Generate stringsession by clicking on run.on.repl.it button below and then click on deploy to heroku . Before clicking on deploy to heroku just click on fork and star just below

[![Run on Repl.it](https://repl.it/badge/github/hackelite01/skull-userbot)](https://repl.it/@hackelite011/generatestringsession)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/SKULLUB/SKULL)

[![skulluserbot logo](https://telegra.ph/file/8521d92b36ebe13ae3095.jpg)](https://heroku.com/deploy?template=https://github.com/SKULLUB/SkullUserbot)


### Join [here](https://t.me/skulluserbot) for updates and tuts and [here](https://t.me/skulluserbot_support) for discussion and bugs

### The Normal Way

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

**Heroku Configuration**
Simply just leave the Config as it is.

**Local Configuration**

Fortunately there are no Mandatory vars for the UniBorg Support Config.

## Mandatory Vars

- Only two of the environment variables are mandatory.
- This is because of `telethon.errors.rpc_error_list.ApiIdPublishedFloodError`

    - `APP_ID`:   You can get this value from https://my.telegram.org
    - `API_HASH`:   You can get this value from https://my.telegram.org
- The userbot will not work without setting the mandatory vars.
