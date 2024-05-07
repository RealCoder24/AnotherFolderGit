import random

def generate_insult():
    adjectives = ["silly", "clueless", "absurd", "ridiculous", "bizarre"]
    nouns = ["noodle", "banana", "toaster", "giraffe", "muffin"]

    adjective = random.choice(adjectives)
    noun = random.choice(nouns)

    return f"Hey, you {adjective} {noun}! 🤪"

print(generate_insult())
