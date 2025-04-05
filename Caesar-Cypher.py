import art


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, cypher_direction):
    cypher_text = ""
    for letter in original_text:
        if letter not in alphabet:
            cypher_text += letter
            continue

        letter_position = alphabet.index(letter)
        shifted_position = 0

        if cypher_direction == "encode":
            shifted_position = letter_position + shift_amount
        elif cypher_direction == "decode":
            shifted_position = letter_position - shift_amount

        shifted_position %= len(alphabet)
        cypher_text += alphabet[shifted_position]

    print(f"Your {cypher_direction}d message is: {cypher_text}")

# TODO-3: Can you figure out a way to restart the cipher program?


print(art.logo)
running = True

while running:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)
    repeat = input("Do you want to go again ('Yes or No')?").lower()
    if repeat == "no":
        running = False
        print("Goodbye")
