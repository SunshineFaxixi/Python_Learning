REPLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt") as f:
    name_list = f.readlines()
    # print(name_list)

with open("Input/Letters/starting_letter.txt") as letter:
    letter_content = letter.read()
    for name in name_list:
        strip_name = name.strip()
        new_letter = letter_content.replace(REPLACEHOLDER, strip_name)
        with open(f"Output/ReadyToSend/letter_to_{strip_name}.txt", "w") as l:
            l.write(new_letter)