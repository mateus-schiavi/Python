import random


def main():
    generate_sentence(1, "past")
    generate_sentence(1, "present")
    generate_sentence(1, "future")
    generate_sentence(0, "past")
    generate_sentence(0, "present")
    generate_sentence(0, "future")
    
def get_determiner(quantity):
    
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        words = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        words = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        
    noun = random.choice(words)
    return noun

def get_verb(quantity, tense):

    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == "present" and quantity == 1:
        words =  ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    elif tense == "present" and quantity != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
        
    else:
        words = ['will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write']
    
    verb = random.choice(words)
    return verb

def get_preposition():

    words = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(words)
    return preposition

def get_prepositional_phrase(quantity):

    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    prepositional_phrase = preposition + ' ' + determiner + ' ' + noun
    return prepositional_phrase

def generate_sentence(quantity, tense):
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    
    print(f'{determiner.capitalize()} {noun} {verb} {prepositional_phrase}.')

main()