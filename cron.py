from crontab import CronTab

# Inisialisasi objek CronTab
cron = CronTab(user='root')  # Ganti 'username' dengan nama pengguna Anda

# Buat objek cron job baru
job = cron.new(command='python /workspace/p/scrape.py')  # Ganti '/path/to/anjai.py' dengan path yang sesuai

# Atur jadwal cron job untuk menjalankan setiap 1 menit
job.minute.every(1)

# Tambahkan job ke crontab
    cron.write()
    
