#!/usr/bin/python3
"""python module with all the question"""

# Define questions for each subject
football_questions = [
    {'text': 'Which player has the most Fifa the best awards': 'correct_answer': 'Lionel Messi'},
    {'text': 'How many minutes is a full football game': 'correct_answer': '90 minutes'},
    {'text': 'What is so fascinating about Sheffield F.C': 'correct answer': 'Its the oldest football club in the world'},
    {'text': 'Which country has the most world cups': 'correct answer': 'Brazil'},
    {'text': 'Where and when was football invented': 'correct answer': 'China, 476.B.C'},
    {'text': 'How many people watch the FIFA world cup': 'correct answer': '3.5 billion'},
    {'text': ' Which player has the most world cup goals': 'correct answer': 'Miroslav Klose'},
    {'text': 'Which African nations have hosted the worldcup': 'correct answer': 'South Africa, 2010'},
    {'text': 'which club and player has the most UEFA titles': 'correct answer': 'Real Madrid, Cristiano Ronaldo'},
]

cricket_questions = [
    {'text': 'Which cricket league is the largest and lucrative in the world': 'correct answer': 'Indian Premier League'},
    {'text': 'Which nation has the most cricket world cups and how many': 'correct answer': 'Australia, five'},
    {'text': 'Which player has the most sixes and from which country': 'correct answer': 'Chris Gayle, West Indies'},
    {'text': 'which player is the fastest ever to score 3000 ODI runs': 'correct answer': 'Hashim Amla'},
    {'text': 'what does ODI stands for': 'correct answer': 'One Day International'},
]

Geography questions = [
        {'text': 'You have to cross the famously dangerous Darién Gap to cross between which two countries': 'correct answer': 'Panama and Columbia'},
        {'text': 'In which mountains would you find Camp David': 'correct answer': 'Appalachian'},
        {'text': 'Which is the only African country to share a land border with another continent': 'correct answer': 'Egypt'},
        {'text': 'Which country is completely surrounded by South Africa': 'correct answer': 'Lesotho'},
        {'text': 'Antananarivo is also a fun word to say, as is the country it is in. Where is it the capital of': 'correct answer': 'Madagascar'},
        {'text': 'Mount Everest can be approached from which two countries': 'correct answer': 'Nepal and China'},
        {'text': 'Which ocean is the world’s most northerly': 'correct answwer': 'The Arctic Ocean'},
        {'text': 'Which river flows 1,680 miles from the Himalayas to the coast of Bangladesh': 'correct answer': 'The Ganges'},
        {'text': 'Which capital city in Africa starts and ends with the same pair of letters, which also occur a third time in the middle of the city’s name': 'correct answer': 'Ouagadougou (Burkina Faso)'},
        {'text': 'How many countries are there in the world': 'correct answer': '195'},
]

African History Questions = [
        {'text': 'Which of these African civilizations was the only one to experience the Bronze Age': 'correct answer': 'Nubia'},
        {'text': 'What year was the Organization of African Unity (OAU) established': 'correct answer': '1963'},
        {'text': 'King Leopold II of Belgium disguised his conquest of the Congo by ending the slave trade and introducing Christianity. However, he was really only interested in the Congo primarily for which of these pairs of resources': 'correct answer': 'Ivory and rubber'},
        {'text': 'According to the "Grand Theory" of Bantu migration and conquest, where did the Bantu people originate from': 'correct answer': 'Southeastern Nigeria'},
        {'text': 'Which country is named after ancient ruins found in it': 'correct answer': 'Zimbabwe'},
        {'text': 'Which African country has its own alphabet': 'correct answer': 'Ethiopia, Ge`ez'},
]

Science questions = [
        {'text': 'In what tabular display are the chemical elements typically displayed': 'correct answer': 'Periodic table'},
        {'text': 'What tissue connects bone to muscle': 'correct answer': 'Tendons'},
        {'text': 'Anaemia is caused by the deficiency of which mineral in the human diet': 'correct answer': 'iron'},
        {'text': 'How is ‘Sound Navigation and Ranging’ more commonly known': 'correct answer': 'Sonar'},
        {'text': 'Elemental gases such as helium, neon, argon and krypton are grouped under what honourable term': 'correct answer': 'noble gases'},
        {'text': 'What links the helix, scapha, triangular fossa and concha': 'correct answer': 'Parts of the outer ear'},
        {'text': 'What is the name of the Martian volcano that is three times the size of Mount Everest': 'correct answer': 'Olympus Mons. It is 600 km wide and 21 km high'},
        {'text': 'What name is given to the natural, internal process that regulates the sleep-wake cycle': 'correct answer': 'Circadian rhythm'},
        {'text': 'A vector describes the movement between two points, quantifying which two aspects': 'correct answer': 'distance and force(magnitude)'}
        {'text': 'Described as the USA’s greatest inventor, which man, who generally had only three or four hours sleep a night, counted amongst his inventions something which contributed to reducing the amount of sleep humans get': 'correct answer': 'Thomas Edison, who invented the lightbulb'},
        {'text': 'Dolphins travel in family groups called what': 'correct answer': 'pods'},
]

# Define functions to retrieve questions
def get_football_questions():
    return football_questions

def get_cricket_questions():
    return cricket_questions

def get_africanhistory_questions():
    return africanhistory_questions

def get_geography_questions():
    return geography_questions

def get_science_questions():
    return science_questions
