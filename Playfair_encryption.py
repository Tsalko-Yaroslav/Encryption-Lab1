


def generate_playfair_matrix(keyword):
    matrix = []
    keyword = keyword.upper().replace("J", "I")
    for char in keyword:
        if char not in matrix and char.isalpha():
            matrix.append(char)

    alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)

    playfair_matrix = [matrix[i:i + 5] for i in range(0, 25, 5)]

    return playfair_matrix

def generate_biagram(word):
    bigramm_arr = []
    bigram = ""
    count = 0

    for letter in word:
        if letter == ' ':
            continue


        if count == 2:
            bigramm_arr.append(bigram)
            bigram = ""
            count = 0
        else:
            if bigram != letter:
                bigram += letter
            else:
                continue
            count += 1
        if count == 1:
            bigramm_arr.append(bigram + 'X')



    return bigramm_arr



keyword = "TRUTH"
word = "LITTLE STROKES FELL GREAT OAKS"


playfair_matrix = generate_playfair_matrix(keyword)
biagram = generate_biagram(word)
print('Matrix:')
for row in playfair_matrix:
    print(row)

print('\n\nBiagram:')
print(biagram)