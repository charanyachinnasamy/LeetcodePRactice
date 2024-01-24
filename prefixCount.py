def prefixCount(words,pref):
    prefix_length = len(pref)
    c = 0
    for word in words:
        i = 0
        while(i<prefix_length and i < len(word)):
            print(i,word[i],pref[i])
            if word[i]== pref[i]:
                i = i + 1
                continue
            else:
                break
        if i == prefix_length:
            c = c + 1
    return c

print(prefixCount(["kttxeksggb","vucqwew","lyknscc","mryl","vwarnwkfmd","ivawxbntgs","mylw","namybmfy","uosag","rzernqxyn","puf","hfwjnmvm","jjfyd","xteybd","v","ywntwzn","npsogop","brgvlw","vewhi","brk","hheub","zl","vt","bxjtjivep","p","io","xotulskjmt","mctffonh","pmeuqhoe","ghktrtq","u","ngnvwan","pqmlvvhl","enjf","qomcejb","twgqww","bnilyqy","nc","fttlodnz","fya","g","uoivsr","gtxgcaf","qs","gkfl","sdmacxf","mzy","xjv","yipc","rctqugjjk","myij","xxg","vyup","utqxplpsa","imbteaczlc","qfgdcz","atfn","pxcsg","f","omukbiaudb","uh","uobwgt","hgqipk","zunfzinenk","i","p","pet","fxai","ortqpwkukg","rxgh","ylfh"],"ikwjoty"))


