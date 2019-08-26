def sum_lengths(word_list):
    accumulator = 0
    for word in word_list:
        accumulator += len(word)
    return accumulator


print(sum_lengths([]))

