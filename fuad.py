# Define a custom comparator function
def custom_comparator(tuple1, tuple2):
    if tuple1[1] < tuple2[1]:
        return -1
    elif tuple1[1] > tuple2[1]:
        return 1
    else:
        if tuple1[0] < tuple2[0]:
            return -1
        elif tuple1[0] > tuple2[0]:
            return 1
        else:
            return 0

# List of tuples to be sorted
tuples = [(1, 3), (2, 2), (3, 3), (4, 1), (5, 2)]

# Sort the list using the custom comparator
sorted_tuples = sorted(tuples, key=lambda x: (x[1], x[0]))

print(sorted_tuples)
