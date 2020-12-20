alphbat = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(direction, message, shift):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in message:
        if char in alphbat:
            position = alphbat.index(char)
            new_position = (position + shift) % len(alphbat)
            new_letter = alphbat[new_position]
            end_text += new_letter
        else:
            end_text += char
    print(f"The {direction}d result: {end_text}")


if __name__ == "__main__":
    should_continue = True
    while should_continue:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(direction, text, shift)

        res = input("Do you want to continue?")
        if res == 'no':
            should_continue = False
            print("GoodBye")