import random


def main():
    tense = ['past','present','future']
    quant = [1,2]
    for amount in quant:
        for tenses in tense:
            adjective = get_adj()
            adverb = get_adv()
            determiner = get_det(quant)
            noun = get_n(quant)
            verb = get_v(quant, tenses)
            preposition_1 = get_prepo_phrase(quant)
            preposition_2 = get_prepo_phrase(quant)
            
            main_sentence = f'{preposition_1.capitalize()},{determiner},{adjective},{verb},{adverb},{preposition_2}. \n'

def get_determiner(quant):
    
    if quant == 1:
        word = ['a','one','the']
    else:
        word = ['some','many','the']
        
    
    determiner = random.choice(word)
    return determiner

def get_n(quant):
     
    if quant == 1:
        noun = ['bird','child','motorcycle','lion','lizard','tiger','snake','butterfly']
    
    else:
        noun = ['birds','children','motorcycles','lions','lizards','tigers','snakes','butterflies']

def get_v(quant, tense):
    
    if tense == 'past':
        verbs = ['played','told','opened','sewed','breathed','printed','threw','jumped']
        
    elif tense == 'present':
        if quant == 1:
            verbs = ['plays','tells','opens','sews','breathes','prints','throws','jumps']
            
        else:
            verbs = ['play','tell','open','sew','breath','print','throw','jump']

    elif tense == 'future':
        verbs = ['will play','will tell','will open','will breath','will print','will throw','will jump','will sew']

    verb = random.ch(verbs)
    return verb

    def get_prepo():

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


def get_prepo_phrase(quant):

    preposition = get_prepo_phrase()
    determiner = get_det(quant)
    noun = get_n(quant)
    adjective = get_adj()

    preposition_phrase = f'{preposition} {determiner} {adj} {noun}'
    return preposition_phrase


def get_adj():
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
    
    
def get_adv():
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