
def permute_string(str):
    if len(str) == 1:
        return [str]
   
    perms = permute_string(str[1:])
    char = str[0] 
permute_string("abc")