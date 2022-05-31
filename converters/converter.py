from random import choice
import string

def generate_short_id(num_of_chars: int):
    return ''.join(choice(string.ascii_letters + string.digits) for _ in range(num_of_chars))

def shorten():
    short_id = generate_short_id(6)
    return f"domianTBC.com/{short_id}"

# print(shorten())

