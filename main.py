import re

matn = """Salom hammaga men Shoxrux developerman mening githup kanalimga obuna bo'linglar.
https://github.com/SHOXRUXno1/Homework hammaga rahmat!"""
andoza = r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)'
link = re.findall(andoza, matn)
print(link)
with open('web_manzil.txt', 'a+') as manzil:
    manzil.write(f'{link}')
