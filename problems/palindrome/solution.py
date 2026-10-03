text = input()
cleantext = ""
for c in text:
    if c.isalnum():
        cleantext = cleantext + c
print("true" if cleantext == cleantext[::-1] else "false")
