import random

import pytest

from sentences import (get_det, get_n, get_prepo,
                       get_prepo_phrase, get_verb, get_adj,get_adv)


def test_get_determiner():

    single_determiners = ["a", "one", "the"]

    for _ in range(4):

        word = get_determiner(1)

        assert word in single_determiners

    plural_determiners = ["two", "some", "many", "the"]

    for _ in range(4):

        quantity = random.randint(2, 11)

        word = get_determiner(quantity)

        assert word in plural_determiners
        
def test_get_noun():
    
    single_nouns = ['bird', "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    
    for _ in range(10):
    
        noun = get_noun(1)
    
        assert noun in single_nouns
        
    plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(10):
        
        quantity = random.randint(2, 11)
        
        noun = get_noun(quantity)
        
        assert noun in plural_nouns
        
def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    
    for _ in range(4):
        
        past_verb = get_verb(1, "past")
        
        assert past_verb in past_verbs
        
    single_present = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    
    for _ in range (4):
        
        single_present_verb = get_verb(1, "present")
        
        assert single_present_verb in single_present
    
    plural_present = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    
    for _ in range (4):
        
        quantity = random.randint(2, 11)
        
        plural_present_verb = get_verb(quantity, "present")
        
        assert plural_present_verb in plural_present
        
    future_tense = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    
    for _ in range(4):
        
        quantity = random.randint(2, 11)
        
        future = get_verb(quantity, "future")
        
        assert future in future_tense

def test_get_preposition():
    
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = get_preposition()
    
    assert preposition in prepositions

def test_prepositional_phrase():
    for _ in range(30):
        
        single_determiners = ["a", "one", "the"]
        
        single_nouns = ['bird', "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
        
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        
        single_prepositional_phrase = get_prepositional_phrase(1)
        
        list = single_prepositional_phrase.split()
        
        list_length = len(list)
        
        assert list_length == 3
        assert list[0] in prepositions
        assert list[1] in single_determiners
        assert list[2] in single_nouns
    
def test_prepositional_phrase():
    for _ in range(30):
        
        plural_determiners = ["two", "some", "many", "the"]
        
        plural_nouns = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
        
        prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        
        plural_prepositional_phrase = get_prepositional_phrase(0)
        
        list = plural_prepositional_phrase.split()
        
        list_length = len(list)
        
        assert list_length == 3
        assert list[0] in prepositions
        assert list[1] in plural_determiners
        assert list[2] in plural_nouns
        
pytest.main(["-v", "--tb=line", "-rN", __file__])