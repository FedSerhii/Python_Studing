def find_even_index(arr):

    total_sum = sum(arr)
    left_sum = 0

    for key, value in enumerate(arr):
        total_sum -= value

        if left_sum == total_sum:
            return key

        left_sum += value

    return -1


print(find_even_index([1,2,3,4,3,2,1]))

