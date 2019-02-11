# import statistics

def mean_num_friends(x):
    # TODO
    # total = 0
    # [total += val for val in x]
    # return total
    return sum(x)/len(x)


def median_num_friends(x):
    # An easier way if importing libraries
    # result = statistics.median(x)
    
    list_len = len(x)
    x_sorted = sorted(x)

    if list_len == 0:
        return None
    if list_len % 2 == 1:
        middle_index = int((list_len-1)/2)
        return x_sorted[middle_index]
    else:
        first_val = x_sorted[int((list_len/2)-1)]
        second_val = x_sorted[int(list_len/2)]
        avg = (first_val + second_val)/2
        return avg

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print(mean_num_friends(num_friends))
print(median_num_friends(num_friends))

