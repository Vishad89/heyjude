# Python | Frequency of each character in String

def freq_char(str):
    result = {}
    for char in str:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    #return result.items()
    return (''.join(['%s%s' %(key,value) for (key,value) in result.items()]))

print(freq_char("aaaaabbbbcbsbbsbsfssgsgscsab"))