"""
CVR COLLEGE OF ENGINEERING AND TECHNOLOGY
DEPARTMENT OF ARTIFICIAL INTELLIGENCE
PROGRAM: A CROSSWORD PUZZLE PROBLEM WITH 10 WORDS
BY: MIR HABEEBULLAH SHAH QUADRI
ROLL NO: 18B81DA914
CLASS: MTECH - I YEAR (AI)
UNDER THE GUIDANCE AND SUPERVISION OF: DR.PONUSAMY

"""

crosswords=[['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
            ['a', 'd', 'o', 'g', 'b', 'c', 'r', 'e'],
            ['a', 'b', 'c', 'c', 'a', 't', 'a', 'l'],
            ['b', 'l', 'i', 'o', 'n', 'i', 'b', 'e'],
            ['s', 'd', 'e', 'e', 'r', 'g', 'b', 'p'],
            ['n', 'b', 'c', 'a', 'b', 'e', 'i', 'h'],
            ['a', 'r', 'a', 't', 'c', 'r', 't', 'a'],
            ['k', 'm', 'o', 'n', 'k', 'e', 'y', 'n'],
            ['e', 'a', 'b', 'c', 'a', 'b', 'c', 't'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']]
           
words=['cat', 'dog', 'elephant', 'lion', 'tiger', 'snake', 'monkey', 'deer', 'rabbit', 'rat']

def capitalize_word_in_crossword(crosswords, words):
    for rownum, row in enumerate(crosswords):
        for word in words:
            find_index=''.join(row).lower().find(word)
            if find_index > 0:
                for i in range(find_index, len(word) + 1):
                    crosswords[rownum][i] = crosswords[rownum][i].upper()

    for colindex in range(len(crosswords[0])):
        for word in words:
            colvalues=[row[colindex] for row in crosswords]
            find_index=''.join(colvalues).lower().find(word)
            if find_index > 0:
                for i in range(find_index, len(word) + 1):
                    crosswords[i][colindex] = crosswords[i][colindex].upper()
    return crosswords

capitalize_word_in_crossword(crosswords, words)

for row in crosswords:
    print(row)
