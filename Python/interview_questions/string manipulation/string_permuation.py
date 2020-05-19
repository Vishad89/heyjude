
def permute_string(str):
    if len(str) <= 1:
        return [str]
   
    perms = permute_string(str[1:])
    print(perms)
    char=str[0]
    print(char)
    result = []
    for perm in perms:
        for i in range(len(perm)+1):
            result.append(perm[:i] + char + perm[i:])
    return result


print(permute_string("abcde"))