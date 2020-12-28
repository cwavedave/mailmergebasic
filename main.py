with open("./Input/Letters/starting_letter.docx", mode="r") as template:
    content = template.read()

with open("./Input/Names/invited_names.txt", mode="r") as list:
    names = list.readlines()

print(content)
print(names)

name_template = "[name]"
formatted_names = []

for name in names:
    formatted_names.append(name.strip())

for name in formatted_names:
    print(name)
    with open(f"./Output/ReadyToSend/{name}.txt",mode="w") as ready_to_send:
        ready_to_send.write(content.replace(name_template, name))