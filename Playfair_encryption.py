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
    bigram = ''
    count = 0
    for char in word:
        # print(char)

        if char == ' ':
            continue
        if char in bigram:
            bigram += 'X'
            bigramm_arr.append(bigram)
            count = 1
            bigram = char
            continue
        bigram += char

        count += 1
        if count == 2:
            bigramm_arr.append(bigram)
            bigram = ''
            count = 0

    return bigramm_arr


def encrypt(matrix, biagram_arr):
    encrypted_biagram_arr = []
    encrypted_biagram = ''
    i1 = 0
    j1 = 0
    i2 = 0
    j2 = 0
    count = 0
    for bi in biagram_arr:
        for char in bi:
            for i, row in enumerate(matrix):
                for j, element in enumerate(row):
                    if element == char:
                        if count == 0:
                            i1 = i
                            j1 = j
                            count += 1
                        elif count == 1:
                            i2 = i
                            j2 = j
                            count = 0
        if i1 == i2:
            if j1 == 4:
                j2 += 1
                j1 = 0
            elif j2 == 4:
                j1 += 1
                j2 = 0
            else:
                j1 += 1
                j2 += 1
        elif j1 == j2:
            if i1 == 4:
                i1 = 0
            elif i2 == 4:
                i2 = 0
            else:
                i1 += 1
                i2 += 1
        else:
            tmp = j1
            j1 = j2
            j2 = tmp

        encrypted_biagram = f"{matrix[i1][j1]}{matrix[i2][j2]}"
        encrypted_biagram_arr.append(encrypted_biagram)
        encrypted_biagram = ''

    return encrypted_biagram_arr

keyword = "TRUTH"
word = "LITTLE STROKES FELL GREAT OAKS"

playfair_matrix = generate_playfair_matrix(keyword)
biagram = generate_biagram(word)
encrypted_biagram = encrypt(playfair_matrix, biagram)


print('Matrix:')
for row in playfair_matrix:
    print(row)
print('\n\nBiagram:')
print(biagram)
print('\n\nEncrypted Biagram:')
print(encrypted_biagram)
