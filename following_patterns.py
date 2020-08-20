def areFollowingPatterns(string, pattern):
    string_set = set()
    pattern_set = set()

    for i in string:
        string_set.add(i)
    for i in pattern:
        pattern_set.add(i)
    return len(string_set) == len(pattern_set)


string = ["cat", "dog", "doggy"]
pattern = ["a", "b", "b"]

print(areFollowingPatterns(string, pattern))
