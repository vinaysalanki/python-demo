import re
with open("info.log","r")as file:
    info=file.read()
mail=re.findall(r"2026-03-(?:0[8-9]|10).*ERROR.*",info)
print(mail)
with open("error.log","w")as file:
    for line in mail:
        file.write(line + "\n")