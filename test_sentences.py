from sentences import get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import pytest


def test_get_determiner():
    """Call and test the get_determiner function 
    Parameters:
        none 
    """
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1).lower()

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(2).lower()

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    """Call and test the get_noun function 
    Parameters:
        none 
    """
    # 1. Test the single nouns.

    single_nouns = ['bird', 'boy', 'car', 'cat', 'child', 'dog', 'girl', 'man', 'rabbit', 'woman']

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_noun(1)

        # Verify that the word returned from get_noun
        # is one of the words in the single_nouns list.
        assert word in single_nouns

    # 2. Test the plural nouns.

    plural_nouns = ['birds', 'boys', 'cars', 'cats', 'children', 'dogs', 'girls', 'men', 'rabbits', 'women']

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Call the get_noun function which
        # should return a plural noun.
        word = get_noun(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_nouns


def test_get_verb():
    """Call and test the get_verb function 
    Parameters:
        none 
    """
    # 1. Test the past verbs.
    
    past_verbs = ['drank', 'ate', 'grew', 'laughed', 'thought', 'ran', 'slept', 'talked', 'walked', 'wrote']
    
    for _ in range(4):
        # Call the get_verb function which
        # should return a past tense verb.
        word = get_verb(1, 'past')
        
        # Verify that the word returned from get_verb
        # is one of the words in the past_verbs list.
        assert word in past_verbs
        
        
    # 2. Test the present singular verbs.  
    
    singular_present_verbs = ['drinks', 'eats', 'grows', 'laughs', 'thinks', 'runs', 'sleeps', 'talks', 'walks', 'writes']
    
    for _ in range(4):
        # Call the get_verb function which
        # should return a singular present tense verb.
        word = get_verb(1, 'present')
        
        # Verify that the word returned from get_verb
        # is one of the words in the singular_present_verbs list.
        assert word in singular_present_verbs
        
        
    # 3. Test the present plural verbs.
    
    plural_present_verbs = ['drink', 'eat', 'grow', 'laugh', 'think', 'run', 'sleep', 'talk', 'walk', 'write']
    
    for _ in range(4):
        # Call the get_verb function which
        # should return a singular present tense verb.
        word = get_verb(2, 'present')
        
        # Verify that the word returned from get_verb
        # is one of the words in the singular_present_verbs list.
        assert word in plural_present_verbs
              
        
    # 4. Test the future verbs.
    
    future_verbs = ['will drink', 'will eat', 'will grow', 'will laugh', 'will think', 'will run', 'will sleep', 'will talk', 'will walk', 'will write']
    
    for _ in range(4):
        # Call the get_verb function which
        # should return a future tense verb.
        word = get_verb(2, 'future')
        
        # Verify that the word returned from get_verb
        # is one of the words in the singular_present_verbs list.
        assert word in future_verbs
    
    
def test_get_preposition():
    """Call and test the get_preposition function
    Parameters:
        none
    """
    
    prepositions = ['about', 'above', 'across', 'after', 'along',
        'around', 'at', 'before', 'behind', 'below',
        'beyond', 'by', 'despite', 'except', 'for',
        'from', 'in', 'into', 'near', 'of',
        'off', 'on', 'onto', 'out', 'over',
        'past', 'to', 'under', 'with', 'without']
    
    for _ in range(4):
        
        # Call the get_preposition function which
        # should return a preposition.
        word = get_preposition()
        
        # Verify that the word returned from get_preposition
        # is one of the words in the prepositions list.
        assert word in prepositions
    
    
def test_get_prepositional_phrase():
    """Call and test the get_prepositional_phrase function 
    Parameters:
        none 
    """
    
    for _ in range(4):
        
        # Call the get_prepositional_phrase function which
        # should return a phrase.
        phrase =  get_prepositional_phrase(1).split(' ')

        # Verify that the word count returned from get_prepositional_phrase
        # is equal to 4.
        assert len(phrase) == 4
        
    for _ in range(4):
        
        # Call the get_prepositional_phrase function which
        # should return a phrase.
        phrase =  get_prepositional_phrase(2).split(' ')
        
        # Verify that the word count returned from get_prepositional_phrase
        # is equal to 4.
        assert len(phrase) == 4
    
    
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])