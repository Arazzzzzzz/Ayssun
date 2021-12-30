import os

class Config(object):
    DATABASE = os.environ.get("DB_URI")
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "1961162381").split())
    SUPPORT = os.environ.get("SUPPORT")
    BOT_NAME = os.environ.get("bat")
    BOT_USERNAME = os.environ.get("bn")
