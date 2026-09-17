star = "*"
line = "-"
text = ""
flag = ""

for i in range(3):
    for j in range(7):
        text += star
    text += "\n"
    
print(text)

for i in range(5):
    for j in range (19):
        if i < 3 and j < 7:
            flag += star
        else:
            flag += line
    flag += "\n"
            
print(flag)