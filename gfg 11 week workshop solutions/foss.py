def count_unique(string):
    hash = {}
    for i in string:
        i.lower()
        if i in hash.keys():
            pass
        else:
            hash[i] = 1
    return len(hash)

print(count_unique("a banana He hE he"))
