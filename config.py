from os import environ 

class Config:
    API_ID = int(environ.get("API_ID", 12345))
    API_HASH = environ.get("API_HASH")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6791399851:AAEI1CUfW0xdAo0kqbu0QzCTb0ov0vUrcoQ") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://FORWARDBOT:FORWARDBOT@cluster0.bbkkwqq.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", 5354962863 5022283560).split()]
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
