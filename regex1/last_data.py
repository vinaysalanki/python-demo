import re
with open("info.log",'r')as file:
    info=file.read()
result=re.findall(r'2026-03-(?:08|10).*ERROR.*',info)
print(result)
with open("error.log","w")as file:
    for line in result:

        file.write(line + "\n")



