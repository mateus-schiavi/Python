from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():

    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        word = get_determiner(1).lower()

        assert word in single_determiners


    plural_determiners = ["some", "many", "the"]

    for _ in range(4):

        word = get_determiner(2).lower()

        assert word in plural_determiners


def test_get_noun():

    single_nouns = ['butterfly', 'motorcycle', 'board', 
                 'cat', 'child', 'snake', 
                 'girl', 'man', 'rabbit', 
                 'woman']

    for _ in range(4):

        word = get_noun(1)

        assert word in single_nouns


    plural_nouns = ['butterflies', 'motorcycles', 'boards', 
                 'cats', 'children', 'snakes', 
                 'girls', 'men', 'rabbits', 
                 'women']

    for _ in range(4):

        word = get_noun(2)

        assert word in plural_nouns


def test_get_verb():
    
    past_verbs = ['slept', 'swam', 'grew', 
                 'laughed', 'ran', 'played', 
                 'opened', 'talked', 'walked', 
                 'wrote']
    
    for _ in range(4):
        word = get_verb(1, 'past')
        
        assert word in past_verbs
        
        
    
    singular_present_verbs = ['sleeps', 'swims', 'grows', 
                     'laughs', 'runs', 'plays', 
                     'opens', 'talks', 'walks', 
                     'writes']
    
    for _ in range(4):
        word = get_verb(1, 'present')
        
        assert word in singular_present_verbs
        
        
    
    plural_present_verbs = ['sleep', 'swim', 'grow', 
                     'laugh', 'run', 'play', 
                     'open', 'talk', 'walk', 
                     'write']
    
    for _ in range(4):
        word = get_verb(2, 'present')
        
        assert word in plural_present_verbs
              
        
    
    future_verbs = ['will sleep', 'will swim', 'will grow', 
                 'will laugh', 'will run', 'will play', 
                 'will open', 'will talk', 'will walk', 
                 'will write']
    
    for _ in range(4):
        word = get_verb(2, 'future')
        
        assert word in future_verbs
    
    
def test_get_preposition():
    
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
    
    for _ in range(4):
        
        word = get_preposition()
        
        assert word in prepositions
    
    
def test_get_prepositional_phrase():
    
    for _ in range(4):
        
        phrase =  get_prepositional_phrase(1).split(' ')

        assert len(phrase) == 4
        
    for _ in range(4):
        
        phrase =  get_prepositional_phrase(2).split(' ')
        
        assert len(phrase) == 4

    
pytest.main(["-v", "--tb=line", "-rN", __file__])