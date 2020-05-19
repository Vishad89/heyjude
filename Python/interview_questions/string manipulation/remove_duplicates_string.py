
def remove_duplicates_string(str):
    str = list(str)
    arr = []
    for i in range(len(str)-1):
        if str[i] not in arr:
            arr.append(str[i])
        else:
            pass
    return (''.join(arr))

print(remove_duplicates_string("abccceedddfasfgadad"))