text = "Lorem ipsum dolor sit amet consectetur adipiscing elit Integer porttitor bibendum nisi ut convallis ante"
text = text.split()
count = 0
for i in text:
    if len(i) > 5:
        count += 1
print(count)
