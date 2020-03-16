def first_non_repeating_character(str1):
    char_order = []
    count = {}
    for c in str1:
        if c in count:
            count[c] += 1
        else:
            count[c] = 1
            char_order.append(c)
    for c in char_order:
        if count[c] == 1:
            return c
    return None

print(first_non_repeating_character('aabbcce'))
