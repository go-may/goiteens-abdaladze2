from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()
# env.str("2111286553:AAHzd1pw1WgMoiEJtnuZximHLDppQQBjDq8")
BOT_TOKEN = "2111286553:AAHzd1pw1WgMoiEJtnuZximHLDppQQBjDq8"  # Забираем значение типа str
ADMINS = [] # env.list("ADMINS")  # Тут у нас будет список из админов
IP =  '127.0.0.1' #env.str("ip")  # Тоже str, но для айпи адреса хоста

