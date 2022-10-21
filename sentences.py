import random 

def main():
    tenses = ['past', 'present', 'future']
    quantities = [1, 2]
    for quantity in quantities:
        for tense in tenses:
            adj = get_adjective()
            adv = get_adverb()
            d = get_determiner(quantity)
            n = get_noun(quantity)
            v = get_verb(quantity, tense)
            p1 = get_prepositional_phrase(quantity)
            p2 = get_prepositional_phrase(quantity)
            
            sentence = f'{p1.capitalize()}, {d} {adj} {n} {v} {adv} {p2}. \n'
            
            print(sentence)


def get_determiner(quantity):
    '''Return a randomly chosen determiner. A determiner is
    a word like 'the', 'a', 'one', 'some', 'many'.
    If quantity == 1, this function will return either 'a',
    'one', or 'the'. Otherwise this function will return
    either 'some', 'many', or 'the'.
    Parameter
        quantity: an integer.
            If quantity == 1, this function will return a
            determiner for a single noun. Otherwise this
            function will return a determiner for a plural
            noun.
    Return: a randomly chosen determiner.
    '''
    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['some', 'many', 'the']

    # Randomly choose and return a determiner.
    determiner = random.choice(words)
    return determiner


def get_noun(quantity):
    '''Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
        'bird', 'boy', 'car', 'cat', 'child',
        'dog', 'girl', 'man', 'rabbit', 'woman'
    Otherwise, this function will return one of
    these ten plural nouns:
        'birds', 'boys', 'cars', 'cats', 'children',
        'dogs', 'girls', 'men', 'rabbits', 'women'
    Parameter
        quantity: an integer that determines if
            the returned noun is single or plural.
    Return: a randomly chosen noun.
    '''
    
    if quantity == 1:
        nouns = ['bird', 'boy', 'car', 
                 'cat', 'child', 'dog', 
                 'girl', 'man', 'rabbit', 
                 'woman']
    else:
        nouns = ['birds', 'boys', 'cars', 
                 'cats', 'children', 'dogs', 
                 'girls', 'men', 'rabbits', 
                 'women']

    noun = random.choice(nouns)
    return noun


def get_verb(quantity, tense):
    '''Return a randomly chosen verb. If tense is 'past',
    this function will return one of these ten verbs:
        'drank', 'ate', 'grew', 'laughed', 'thought',
        'ran', 'slept', 'talked', 'walked', 'wrote'
    If tense is 'present' and quantity is 1, this
    function will return one of these ten verbs:
        'drinks', 'eats', 'grows', 'laughs', 'thinks',
        'runs', 'sleeps', 'talks', 'walks', 'writes'
    If tense is 'present' and quantity is NOT 1,
    this function will return one of these ten verbs:
        'drink', 'eat', 'grow', 'laugh', 'think',
        'run', 'sleep', 'talk', 'walk', 'write'
    If tense is 'future', this function will return one of
    these ten verbs:
        'will drink', 'will eat', 'will grow', 'will laugh',
        'will think', 'will run', 'will sleep', 'will talk',
        'will walk', 'will write'
    Parameters
        quantity: an integer that determines if the
            returned verb is single or plural.
        tense: a string that determines the verb conjugation,
            either 'past', 'present' or 'future'.
    Return: a randomly chosen verb.
    '''
    
    if tense == 'past':
        verbs = ['drank', 'ate', 'grew', 
                 'laughed', 'thought', 'ran', 
                 'slept', 'talked', 'walked', 
                 'wrote']
    elif tense == 'present':
        if quantity == 1:
            verbs = ['drinks', 'eats', 'grows', 
                     'laughs', 'thinks', 'runs', 
                     'sleeps', 'talks', 'walks', 
                     'writes']
        else:
            verbs = ['drink', 'eat', 'grow', 
                     'laugh', 'think', 'run', 
                     'sleep', 'talk', 'walk', 
                     'write']
    elif tense == 'future':
        verbs = ['will drink', 'will eat', 'will grow', 
                 'will laugh', 'will think', 'will run', 
                 'will sleep', 'will talk', 'will walk', 
                 'will write']

    verb = random.choice(verbs)
    return verb


