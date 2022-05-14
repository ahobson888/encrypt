# This file implements an encryption scheme.
# ==========================================
import string
import random
import argparse

def main():

    args = parse_args()

    seed = input("Enter the random seed: ")
    input_message = "Enter the message for "
    if args.decrypt:
        input_message += "decryption: "
    else:
        input_message += "encryption: "
    message = input(input_message)

    if args.decrypt:
        print(f"The decrypted message is:\n{decrypt(message, seed)}")
    else:
        print(f"The encrypted message is:\n{encrypt(message, seed)}")


def parse_args():
    """Parse arguments from the command line.
    
    Returns a Namespace object.
    """

    parser = argparse.ArgumentParser(
        description="Tool for encrypting & decrypting secret messages." 
    )

    parser.add_argument(
        "--decrypt",
        action='store_true',
        help="run in decrypt mode",
    )

    return parser.parse_args()

def create_character_dict(seed, encrypt):

    # Set the random seed.
    random.seed(seed)

    # Get a list of all of the characters we want to use.
    character_list = list(string.ascii_letters + string.digits + string.punctuation + ' ')

    # Jumble them up.
    jumbled = character_list.copy()
    random.shuffle(jumbled)

    # Create a dictionary for mapping between characters.
    character_dict = dict()
    for i in range(len(character_list)):
        char = character_list[i]
        jumbled_char = jumbled[i]

        if encrypt:
            character_dict[char] = jumbled_char
        else:
            character_dict[jumbled_char] = char

    return character_dict

def encrypt(message, seed):

    # Create the character dictionary for encryption.
    character_dict = create_character_dict(seed, encrypt=True)

    # Map each letter in the message to its jumbled character.
    jumbled_message = [character_dict[char] for char in message]

    # Convert the list of characters into a string.
    return ''.join(jumbled_message)


def decrypt(message, seed):

    # Create the character dictionary for decryption.
    character_dict = create_character_dict(seed, encrypt=False)   

    # Map each letter in the encrypted message to its plaintext character.
    plaintext_message = [character_dict[char] for char in message]

    # Convert the list of characters into a string.
    return ''.join(plaintext_message)

if __name__ == "__main__":
    main()
