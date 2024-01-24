def decodeMessage(key , message):
    alpahabets='abcdefghijklmnopqrstuvwxyz'
    decode={' ':' '}
    i = 0
    res = ""

    for char in key:
        if char not in decode:
            decode[char]= alpahabets[i]
            i = i + 1
    for char in message:
        res = res + decode[char]


    return res

print(decodeMessage("the quick brown fox jumps over the lazy dog","vkbs bs t suepuv"))
