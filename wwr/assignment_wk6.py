import random
import re

tense = [0,1,2]
tense = random.choice(tense)

def take_noun():
    global noun_variable
    global determinated_variable
    determinated_variable = 0
    
    first_noun = ['I']
    second_noun = ['Holiday','business','scriptures','insects','animal','maintask','house']
    third_noun = ['crowd','decade','week','objects']
    fourth_noun = ['you', 'they']
    
    noun = [first_noun,second_noun,third_noun,fourth_noun]
    noun_chosen = random.choice(noun)
    noun_real_chosen = random.choice(noun_chosen)
    
    
    if noun_chosen == first_noun:
        noun_variable = 0
        determinated_variable = 0
    elif noun_chosen == second_noun:
        noun_variable = 1
        determinated_variable = 1
    elif noun_chosen == third_noun:
        noun_variable = 2
        determinated_variable = 2
    elif noun_chosen == fourth_noun:
        noun_variable = 2
        determinated_variable = 0
    else:
        print('It is not possible to run the program')
        
def getting_determinated(determinated_variable):

    determinated_none = ''
    determinated_singular = ['the','a']
    determinated_plural = ['some','many']

    if determinated_variable == 0:
        determinated_real = determinated_none
        return determinated_real  
    elif determinated_variable == 1:
        determinated_real = random.choice(determinated_singular)
        return determinated_real
    elif determinated_variable == 2:
        determinated_real = random.choice(determinated_plural)
        return determinated_real
    
def take_verb(noun_variable):
    
    global tense
    tense = [0,1,2]
    tense = random.choice(tense)
    
    to_be = [['am','was','will be'],['is','was','will be'],['are','were','will be']]
    to_have = [['have','had','will have'],['has','had','will have'],['have','had','will have']]
    to_see = [['see','saw','will see'],['sees','saw','will see'],['see','saw','will see']]
    to_know = [['know','knew','will know'],['knows','knew','will know'],['know','knew','will know']]
    to_want = [['want','wanted','will want'],['wants','wanted','will want'],['want','wanted','will want']]
    
    main_verbs = [to_be,to_have,to_see,to_know,to_want]
    
    verb = random.choice(main_verbs)
    verb_chosen = verb[noun_variable]
    verb_real_chosen = verb_chosen[tense]
    return verb_real_chosen

def take_preposition():
    preposition_list = ["about","above","across","after","along","around","at","before","behind",
    "below","beyond","by","despite","except","for","from","in","into","near","of",
    "off","on","onto","out","over","past","to","under","with","without",]
    
    preposition = random.choice(preposition_list)
    return preposition

def take_prepositioinal_phrase():
    first_phrase = ['around the corner', 'ontop of the hill', 'at the lake', ]
    second_phrase = ['at the beach', 'up the hill', 'during the game', 'during the storm',]
    third_phrase = ['over the mountain', 'on the edge of the cliff', 'on the hiking trail',]

    phrases = [first_phrase,second_phrase,third_phrase]
    phrase_chosen = random.choice(phrases)
    phrase_real_chosen = random.choice(phrase_chosen)


def take_indirect_object():
    object_used = ['the raisins','the landscapes','the sea','him','the policy','the librarian','traveling','cats']
    object_real = random.choice(object_used)
    return object_real

def take_direct_object():
    object_main = ['it','them','him','her','you']
    object_real = random.choice(object_main)
    return object_real

def main():
    noun_p = take_noun()
    determine_p = getting_determinated(determinated_variable)
    verb_p = take_verb(noun_variable)
    preposition_p = take_preposition()
    indirect_object_p = take_indirect_object()
    direct_object_p = take_direct_object()
    prep_phrase_p = take_prepositioinal_phrase()

    sentence_structures = ['sub_verb_dp', 'det_sub_verb_prep_dp', 'det_sub_verb_dp_prep_io', 'det_sub_verb_dp_prep_io_pp',]
    sentence_structure = random.choice(sentence_structures)

    if sentence_structure == 'sub_verb_dp':
        phrase_p = (f'{determiner_p} {noun_p} {verb_p} {direct_object_p}')
    if sentence_structure == 'det_sub_verb_prep_dp':
        phrase_p = (f'{determiner_p} {noun_p} {verb_p} {preposition_p} {direct_object_p}')
    if sentence_structure == 'det_sub_verb_dp_prep_io':
        phrase_p = (f'{determiner_p} {noun_p} {verb_p} {direct_object_p} {preposition_p} {indirect_object_p}')
    if sentence_structure == 'det_sub_verb_dp_prep_io_pp':
        phrase_p = (f'{determiner_p} {noun_p} {verb_p} {direct_object_p} {preposition_p} {indirect_object_p} {prep_phrase_p}')

    print(phrase_p)

main()