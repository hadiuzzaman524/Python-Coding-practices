message=input(">")
emoji={
    ":)": "😘",
    "):": "😂"
}
word=message.split(" ")

msg=""
for i in word:
    msg+=emoji.get(i,i)+" "
print(msg)