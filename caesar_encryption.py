print('Caesar encryption\n\n\n')

K = 7

INPUT = "TSALKO"
print(f"Input: {INPUT}")
enWord = ""
kIndex=0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
idx = 0
for letter in INPUT:
    index = alphabet.index(letter)
    kIndex = int(K+index)
    if kIndex > 25:
        kIndex = int(kIndex - (len(alphabet)))
    enWord += str(alphabet[kIndex])

print(f"Encrypted: {enWord}")

denWord = ""
for letter in enWord:
    index = alphabet.index(letter)
    kIndex = int(index - K)
    if kIndex < 0:
        kIndex = int((len(alphabet) - K))
    denWord += str(alphabet[kIndex])

print(f"Decrypted: {denWord}")