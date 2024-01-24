def firstPalindrome(words):
        flag  = 1
        for word in words:
            i = 0
            j = len(word)-1
            while(i< len(word)//2 or j >= len(word)//2):
                if word[i] == word[j]:
                    i = i + 1
                    j = j - 1
                    continue
                else:
                    flag = 0
                    break
            if flag == 0:
                flag = 1
                continue
            else:
                return word
        return ""

print(firstPalindrome(["xngla","e","itrn","y","s","pfp","rfd"]))
