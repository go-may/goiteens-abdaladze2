from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = "BOT_TOKEN"  # Забираем значение типа str
ADMINS = [] # env.list("ADMINS")  # Тут у нас будет список из админов
IP =  '127.0.0.1' #env.str("ip")  # Тоже str, но для айпи адреса хоста