def get_preposition():
    '''Return a randomly chosen preposition
    from this list of prepositions:
        'about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without'
    Return: a randomly chosen preposition.
    '''
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


def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    Parameter
        quantity: an integer that determines if the determiner
            and noun in the prepositional phrase returned from
            this function are single or plural.
    Return: a prepositional phrase.
    """
    
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    adj = get_adjective()

    prepositional_phrase = f'{preposition} {determiner} {adj} {noun}'
    return prepositional_phrase


def get_adjective():
    adjectives = ['adorable', 'adventurous', 'aggressive', 
                   'agreeable', 'alert', 'alive', 
                   'amused', 'angry', 'annoyed', 
                   'annoying', 'anxious', 'arrogant', 
                   'ashamed', 'attractive', 'average', 
                   'awful', 'bad', 'beautiful', 
                   'better', 'bewildered', 'black', 
                   'bloody', 'blue', 'blue-eyed', 
                   'blushing', 'bored', 'brainy', 
                   'brave', 'breakable', 'bright', 
                   'busy', 'calm', 'careful', 
                   'cautious', 'charming', 'cheerful', 
                   'clean', 'clear', 'clever', 
                   'cloudy', 'clumsy', 'colorful', 
                   'combative', 'comfortable', 'concerned', 
                   'condemned', 'confused', 'cooperative', 
                   'courageous', 'crazy', 'creepy', 
                   'crowded', 'cruel', 'curious', 
                   'cute', 'dangerous', 'dark', 
                   'dead', 'defeated', 'defiant', 
                   'delightful', 'depressed', 'determined', 
                   'different', 'difficult', 'disgusted', 
                   'distinct', 'disturbed', 'dizzy', 
                   'doubtful', 'drab', 'dull']
    
    adjective = random.choice(adjectives)
    return adjective
    
    
def get_adverb():
    adverbs = ['accidentally', 'always', 'angrily', 
               'anxiously', 'arrogantly', 'awkwardly', 
               'badly', 'blindly', 'boastfully', 
               'boldly', 'bravely', 'brightly', 
               'cheerfully', 'coyly', 'crazily', 
               'cruelly', 'defiantly', 'deftly', 
               'deliberately', 'devotedly', 'doubtfully', 
               'dramatically', 'dreamily', 'dutifully', 
               'eagerly', 'elegantly', 'enormously', 
               'evenly', 'eventually', 'exactly', 
               'faithfully', 'finally', 'fondly', 
               'foolishly', 'fortunately', 'frantically', 
               'frequently', 'gleefully', 'gracefully', 
               'happily', 'hastily', 'honestly', 
               'hopelessly', 'hourly', 'hungrily', 
               'innocently', 'inquisitively', 'irritably', 
               'jealously', 'joyously', 'justly', 
               'kindly', 'lazily', 'loosely', 
               'madly', 'merrily', 'mortally', 
               'mysteriously', 'nervously', 'never', 
               'noisily', 'obediently', 'obnoxiously', 
               'occasionally', 'often', 'only', 
               'perfectly', 'politely', 'poorly', 
               'powerfully', 'promptly', 'quickly', 
               'rapidly', 'rarely', 'regularly', 
               'reluctantly', 'rudely', 'safely', 
               'seldom', 'selfishly', 'seriously', 
               'shakily', 'sharply', 'silently', 
               'slowly', 'solemnly', 'sometimes', 
               'speedily', 'sternly', 'technically', 
               'tediously', 'unexpectedly', 'usually', 
               'victoriously', 'vivaciously', 'warmly', 
               'wearily', 'weekly', 'wildly', 
               'yearly']
    
    adverb = random.choice(adverbs)
    return adverb


if __name__ == '__main__':
    main()