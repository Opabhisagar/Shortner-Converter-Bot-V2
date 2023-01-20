# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "28605803"))
API_HASH = os.environ.get("API_HASH", "5128d225bdcb1f5d375ed9550af15620")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5981200068:AAHsJiXjL9TZDUUWOkwBCoqQP0weDUiwkq8")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("944893221")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Opabhisagar")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Opabhisagar:<Abhishek@@@@@89>@cluster0.qzvaldg.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "944893221")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001721695366")) 
UPDATE_CHANNEL = os.environ.get("mdiskshortner", "Updates Channel User name Without @") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
