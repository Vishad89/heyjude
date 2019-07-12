# permutation of string

def permutations(word):
    if len(word)<= 1:
        return [word]
 
    #get all permutations of length N-1
    perms=permutations(word[1:])
    print(perms)
    char=word[0]
    print(char)
    result=[]
    #iterate over all permutations of length N-1
    for perm in perms:
        #insert the character into every possible location
        #print(perm)
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
            print(perm), print(len(perm)+1)
    return result

print(permutations("ABCDE"))
