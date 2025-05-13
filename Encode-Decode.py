# The original set of charector used
# charecter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
#             'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
#             'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#             'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7',
#             '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=',
#             '+', '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '.', '<', '>', 
#             '/', '?', '`', '~', ' ']

# Shuffled set of characters

charecter = ['m', 'k', 'G', 'Q', 'Y', '%', 'T', '&', '?', 'g', '8', 'V', 'v', 's', '#',
            'R', 'L', 'f', '^', 'K', 'o', '[', 'h', 'd', '2', '_', '4', 'p', 'F', 'N',
            ')', '/', 'D', '+', 'J', 'j', 'X', 'r', ':', '-', '|', 'y', 'E', 'B', 'b',
            '`', 'a', 'x', 'H', 'M', 't', 'q', ' ', 'C', '3', 'z', 'S', ',', 'I', 'l',
            '>', '{', '~', '0', 'Z', 'A', '7', '@', 'c', '6', '}', '9', 'n', '.', '(',
            '5', "'", ';', '"', 'O', '=', 'W', '!', '\\', 'P', 'i', 'e', ']', '1', 'U',
            'u', '*', 'w', '<', '$']


def encode_decode(og_msg, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
            shift_amount *= -1
    for letter in og_msg:

        if letter not in charecter:
            output_text += letter

        else:
            shifted_position = charecter.index(letter) + shift_amount
            shifted_position %= len(charecter)
            output_text += charecter[shifted_position]
        
    print(f"Here is your {encode_or_decode} message: {output_text}")


should_continue = True

while should_continue:

    direction =  input("Type 'encode' to encrypt and 'decode' to decrypt\n").lower()
    msg = input("Type Your massage\n")
    shift = int(input("Type shift number\n"))

    encode_decode(msg, shift, direction)
    
    restart = input("Type 'yes' if you want to go again else type 'no'\n").lower()

    if restart != "yes":
        should_continue = False
        print("Goodbye")
    else:
        pass
