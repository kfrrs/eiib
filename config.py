## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "AgB9_NwaH7eC3sVBAQd8UTNEBOdXSXWJk-dKEYyhY0HzfOdtfZI8-gjHcIM9RonXEpWeHoDsfQ_FPd9CF8XA16K8BlburvSZeTRfkKnHH93m_73WE7ZMPtrAijEE6DHnAjBTHx_W0TkdZmklpOdF4l_jURf_aLGEQBs5fQX1D1vJzTXq3YzAnS-257fnlDz943Rms4JgCgQpiwMi9SE4vOkKwposhga-71buHKB-NjXl7sj0Og4iOM_fQ93BrwFOMmO5WvTWz7JrWEAGWB0RyYn2yAmAwzOP9RyvFHagM6nyG6A0zIgmvJPWXznFNHtNzDWDj9ONFls-IKdt01Ed5gOmAAAAAU1j9gsA")
BOT_TOKEN = getenv("BOT_TOKEN", "5531140266:AAGB6uc2yhrnZoafmRuRF-r6O309ZtwTjo0")
BOT_NAME = getenv("BOT_NAME", "ᯎ Texas ¹.")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "اެلفخِم")
OWNER_USERNAME = getenv("OWNER_USERNAME", "RHHPP")
ALIVE_NAME = getenv("ALIVE_NAME", "𝖡ْ𝖾ٌِ𝖱𝗈ّ")
BOT_USERNAME = getenv("BOT_USERNAME", "WUI5BOT")
OWNER_ID = getenv("OWNER_ID", "1163044147")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "G2IID")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "HDPPPP")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "BHPPPP")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1163044147").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/e22e5d1f0ccd57fa5f677.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
