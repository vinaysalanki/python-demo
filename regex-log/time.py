import re
with open("error.log","r")as file:
    time=file.read()
time=re.findall(r'admin+@\S+.*ERROR.*',time)
print(time)
with open("timeerror.log","w")as file:
    for line in time:
        file.write(line + "/n")