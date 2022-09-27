import random

def random_string():
    random_list = [
        "Oh! It appears you wrote something I don't understand yet",
        "Can you please rephrase that?",
        "Do you mind trying to rephrase that?",
        "I'm sorry, I don't understand what you mean",
        "I can't answer that yet, please try asking something else."
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]
