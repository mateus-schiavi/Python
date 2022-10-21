import random 

def main():
    tenses = ['past', 'present', 'future']
    quantities = [1, 2]
    for x in quantities:
        for tense in tenses:
            adjective = get_adjective()
            adverb = get_adverb()
            determiner = get_determiner(x)
            noun = get_noun(quantity)
            verb = get_verb(quantity, tense)
            preposition_1 = get_prepositional_phrase(x)
            preposition_2 = get_prepositional_phrase(x)
            
            sentence = f'{preposition_1.capitalize()}, {determiner} {adjective} {noun} {verb} {adverb} {preposition_2}. \n'
            
            print(sentence)


def get_determiner(x):
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']

    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    return determiner


def get_noun(x):

    if quantity == 1:
        nouns = ['butterfly', 'motorcycle', 'board', 
                 'cat', 'child', 'snake', 
                 'girl', 'man', 'rabbit', 
                 'woman']
    else:
        nouns = ['butterflies', 'motorcycles', 'boards', 
                 'cats', 'children', 'snakes', 
                 'girls', 'men', 'rabbits', 
                 'women']

    noun = random.choice(nouns)
    return noun


def get_verb(x, tense):

    if tense == 'past':
        verbs = ['slept', 'swam', 'grew', 
                 'laughed', 'ran', 'played', 
                 'opened', 'talked', 'walked', 
                 'wrote']
    elif tense == 'present':
        if quantity == 1:
            verbs = ['sleeps', 'swims', 'grows', 
                     'laughs', 'runs', 'plays', 
                     'opens', 'talks', 'walks', 
                     'writes']
        else:
            verbs = ['sleep', 'swim', 'grow', 
                     'laugh', 'run', 'play', 
                     'open', 'talk', 'walk', 
                     'write']
    elif tense == 'future':
        verbs = ['will sleep', 'will swim', 'will grow', 
                 'will laugh', 'will run', 'will play', 
                 'will open', 'will talk', 'will walk', 
                 'will write']

    verb = random.choice(verbs)
    return verb


def get_preposition():

    prepositions = ['about', 'above', 'across', 
                    'after', 'along', 'around', 
                    'at', 'before', 'behind', 
                    'below', 'beyond', 'by', 
                    'despite', 'except', 'for', 
                    'from', 'in', 'into', 
                    'near', 'of', 'off', 
                    'on', 'onto', 'out', 
                    'over', 'past', 'to', 
                    'under', 'with', 'without']
    preposition = random.choice(prepositions)
    return preposition


def get_prepositional_phrase(x):

    preposition = get_preposition()
    determiner = get_determiner(x)
    noun = get_noun(x)
    adj = get_adjective()

    prepositional_phrase = f'{preposition} {determiner} {adj} {noun}'
    return prepositional_phrase


def get_adjective():
    adjectives = ['awful', 'bad', 'beautiful', 
                   'better', 'bewildered', 'black', 
                   'bloody', 'blue', 'blue-eyed', 
                   'blushing', 'bored', 'brainy', 
                   'brave', 'breakable', 'bright',
                   'distinct', 'disturbed', 'dizzy', 
                   'doubtful', 'drab', 'dull']
    
    adjective = random.choice(adjectives)
    return adjective
    
    
def get_adverb():
    adverbs = ['kindly', 'lazily', 'loosely', 
               'madly', 'merrily', 'mortally', 
               'mysteriously', 'nervously', 'never', 
               'noisily', 'obediently', 'obnoxiously', 
               'occasionally', 'often', 'only', 
               'perfectly', 'politely', 'poorly', 
               'powerfully', 'promptly', 'quickly', 
               'yearly']
    
    adverb = random.choice(adverbs)
    return adverb


if __name__ == '__main__':
    main()