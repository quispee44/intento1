import random

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)

    return password

def elegir_emoji():
    emojis=["🥺","😶‍🌫️","😯","😑"]
    return random.choice(emojis)
