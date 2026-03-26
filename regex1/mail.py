import re
with open("info.log","r")as file:

    info=file.read()
mail = re.findall(r'2026-03-(?:08|10).*?\|\s*(\S+@\S+)', info)
print(mail)

with open("mails.log","w")as file:
    for data in mail:
        file.write(data + "\n")