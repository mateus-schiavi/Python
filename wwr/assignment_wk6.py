import random
import re

#make the program select random tense
tenses = [0,1,2] # present, past, future
tense = random.choice(tenses)

#determining  noun
def get_noun():
    global noun_var
    global determiner_var
    determiner_var = 0

    nouns1 = ['I']
    nouns2 = ['Cartoon','Crowd','Book or Mormon', 'School','animal','school','BYU']
    nouns3 = ['people','century','week','business']
    nouns4 = ['you','they']
    #allows the program to choose any form from any subject line
    nouns = [nouns1,nouns2,nouns3,nouns4]
    nouns_choice = random.choice(nouns)
    nouns_choice_real = random.choice(nouns_choice)

    #determining which kind of tense the program will acquire
    if nouns_choice == nouns1:
        noun_var = 0
        determiner_var = 0
    elif nouns_choice == nouns2:
        noun_var = 1
        determiner_var = 1
    elif nouns_choice == nouns3:
        noun_var = 2
        determiner_var = 2
    elif nouns_choice == nouns4:
        noun_var = 2
        determiner_var = 0
    else:
        print('error')
    
    return(nouns_choice_real)

#get determiners

def get_determiner(determiner_var):

    determiner_none = ''
    determiner_sg = ['the','a']
    determiner_pl = ['many','some']
   
    if determiner_var == 0:
        determiner_real = determiner_none
        return determiner_real
    elif determiner_var == 1:
        determiner_real = random.choice(determiner_sg)
        return determiner_real
    elif determiner_var == 2:
        determiner_real = random.choice(determiner_pl)
        return determiner_real
  
#set up the nouns
# def get_noun():
#     nouns = [""]

def get_verb(noun_var):
    
    global tenses
    tenses = [0,1,2] # present, past, future
    #randomize verb tense
    tense = random.choice(tenses)
    
    to_be = [['am','was','will be'],['is','was','will be'],['are','were','will be']]
    to_have = [['have','had','will have'],['has','had','will have'],['have','had','will have']]
    to_see = [['see','saw','will see'],['sees','saw','will see'],['see','saw','will see']]
    to_know = [['know','knew','will know'],['knows','knew','will know'],['know','knew','will know']]
    to_want = [['want','wanted','will want'],['wants','wanted','will want'],['want','wanted','will want']]

    #allow program to know what to randomize
    verbs = [to_be,to_have,to_see,to_know,to_want]

    verb = random.choice(verbs)
    verb_choice = verb[noun_var]  #choose subject
    verb_choice_real = verb_choice[tense] #choose tense
    return verb_choice_real

def get_preposition():
    prepositions = ["about","above","across","after","along","around","at","before","behind",
    "below","beyond","by","despite","except","for","from","in","into","near","of",
    "off","on","onto","out","over","past","to","under","with","without",]
    
    #radnomize the proposition
    preposition = random.choice(prepositions)
    return preposition

#Get prepositional phrases
def get_prepositioinal_phrase():
    phrase1 = ['around the corner', 'ontop of the hill', 'at the lake', ]
    phrase2 = ['at the beach', 'up the hill', 'during the game', 'during the storm',]
    phrase3 = ['over the mountain', 'on the edge of the cliff', 'on the hiking trail',]

    phrases = [phrase1,phrase2,phrase3]
    phrase_choice = random.choice(phrases)
    phrase_choice_real = random.choice(phrase_choice)


#set indirect objects
def get_indirect_object():
    objects = ['the raisins','the landscapes','the sea','him','the policy','the librarian','traveling','cats']
    object_real = random.choice(objects)
    return object_real

#set indirect objects
def get_direct_object():
    objects = ['it','them','him','her','you']
    object_real = random.choice(objects)
    return object_real

def main():
    noun_p = get_noun()
    determiner_p = get_determiner(determiner_var)
    verb_p = get_verb(noun_var)
    preposition_p = get_preposition()
    indirect_object_p = get_indirect_object()
    direct_object_p = get_direct_object()
    prep_phrase_p = get_prepositioinal_phrase()

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

#    phrase_p = phrase_p.lstrip()
#    phrase_p = re.sub("\s\s+", " ", phrase_p)
#    phrase_p = phrase_p.capitalize()
    print(phrase_p)

main()